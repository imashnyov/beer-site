from django.views.generic import ListView
from .models import Beer

# Create your views here.
class BeerListView(ListView):
    model = Beer
    template_name = 'beer_list.html'