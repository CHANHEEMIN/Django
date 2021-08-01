from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display=('name','birthday')
admin.site.register(Board,BoardAdmin)
    
