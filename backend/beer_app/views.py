from django.views import generic
from django.views.generic import ListView
from django.db.models import Avg
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet

from .models import Beer
from .serializers import BeerListSerializer, BeerSerializer


class BeerViewset(ModelViewSet):
    queryset = Beer.objects.all().annotate(raiting=Avg('user_comments__mark'))
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return BeerListSerializer
        return BeerSerializer
