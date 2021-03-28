from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import views


beer_router = DefaultRouter()
beer_router.register(r'beers', views.BeerViewset)

app_name = 'shop'
urlpatterns = [
    # path('', views.BeerListView.as_view(), name='beer-list'),
    path('', TemplateView.as_view(template_name='home.html')),
    path('api/', include(beer_router.urls))
]