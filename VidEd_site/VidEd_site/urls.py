"""
URL configuration for VidEd_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from testapp1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('reg/', reg_page),
    path('index/', index_page),
    path('reg/regcomplete/', newreg),
    path('auth/', auth_page),
    path('auth/login/', login_page),
    path('profile/logout/', logout_page),
    path('profile/', profile_page),
    path('messanger/', messanger_page),
    path('userlist/', userlist_page),
    path('Design/', Design_page),
    path('login/', login_page),
    path('Prog/', Prog_page),
    path('VidEd/', VidEd_page)
]
