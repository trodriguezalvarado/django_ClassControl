#from django.conf.urls import path

from . import views
from django.urls import include, path



urlpatterns = [
        path('', views.index, name='index'),
        path('planning/', views.planniglistView.as_view(), name='planninglist'),
        path('planning/<int:pk>', views.PlanningDetailView.as_view(), name='planningdetail'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]