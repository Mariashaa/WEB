"""
Definition of urls for labaaaa44.
"""

from datetime import datetime
from os import name
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('videopost', views.videopost, name='videopost'),
    re_path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('directions/', views.about, name= 'directions'),
    path('links/', views.links, name='links'),
    path('anketa/',views.anketa, name= 'anketa'),
    path('newpost', views.newpost, name='newpost'),
    path('user/registration/', views.registration, name='registration'),
    # path('^registration/', views.registration, name='registration'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
