from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.staticfiles import finders
from django.views.generic import DetailView, ListView, TemplateView

from .models import Project


class HomeView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_projects"] = Project.objects.all()[:3]
        return context


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/projects.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["google_flow_video_exists"] = bool(finders.find("videos/googleFlowVideo.mp4"))
        return context


class SkillsView(TemplateView):
    template_name = "portfolio/skills.html"


class ResumeView(LoginRequiredMixin, TemplateView):
    template_name = "portfolio/resume.html"


class ContactView(TemplateView):
    template_name = "portfolio/contact.html"
