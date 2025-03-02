from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre',unique=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type,on_delete=models.CASCADE,verbose_name='Tipo')
    names = models.CharField(max_length=150,verbose_name='Nombres')
    dni = models.CharField(max_length=10,unique=True,verbose_name='DNI')
    date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_creation = models.DateField(auto_now=True,verbose_name='Fecha de creacion')
    date_update = models.DateField(auto_now_add=True,verbose_name='Fecha de actualizacion')
    age = models.PositiveIntegerField(default=0,verbose_name='Age')
    salary = models.DecimalField(default=0.00,decimal_places=2,max_digits=9,verbose_name='Salario')
    state = models.BooleanField(default=True,verbose_name='Estado')
    gender = models.CharField(max_length=50, verbose_name='Gender')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',verbose_name='Imagen de la empresa',null=True,blank=True)
    cv = models.ImageField(upload_to='cv/%Y/%m/%d',verbose_name='CV',null=True,blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']

