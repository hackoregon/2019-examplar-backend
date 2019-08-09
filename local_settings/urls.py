from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

api_title = 'Hack Oregon Examplar 2019 API'

schema_view = get_swagger_view(title=api_title)


urlpatterns = [
    url(r'^examplar/schema/', schema_view),
    url(r'^examplar/api/', include('hackoregon_examplar.api.urls')),
    url(r'^examplar/docs/', include_docs_urls(title=api_title)),
    url(r'^examplar/health/', include('health_check.urls'))
]

url(r'^$', schema_view)
