"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto, name='contacto'),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    path('acerca_de/', views.acerca_de),
    #path('', views.saludo, name= 'saludo'),
    #path('despedir/', views.despedida, name= 'despedir'),



    #Urls de la aplicacion posts
    path('posts/', include('apps.posts.urls')),
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    #path('agregar/', include('apps.posts.agregar_post')),
    path('usuarios/', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
