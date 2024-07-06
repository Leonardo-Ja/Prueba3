from django.db import models

# Create your models here.

class TituloNav(models.Model):
    titulo = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo

class Navbar(models.Model):
    id_navbar = models.AutoField(db_column= "idNavbar", primary_key= True )
    enlac = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.enlac
    def __str__(self):
        return self.url