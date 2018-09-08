from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('schooldata/show', views.schooldata_list, name='school_list'),
    path('schooldata/edit/<int:id>', views.schooldata_edit, name='s'),
    path('test/', views.test),
    path('schooldata/delete/<int:id>',
        views.schooldata_delete,
        name='school_delete'),
    path('schooldata/update/<int:id>',
        views.schooldata_update,
        name='school_update'),
    path('school/add', views.school_add),
    path('school/', views.add_show),
    
]