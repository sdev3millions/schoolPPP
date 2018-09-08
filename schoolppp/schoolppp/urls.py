"""schoolppp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('schooldata/show', views.schooldata_list, name='school_list'),
    path('schooldata/edit/<int:id>', views.schooldata_edit, name='s'),
    path('test/', views.test),
    path(
        'schooldata/delete/<int:id>',
        views.schooldata_delete,
        name='school_delete'),
    path(
        'schooldata/update/<int:id>',
        views.schooldata_update,
        name='school_update'),
    path('school/add', views.school_add),
    path('school/', views.add_show),
]