from django.views.generic import ListView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Beer
from .serializers import BeerListSerializer

# Create your views here.
class BeerListView(ListView):
    model = Beer
    template_name = 'beer_list.html'


class BeerViewset(ReadOnlyModelViewSet):
    queryset = Beer.objects.all()

    def get_serializer_class(self):
        return BeerListSerializer



