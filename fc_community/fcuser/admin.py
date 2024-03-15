from django.contrib import admin
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


# 앱 등록
admin.site.register(Fcuser, FcuserAdmin)