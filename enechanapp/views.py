from django.views.generic import TemplateView, CreateView
#from flask import template_rendered
#from regex import template
from django.shortcuts import render
from . import forms
from django.views.generic import FormView
from django.urls import reverse_lazy

class DeadView(TemplateView):
    template_name = 'purupuru.html'

class NormalView(TemplateView):
    template_name = 'korokoro.html'



class EnechanCreateFormView(FormView):
    template_name = "../templates/enechanform.html"
    form_class = forms.EnechanFormClass
    success_url = reverse_lazy('angry')

class AngryView(TemplateView):
    template_name = 'purun.html'

class PostView(CreateView):
    template_name = 'post_create.html'
    form_class = forms.PostFrom
    success_url = reverse_lazy('post:post_create_complete')

class PostCompleteView(TemplateView):
    template_name = 'post_create_complete.html'