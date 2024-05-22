#from django.conf.urls import path

from . import views
from django.urls import include, path



urlpatterns = [
        path('', views.index, name='index'),
        path('planning/', views.planniglistView.as_view(), name='planninglist'),
        path('planning/<int:pk>', views.PlanningDetailView.as_view(), name='planningdetail'),
        path('planning/add', views.PlanningAddView.as_view(), name='planningadd'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]