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
from waitlist import views as wv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', lv.index, name='index'),
    url(r'^login/', lv.login, name='login'),
    url(r'^register/', lv.register, name='register'),
    url(r'^chpasswd/', lv.chpasswd, name='chpasswd'),
    url(r'^chpasswdsuccess/', lv.chpasswdsuccess, name='chpasswdsuccess'),
    url(r'^logout/', lv.logout, name='logout'),
    url(r'^profile/', lv.profile, name='profile'),
    url(r'^deleteuser/', lv.deleteuser, name='deleteuser'),
    url(r'^booktable/', rv.booktable, name='booktable'),
    url(r'^booksuccess/', rv.booksuccess, name='booksuccess'),
    url(r'^checkrev/', rv.checkrev, name='checkrev'),
    url(r'^nofunction/', lv.notfound, name='notfound'),
    url(r'^takeno/', wv.takeno, name='takeno'),
    url(r'^takesuccess/', wv.takesuccess, name='takesuccess'),
    url(r'^checkstate/', wv.checkstate, name='checkstate'),
    url(r'^managewl/', lv.managewl, name='managewl'),
    url(r'^managersv/', lv.managersv, name='managersv'),
    url(r'^managetb/', lv.managetb, name='managetb'),
    url(r'^pop_waitlist/', lv.pop_waitlist, name='pop_waitlist'),
    url(r'^change_table/', lv.change_table, name='change_table'),
    url(r'^menu/', lv.menu, name='menu'),
]

