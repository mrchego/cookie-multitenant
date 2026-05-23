# tenants/services.py
from cookie_multitenant.tenants.models import Tenant


def create_tenant_service(*, name: str, slug: str) -> Tenant:
    tenant = Tenant.objects.create(
        name=name,
        slug=slug,
        schema_name=slug,  # important: keeps django-tenants consistent
    )

    return tenant
