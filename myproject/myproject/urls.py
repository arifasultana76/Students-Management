from django.contrib import admin
from django.urls import path
from myapp.views import studentlist,students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlist/', studentlist,name='studentlist'),
    path('students/', students,name='students')
    
]
