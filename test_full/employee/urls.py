from . import views
from django.urls import path

urlpatterns = [
    path("", views.department_tree_view, name='index'),
]
