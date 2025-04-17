
from django.contrib import admin
from django.urls import path
from core.views import whatsapp_webhook, home

urlpatterns = [
    path('', home, name='home'),  # Adicionando a URL raiz
    path('admin/', admin.site.urls),
    path('webhook/', whatsapp_webhook, name='whatsapp_webhook'),
]
