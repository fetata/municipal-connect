from django.urls import path
from .views import MarketplaceListView, MarketplaceDetailView, MarketplaceCreateView, MarketplaceUpdateView, \
    MarketplaceDeleteView

app_name = "marketplace"

urlpatterns = [
    path("", MarketplaceListView.as_view(), name="list"),
    path("create/", MarketplaceCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", MarketplaceUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", MarketplaceDeleteView.as_view(), name="delete"),
    path("<int:pk>/", MarketplaceDetailView.as_view(), name="details"),
]
