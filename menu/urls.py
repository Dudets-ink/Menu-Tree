from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tree/<str:name>/', views.TreeView.as_view(), name='tree'),
]
 