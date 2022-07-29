from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'enechanapp'
urlpatterns = [
    #path('index/', views.IndexView.as_view(), name='index'),
    path('', views.NormalView.as_view(), name='normal'),
    path('dead/', views.DeadView.as_view(), name='dead'),
    path('enechanform/', views.EnechanCreateFormView.as_view(),name="enechanform"),
    path('enechanform/angry',views.AngryView.as_view(), name='angry'),
    path('post/', views.PostView.as_view(), name='post_create'),
    path('post/complete/', views.PostCompleteView.as_view(), name="post_create_comlete"),
]
