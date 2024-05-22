from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from .decorators import group_required
from .models import Planning_control_classes

# Create your views here.

@login_required
def index(request):
    return render(request, 'home/index.html')

# Planning Views
@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('responsibles',), name='dispatch')
class planniglistView(generic.ListView):
    model = Planning_control_classes
    template_name = "planning/planninglist.html"
    context_object_name = 'planning_list'


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('responsibles',), name='dispatch')    
class PlanningDetailView(generic.DetailView):
    model = Planning_control_classes
    template_name = "planning/planningDetail.html"
    context_object_name = 'planning_Data'

# Planning Views end
