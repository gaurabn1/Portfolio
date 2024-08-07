from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views import generic
from .forms import ContactProfileForm
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        portfolio = Portfolio.objects.filter(is_active=True)[:3]
        skills = Skill.objects.filter(is_key_skill=True)
        coding_skills = Skill.objects.filter(is_key_skill=False)
        user = UserProfile.objects.first()
        logos = Media.objects.filter(is_logo=True)
        certificates = Certificate.objects.filter(is_active=True)

        context['user'] = user
        context['portfolios'] = portfolio
        context['skills'] = skills
        context['coding_skills'] = coding_skills
        context['logos'] = logos
        context['certificates'] = certificates
        return context
    

class ContactView(generic.FormView):
    template_name = 'main/contact.html'
    form_class = ContactProfileForm
    success_url = '/'

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        messages.success(self.request, 'Thank You. We will be in touch soon.')
        return super().form_valid(form)
    
class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'
    paginate_by = 10
    context_object_name = 'portfolios'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'main/portfolio-detail.html'
    context_object_name = "portfolio"
    





