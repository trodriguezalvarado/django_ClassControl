from django.contrib import admin
from .models import Categories, Responsibles, ClassTypes, Careers, Levels, Planning_control_classes

# Register your models here.
admin.site.register(Categories)
admin.site.register(Responsibles)
admin.site.register(Careers)
admin.site.register(Levels)
admin.site.register(Planning_control_classes)