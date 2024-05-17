from random import choices
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Categories(models.Model):
    Id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50, verbose_name="Category Name", help_text="Add a name for the category")
    
    def get_absolute_url(self):
        return reverse('categories', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.CategoryName)
class Responsibles(models.Model):
    ResponsibleFirstName = models.CharField(max_length=100, verbose_name="Responsible First Name", help_text="Add a first name for the responsible")
    ResponsibleLastName = models.CharField(max_length=100, verbose_name="Responsible Last Name", help_text="Add a last name for the responsible")
    def get_absolute_url(self):
        return reverse('responsibles', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.ResponsibleFirstName, self.ResponsibleLastName)
    
class ClassTypes(models.Model):
    
    ClassTypeName= models.CharField(max_length=50, verbose_name='Class Type', help_text='Add a class type name')
    
    def get_absolute_url(self):
        return reverse('classtypes', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.ClassTypeName)
    
class Careers(models.Model):
    
    CareerName= models.CharField(max_length=100, verbose_name='Career Name', help_text='Add a career name')
    
    def get_absolute_url(self):
        return reverse('careers', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.CareerName)
    
class Levels(models.Model):
    
    LevelName= models.CharField(max_length=50, verbose_name='Level Name', help_text='Add a level name')
    
    def get_absolute_url(self):
        return reverse('levels', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.LevelName)


    
class Planning_control_classes(models.Model):
    
    Category = models.ForeignKey("Categories", verbose_name="Category", help_text="Select a category", on_delete=models.CASCADE, blank=False, null=False)
    
    Responsible = models.ForeignKey("Responsibles", verbose_name="Responsible", help_text="Select a responsible", on_delete=models.CASCADE, blank=False, null=False)
    
    
    ClassType = models.ForeignKey("ClassTypes", verbose_name="Class Type", help_text="Select a class type", on_delete=models.CASCADE, blank=False, null=False)
    
    Career = models.ForeignKey("Careers", verbose_name="Career", help_text="Select a career", on_delete=models.CASCADE, blank=False, null=False)
    
    Level = models.ForeignKey("Levels", verbose_name="Level", help_text="Select a level", on_delete=models.CASCADE, blank=False, null=False)
    
    ClassRoom = models.CharField(max_length=100, verbose_name="Classroom", help_text="Typoe a classroom", blank= False, null=False)
    
    Evaluation = models.IntegerField(verbose_name="Evaluation", help_text="choose an evaluation", null= True, choices=[(2,'2'), (3,'3'), (4,'4'), (5,'5')])
    
    RealizationDate = models.DateField(verbose_name="Realization Date", help_text="Select a date of realization", null=True)
    
    Observations= models.TextField(verbose_name="Observations", help_text="Type any observation here")
    
    def get_absolute_url(self):
        return reverse('planningClassControl', args=[str(self.id)])

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.Responsible, self.Category,self.ClassType, self.Career, self.Level, self.ClassRoom)
  
