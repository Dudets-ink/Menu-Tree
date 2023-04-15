from django.views.generic import ListView
from django.db.models import Q, Count

from .models import Menu
from .utils import build_parent


# Create your views here.
class IndexView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(parent=None) \
            .prefetch_related('menu_set')
        return queryset
    
    
class TreeView(ListView):
    model = Menu
    template_name = 'menu/tree.html'
    
    def get_queryset(self):
        MAX_LEVEL = 30
        queryset = self.model.objects \
            .filter(Q(name=self.kwargs['name']) | Q(parent=None)) \
            .exclude(menu__name=self.kwargs['name']) \
            .prefetch_related('menu_set') \
            .select_related(*build_parent(MAX_LEVEL))
        
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.kwargs['name']
        return context
    
        
    