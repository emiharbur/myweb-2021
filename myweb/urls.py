"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myfapp import views as myfapp_views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myfapp_views.index),
    path('newshandle/',myfapp_views.newshandle),
    path('newshandle/save/',myfapp_views.save),
    path('newshandletest/',myfapp_views.newshandletest),
    path('newshandletest/savetest/',myfapp_views.savetest),
    path('newssearch/',myfapp_views.newssearch),
    path('postnews/', myfapp_views.postnews),
    #path('',include('myfapp.urls'))
]
urlpatterns += staticfiles_urlpatterns()



