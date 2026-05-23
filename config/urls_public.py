from django.contrib import admin
from django.urls import path
# from strawberry.django.views import GraphQLView
from django.views.generic import TemplateView
# from .schema import schema as public_schema


urlpatterns = [
    # Landing page (optional)
    path(
        "",
        TemplateView.as_view(template_name="pages/home.html"),
        name="home",
    ),

    # Public GraphQL (optional but common for SaaS auth/onboarding)
    # path("graphql/", GraphQLView.as_view(schema=public_schema)),

    # Public admin (usually disabled in production)
    path("admin/", admin.site.urls),
]
