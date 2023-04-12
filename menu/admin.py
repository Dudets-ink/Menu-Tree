from django.contrib import admin

from .models import Menu, Submenu


# Register your models here.
admin.site.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     model = Menu
#     list_display = ['name', submenus]
    
#     @admin.display(description='All related to this menu submenus')
#     def submenus(self, obj):
#         return 
    
admin.site.register(Submenu)