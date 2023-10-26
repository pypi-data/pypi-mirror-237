from django.conf import settings
from django.db import connection
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from django_tenants import get_domain_model

from django_tenants.utils import remove_www


class TenantMainMiddleware(MiddlewareMixin):
    TENANT_NOT_FOUND_EXCEPTION = Http404
    """
    This middleware should be placed at the very top of the middleware stack.
    Selects the proper database schema using the request host. Can fail in
    various ways which is better than corrupting or revealing data.
    """

    @staticmethod
    def hostname_from_request(request):
        """ Extracts hostname from request. Used for custom requests filtering.
            By default, removes the request's port and common prefixes.
        """
        return remove_www(request.get_host().split(':')[0])

    def get_tenant(self, domain_model, hostname):
        if hostname in settings.PUBLIC_HOSTS:
            return None
        domain = domain_model.objects.select_related('tenant').get(domain=hostname)
        return domain.tenant

    def get_tenant_descendants(self, tenant):  # NOQA
        descendants = tenant.get_descendants(include_self=True)
        return [str(descendant.pk) for descendant in descendants]

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        hostname = self.hostname_from_request(request)

        domain_model = get_domain_model()
        try:
            tenant = self.get_tenant(domain_model, hostname)
        except domain_model.DoesNotExist:
            self.no_tenant_found(request, hostname)
            return

        if tenant:
            tenant.domain_url = hostname
            connection.set_main_tenant(tenant.get_root())
            connection.set_sub_tenant(tenant)
            connection.set_descendant_tenants(tenant.get_descendants(include_self=True))

        request.tenant = tenant

        self.setup_url_routing(request)

    def no_tenant_found(self, request, hostname):
        """ What should happen if no tenant is found.
        This makes it easier if you want to override the default behavior """
        if hasattr(settings, 'SHOW_PUBLIC_IF_NO_TENANT_FOUND') and settings.SHOW_PUBLIC_IF_NO_TENANT_FOUND:
            self.setup_url_routing(request=request, force_public=True)
        else:
            raise self.TENANT_NOT_FOUND_EXCEPTION('No tenant for hostname "%s"' % hostname)

    @staticmethod
    def setup_url_routing(request, force_public=False):
        if hasattr(settings, 'PUBLIC_URLCONF') and not request.tenant:
            request.urlconf = settings.PUBLIC_URLCONF
        elif hasattr(settings, 'ADMINISTRATIVE_URLCONF') and request.tenant.is_main:
            request.urlconf = settings.ADMINISTRATIVE_URLCONF
        else:
            request.urlconf = settings.ROOT_URLCONF


class Tenant:
    def __init__(self):
        pass
