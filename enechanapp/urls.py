from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'enechanapp'
urlpatterns = [
    #path('index/', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),
]