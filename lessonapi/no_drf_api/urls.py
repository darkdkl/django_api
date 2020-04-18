from django.urls import path
from .views import ApiView,DRFView


urlpatterns = [
    path('', ApiView.as_view(),name= 'get_api'),
    path('drf/',DRFView.as_view(),name='get_drf_api')
]