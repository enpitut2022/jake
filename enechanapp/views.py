from django.views.generic import TemplateView
#from flask import template_rendered
#from regex import template

class DeadView(TemplateView):
    template_name = 'purupuru.html'

class NormalView(TemplateView):
    template_name = 'korokoro.html'
