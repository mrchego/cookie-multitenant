# config/graphql.py
import strawberry

from cookie_multitenant.tenants.schema import Query
from cookie_multitenant.tenants.mutations import Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
