"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from test2.views import *
from django.urls.conf import re_path
from books import views
from books import models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('time/', current_datetime,{'temp_name':'current_date.html'}),
    re_path(r'time/plus/(\d{1,2})/$', hours_ahead),
    path('search/',views.search,{'temp_name1':'search_form.html','temp_name2':'search_results.html'}),
    path('about/',views.PublisherList.as_view(),name='publisher'),

]
