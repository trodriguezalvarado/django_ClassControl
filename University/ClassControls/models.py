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
    
class Evaluations(models.Model):
    
    Evaluation= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Evaluation', help_text='Add an evaluation')
    
    def get_absolute_url(self):
        return reverse('evaluations', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.Evaluation)