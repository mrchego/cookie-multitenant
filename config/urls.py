from django.conf import settings
from django.urls import include, path
import debug_toolbar

from cookie_multitenant.core.views import tenant_debug
from django.contrib import admin

urlpatterns = [
    path("", tenant_debug),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
