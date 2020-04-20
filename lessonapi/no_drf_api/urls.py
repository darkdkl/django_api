from django.urls import path, include
from .views import ApiView, DRFView, MLWDRFView, DRPresentationView, PresentationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PresentationViewSet)

urlpatterns = [
    path('', ApiView.as_view(), name = 'get_api'),
    path('drf/', DRFView.as_view(), name = 'get_drf_api'),
    path('drf_mlw/', MLWDRFView.as_view(), name = 'get_drf_mlw'),
    path('drf_view/', DRPresentationView.as_view(), name = 'get_drf_view'),
    path('model/', include(router.urls)),
]
