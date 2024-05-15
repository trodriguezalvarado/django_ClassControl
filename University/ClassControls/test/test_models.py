from django.test import TestCase
from ClassControls.models import Categories, Responsibles, ClassTypes, Careers, Levels, Evaluations
from django.db.models import AutoField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your tests here.

class CategoriesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Categories.objects.create(CategoryName="Test Category")
        
    def test_category_pk_type(self):
        category = Categories.objects.get(Id=1)
        field = category._meta.get_field('Id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_category_pk_name(self):
        category = Categories.objects.get(Id=1)
        field_name = category._meta.get_field('Id').name
        self.assertEqual(field_name, 'Id') 
        
    def test_category_name(self):
        category = Categories.objects.get(Id=1)
        field_label = category._meta.get_field('CategoryName').verbose_name
        self.assertEqual(field_label, 'Category Name')
        
    def test_category_max_length(self):
        category = Categories.objects.get(Id=1)
        max_length = category._meta.get_field('CategoryName').max_length
        self.assertEqual(max_length, 50)
        
    def test_category_str_name(self):
        category = Categories.objects.get(Id=1)
        expected_object_name = category.CategoryName
        self.assertEqual(expected_object_name, str(category))
        
    def test_category_absolute_url(self):
        category = Categories.objects.get(Id=1)
        self.assertEqual(category.get_absolute_url, '/ControlClass/categories/1')

class ResponsiblesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Responsibles.objects.create(ResponsibleFirstName="Test ResponsibleFirstName", ResponsibleLastName="Test ResponsibleLastName")
        
    def test_responsible_pk_type(self):
        responsible = Responsibles.objects.get(id=1)
        field = responsible._meta.get_field('id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_responsible_pk_name(self):
        responsible = Responsibles.objects.get(id=1)
        field_name = responsible._meta.get_field('id').name
        self.assertEqual(field_name, 'id') 
        
    def test_responsible_first_name(self):
        responsible = Responsibles.objects.get(id=1)
        field_label = responsible._meta.get_field('ResponsibleFirstName').verbose_name
        self.assertEqual(field_label, 'Responsible First Name')
    
    def test_responsible_last_name(self):
        responsible = Responsibles.objects.get(id=1)
        field_label = responsible._meta.get_field('ResponsibleLastName').verbose_name
        self.assertEqual(field_label, 'Responsible Last Name')        
          
    def test_responsible_first_name_max_length(self):
        responsible = Responsibles.objects.get(id=1)
        max_length = responsible._meta.get_field('ResponsibleFirstName').max_length
        self.assertEqual(max_length, 100)
        
    def test_responsible_last_name_max_length(self):
        responsible = Responsibles.objects.get(id=1)
        max_length = responsible._meta.get_field('ResponsibleLastName').max_length
        self.assertEqual(max_length, 100)
        
    def test_responsible_str_name(self):
        responsible = Responsibles.objects.get(id=1)
        expected_object_name = "%s %s" % (responsible.ResponsibleFirstName, responsible.ResponsibleLastName) 
        self.assertEqual(expected_object_name, str(responsible))
        
    def test_responsible_absolute_url(self):
        responsible = Responsibles.objects.get(id=1)
        self.assertEqual(responsible.get_absolute_url, '/ControlClass/responsibles/1')
        
class ClassTypesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ClassTypes.objects.create(ClassTypeName="Test Class Type")
        
    def test_classtype_pk_type(self):
        classtype = ClassTypes.objects.get(id=1)
        field = classtype._meta.get_field('id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_classtype_pk_name(self):
        classtype = ClassTypes.objects.get(id=1)
        field_name = classtype._meta.get_field('id').name
        self.assertEqual(field_name, 'id') 
        
    def test_classtype_name(self):
        classtype = ClassTypes.objects.get(id=1)
        field_label = classtype._meta.get_field('ClassTypeName').verbose_name
        self.assertEqual(field_label, 'Class Type')           
          
    def test_classtype_name_max_length(self):
        classtype = ClassTypes.objects.get(id=1)
        max_length = classtype._meta.get_field('ClassTypeName').max_length
        self.assertEqual(max_length, 50)      
        
    def test_classtype_str_name(self):
        classtype = ClassTypes.objects.get(id=1) 
        self.assertEqual(classtype.ClassTypeName, str(classtype))  
    
    def test_classtype_absolute_url(self):
        classtype = ClassTypes.objects.get(id=1)
        self.assertEqual(classtype.get_absolute_url, '/ControlClass/classtypes/1')
        
class CareersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Careers.objects.create(CareerName="Test Carrer Name")
        
    def test_career_pk_type(self):
        career = Careers.objects.get(id=1)
        field = career._meta.get_field('id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_career_pk_name(self):
        career = Careers.objects.get(id=1)
        field_name = career._meta.get_field('id').name
        self.assertEqual(field_name, 'id') 
        
    def test_career_name(self):
        career = Careers.objects.get(id=1)
        field_label = career._meta.get_field('CareerName').verbose_name
        self.assertEqual(field_label, 'Career Name')           
          
    def test_career_name_max_length(self):
        career = Careers.objects.get(id=1)
        max_length = career._meta.get_field('CareerName').max_length
        self.assertEqual(max_length, 100)      
        
    def test_career_str_name(self):
        career = Careers.objects.get(id=1) 
        self.assertEqual(career.CareerName, str(career))  
    
    def test_career_absolute_url(self):
        career = Careers.objects.get(id=1)
        self.assertEqual(career.get_absolute_url, '/ControlClass/careers/1')
        
class LevelsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Levels.objects.create(LevelName="Test Level Name")
        
    def test_level_pk_type(self):
        level = Levels.objects.get(id=1)
        field = level._meta.get_field('id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_level_pk_name(self):
        level = Levels.objects.get(id=1)
        field_name = level._meta.get_field('id').name
        self.assertEqual(field_name, 'id') 
        
    def test_level_name(self):
        level = Levels.objects.get(id=1)
        field_label = level._meta.get_field('LevelName').verbose_name
        self.assertEqual(field_label, 'Level Name')           
          
    def test_level_name_max_length(self):
        level = Levels.objects.get(id=1)
        max_length = level._meta.get_field('LevelName').max_length
        self.assertEqual(max_length, 50)      
        
    def test_level_str_name(self):
        level = Levels.objects.get(id=1) 
        self.assertEqual(level.LevelName, str(level))  
    
    def test_level_absolute_url(self):
        level = Levels.objects.get(id=1)
        self.assertEqual(level.get_absolute_url, '/ControlClass/levels/1')
        
class EvaluationsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Evaluations.objects.create(Evaluation=3)
        
    def test_evaluation_pk_type(self):
        evaluation = Evaluations.objects.get(id=1)
        field = evaluation._meta.get_field('id')
        self.assertTrue(isinstance(field, AutoField))
        
    def test_evaluation_pk_name(self):
        evaluation = Evaluations.objects.get(id=1)
        field_name = evaluation._meta.get_field('id').name
        self.assertEqual(field_name, 'id') 
        
    def test_evaluation_name(self):
        evaluation = Evaluations.objects.get(id=1)
        field_label = evaluation._meta.get_field('Evaluation').verbose_name
        self.assertEqual(field_label, 'Evaluation')           
          
    def test_evaluation_name_min_value(self):
        evaluation = Evaluations.objects.get(id=1)
        evaluation.Evaluation = 1
        evaluation.save()           
        
    def test_evaluation_name_max_value(self):
        evaluation = Evaluations.objects.get(id=1)
        evaluation.Evaluation = 6
        evaluation.save()  
    
    def test_evaluation_absolute_url(self):
        evaluation = Evaluations.objects.get(id=1)
        self.assertEqual(evaluation.get_absolute_url, '/ControlClass/evaluations/1')