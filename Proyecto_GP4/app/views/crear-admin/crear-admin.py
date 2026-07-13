from django.contrib.auth.models import User
from django.http import HttpResponse

def crear_admin(request):
    if User.objects.filter(username="admin").exists():
        return HttpResponse("El usuario admin ya existe")

    User.objects.create_superuser(
        username="admin",
        email="admin@admin.com",
        password="Admin12345"
    )

    return HttpResponse("Administrador creado correctamente")