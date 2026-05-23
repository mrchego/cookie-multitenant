import strawberry

from .services import create_tenant_service


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_tenant(self, name: str, slug: str) -> str:
        tenant = create_tenant_service(
            name=name,
            slug=slug,
        )

        return tenant.schema_name
