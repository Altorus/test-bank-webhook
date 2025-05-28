from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'webhook/bank', views.PaymentViewSet, basename='webhook-bank')
router.register(r'organisations', views.OrganisationViewSet, basename='organisations')

urlpatterns = [
    *router.urls
]
