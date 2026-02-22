from django.urls import path
from .views import ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView

app_name = "reports"

urlpatterns = [
    path("", ReportListView.as_view(), name="list"),
    path("<int:pk>-<slug:slug>/", ReportDetailView.as_view(), name="details"),
    path("create/", ReportCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", ReportUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", ReportDeleteView.as_view(), name="delete"),
]
