from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.mixins import SearchMixin
from .forms import MarketplaceCreateForm
from .models import MarketplaceItem


class MarketplaceListView(SearchMixin, ListView):
    model = MarketplaceItem
    template_name = "marketplace/marketplace-list.html"
    context_object_name = "items"
    search_fields = ["title", "description"]

class MarketplaceDetailView(DetailView):
    model = MarketplaceItem
    template_name = "marketplace/marketplace-details.html"
    context_object_name = "item"

class MarketplaceCreateView(CreateView):
    model = MarketplaceItem
    form_class = MarketplaceCreateForm
    template_name = "marketplace/marketplace-create.html"
    success_url = reverse_lazy("marketplace:list")

class MarketplaceUpdateView(UpdateView):
    model = MarketplaceItem
    form_class = MarketplaceCreateForm
    template_name = "marketplace/marketplace-edit.html"

    def get_success_url(self):
        return reverse_lazy("marketplace:details", kwargs={"pk": self.object.pk})

class MarketplaceDeleteView(DeleteView):
    model = MarketplaceItem
    template_name = "marketplace/marketplace-delete.html"
    success_url = reverse_lazy("marketplace:list")
