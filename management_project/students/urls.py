from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu,name='menu'),
    path('add/',views.add_students,name='add_students'),
    path('view/',views.view_students,name='view_students'),
    path('update/<int:id>',views.update_students,name='update_students'),
    path('delete/<int:id>',views.delete_students,name='delete_students'),
]