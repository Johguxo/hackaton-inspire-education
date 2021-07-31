from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render
# Create your views here.
#class LandingPage(TemplateView):
#    template_name = 'personal_information/landing-page.html'
#    return render(request,"landing-page.html")

class LandingPage(TemplateView):
    template_name = 'personal_information/landing-page.html'
    #return render(request,template_name)