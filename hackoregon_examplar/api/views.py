from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from api.models import RouteChange
from api.serializers import RouteChangeSerializer

class RouteChangeViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = RouteChange.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = RouteChangeSerializer
