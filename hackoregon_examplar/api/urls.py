from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'routes/change', views.RouteChangeViewSet, base_name='api')

urlpatterns = [
    url(r'^', include(router.urls)),
]
