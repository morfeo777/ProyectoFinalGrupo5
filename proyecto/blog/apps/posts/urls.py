from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_post, name= 'home_posts'),
    path('categorias_ver', views.categorias_vistas, name= 'categorias_ver'),
    path('posteos', views.post_realizado, name= 'post_realizado'),
    path('post_detail/<int:post_id>', views.post_detail, name= 'post_detail'),
    #Comentarios
    path('comentario', views.comentar_posteo, name= 'comentar'),
    path('Borrar/<int:pk>', views.Borrar_Comentario.as_view(), name= 'borrar_comentario'),
    path('Modificar/<int:pk>', views.Modificar_Comentario.as_view(), name= 'modificar_comentario'),
    #url para crear posts
    path('cargar/', views.Cargar_Post.as_view(), name= 'cargar_post'),
    #urls para contacto
    path('cargar_contactos/', views.Cargar_Contacto.as_view(), name = 'cargar_contacto'),


    #Agregar Post
    path('agregar_post', views.agregar_post, name= 'agregar_post'),
    path('agregar_post_formulario', views.agregar_post_form, name= 'agregar_post_formulario'),



    
]