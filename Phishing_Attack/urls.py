"""Phishing_Attack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from Phishing_Attack import settings
from user import views as user_views
from admins import views as admin_views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$',user_views.index,name="index"),
    url('user/register',user_views.register,name="register"),
    url('userpage',user_views.userpage,name="userpage"),
    url('mydetails',user_views.mydetails,name="mydetails"),


    url('admins',admin_views.admins,name="admins"),
    url('admin_page',admin_views.admin_page,name="admin_page"),
    url('user_details',admin_views.user_details,name="user_details"),
    url('attack_details',admin_views.attack_details,name="attack_details"),
    url('chart_page',admin_views.chart_page,name="chart_page"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
