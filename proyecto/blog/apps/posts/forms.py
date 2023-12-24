from django import forms
from .models import Comentario, Post, Contacto

class Formulario_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)

class Fom_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "cuerpo", "imagen", "categoria_post")

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]

class Form_Contacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ("nombre", "correo", "tipo_consulta", "mensaje", "avisos",)