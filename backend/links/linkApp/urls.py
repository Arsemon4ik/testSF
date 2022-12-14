from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items

urlpatterns = [
    path('visited_links/', manage_items),
]
urlpatterns = format_suffix_patterns(urlpatterns)