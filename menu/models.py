from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    
    def __str__(self):
        return f'Menu {self.name}'
    

class Submenu(models.Model):
    text = models.TextField(max_length=255 ,blank=False)
    number = models.IntegerField(default=1) 
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Article of {self.menu.name} {self.number}'