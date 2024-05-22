#from django.conf.urls import path

from . import views
from django.urls import include, path



urlpatterns = [
        path('', views.index, name='index'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]