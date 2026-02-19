from django.shortcuts import render
from django.views.generic import TemplateView
from reports.models import Report
from skills.models import Skill
from marketplace.models import MarketplaceItem
from .models import Announcement


class HomeView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["announcement"] = Announcement.objects.filter(is_active=True).first()
        context["latest_reports"] = Report.objects.all()[:3]
        context["latest_skills"] = Skill.objects.all()[:3]
        context["latest_items"] = MarketplaceItem.objects.all()[:3]

        return context


def about_page(request):
    return render(request, "common/about.html")
