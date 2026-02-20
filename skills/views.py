from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.mixins import SearchMixin
from .forms import SkillCreateForm
from .models import Skill


class SkillListView(SearchMixin, ListView):
    model = Skill
    template_name = "skills/skill-list.html"
    context_object_name = "skills"
    search_fields = ["name", "description"]

class SkillDetailView(DetailView):
    model = Skill
    template_name = "skills/skill-details.html"
    context_object_name = "skill"

class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillCreateForm
    template_name = "skills/skill-create.html"
    success_url = reverse_lazy("skills:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Skill created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillCreateForm
    template_name = "skills/skill-edit.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.warning(self.request, "Skill updated.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("skills:details", kwargs={"pk": self.object.pk})

class SkillDeleteView(DeleteView):
    model = Skill
    template_name = "skills/skill-delete.html"
    success_url = reverse_lazy("skills:list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.warning(self.request, "Skill deleted.")
        return response
