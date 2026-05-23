# core/views.py

from django.http import JsonResponse
from django.db import connection

def tenant_debug(request):
    return JsonResponse({
        "schema": connection.schema_name,
        "tenant": str(request.tenant),
    })
