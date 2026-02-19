from django.urls import path
from common import views
from common.views import HomeView

app_name = "common"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", views.about_page, name="about"),
]
