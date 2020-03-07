"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from login import views as lv
from reservation import views as rv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', lv.index),
    url(r'^login/', lv.login),
    url(r'^register/', lv.register),
    url(r'^logout/', lv.logout),
    url(r'^profile/', lv.profile),
    url(r'^deleteuser/', lv.deleteuser),
    url(r'^booktable/', rv.booktable),
    url(r'^booksuccess/', rv.booksuccess),
    url(r'^checkrev/', rv.checkrev),
]