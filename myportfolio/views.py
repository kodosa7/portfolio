from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Personal, Contact, Skill, History, Course, Portfolio


# homepage view
def home_view(request):
    queryset_personal = Personal.objects.all()
    queryset_contact = Contact.objects.all()
    queryset_skill = Skill.objects.all()
    queryset_history = History.objects.all()
    queryset_course = Course.objects.all()
    queryset_portfolio = Portfolio.objects.all()

    context = { 'personals': queryset_personal,
                'contacts': queryset_contact,
                'skills': queryset_skill,
                'historys': queryset_history,
                'courses': queryset_course,
                'portfolios': queryset_portfolio,
            }
    
    return render(request, 'home.html', context)
