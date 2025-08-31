from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values()
    return JsonResponse(list(properties), safe=False)

from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    return JsonResponse(properties, safe=False)
