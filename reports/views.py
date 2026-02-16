from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Report
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ReportCreateForm

class ReportListView(ListView):
    model = Report
    template_name = "reports/report-list.html"
    context_object_name = "reports"


class ReportDetailView(DetailView):
    model = Report
    template_name = "reports/report-details.html"
    context_object_name = "report"

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportCreateForm
    template_name = "reports/report-create.html"
    success_url = reverse_lazy("reports:list")

    def form_valid(self, form):
        return super().form_valid(form)

class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportCreateForm
    template_name = "reports/report-edit.html"

    def get_success_url(self):
        return reverse_lazy("reports:details", kwargs={"pk": self.object.pk})

class ReportDeleteView(DeleteView):
    model = Report
    template_name = "reports/report-delete.html"
    success_url = reverse_lazy("reports:list")