"""GiftOfSocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from form.views import user_form, admin_form, user, admin_shell, admin_user_results
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_form/$',user_form, name='user_form'),
    url(r'^admin_form/$',admin_form, name='admin_form'),
    url(r'^user/$',user, name='user'),
    url(r'^admin_shell/$',admin_shell, name='admin_shell'),
    url(r'^admin_user_results/$',admin_user_results, name='admin_user_results')
]
