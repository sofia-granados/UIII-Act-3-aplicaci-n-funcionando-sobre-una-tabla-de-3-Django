from django.contrib import admin
from .models import Animal, Cliente, Empleado

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id_animales', 'nombre', 'especie', 'edad', 'dueno', 'imagen_preview']
    readonly_fields = ['imagen_preview']
    list_filter = ['especie', 'dueno']
    search_fields = ['nombre', 'especie']
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Sin imagen"
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Vista Previa'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'apepaterno', 'correo', 'telefono']
    search_fields = ['nombre', 'apepaterno', 'correo']

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id_empleado', 'nombre', 'apepaterno', 'ocupacion', 'telefono']
    search_fields = ['nombre', 'apepaterno', 'ocupacion']

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)