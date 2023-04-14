from django.views.generic import ListView
from django import db

from .models import Menu


# Create your views here.
class IndexView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(parent=None).prefetch_related('menu_set')
        
        # print(queryset)
        return queryset
        
    