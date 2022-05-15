from django.contrib import admin
from .models import S_Data
from .models import T_Data
from .models import Batch

class Students(admin.ModelAdmin):
    list_display = ('u_type','f_name','u_name','e_mail','phone','dob')
class Tutors(admin.ModelAdmin):
    list_display = ('u_type','f_name','e_mail','phone','dob','qualification','expertise','languages','rate')
class Stu_Tu(admin.ModelAdmin):
    list_display = ('tutor','student')

# Register your models here.

admin.site.register(S_Data,Students)
admin.site.register(T_Data,Tutors)
admin.site.register(Batch,Stu_Tu)