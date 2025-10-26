from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Noticia

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'area', 'is_staff', 'admitido')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nombre', 'apellido', 'area', 'admitido')}),
    )

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
