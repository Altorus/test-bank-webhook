from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'organisations', views.OrganisationViewSet, basename='organisations')

urlpatterns = [
    path('webhook/bank', views.PaymentViewSet.as_view(), name='webhook-bank'),
    *router.urls
]
