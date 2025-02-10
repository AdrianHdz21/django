from config.wsgi import *
from core.erp.models import Type

#query = Type.objects.all()
#print(query)

#Insercion
#t = Type(name = 'Prueba').save()

#Update
#t = Type.objects.get(id = 1)
#t.name = "President"
#t.save()

#Delete
#t = Type.objects.get(pk=5)
#t.delete()

#listado
#obj = Type.objects.filter(name__icontains='pre') #Sin importar si hay mayus o min
#obj = Type.objects.filter(name__startswith='P') #Empiecen con
#obj = Type.objects.filter(name__endwith='P') #Terminen con
#print(obj)