from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Categorias, Comentario, Contacto
from django.views.generic import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import Formulario_Modificacion, Fom_Post, ContactoForm, Form_Contacto
from django.http import Http404, HttpResponse

# Create your views here.
def home_post(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')

def agregar_post_form(request):
    categorias = Categorias.objects.all()
    print(categorias)
    #ctx = {'categorias_traidas': categorias}
    return render(request, 'posts/agregar_post.html', {'categorias_traidas': categorias})

def post_realizado(request):
    #posteos = Post.objects.all() # select * from post
    #categorias = Categorias.objects.all()
    #print(categorias)
    #print(posteos)    
    id_categoria = request.GET.get('id', None)
    antiguedad = request.GET.get('orden', None)
    alfabetico = request.GET.get('orden', None)
    ctx = {}
    if id_categoria:
        posteos = Post.objects.filter(categoria_post = id_categoria)
    else:
        if antiguedad == "asc":
            posteos = Post.objects.all().order_by("fecha_creacion")
        elif alfabetico == "a":
            posteos = Post.objects.all().order_by("titulo")
        elif alfabetico == "z":
            posteos = Post.objects.all().order_by("-titulo")
        else:
            posteos = Post.objects.all().order_by("-fecha_creacion")
        # posteos = Post.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(posteos, 5)
        posteos = paginator.page(page)
    except EmptyPage:    
        raise Http404
        
    categorias = Categorias.objects.all()    
    ctx["posteos"] = posteos
    ctx["categorias"] = categorias
    ctx["paginator"] = paginator
    #print(ctx)
    return render(request, 'posts/post.html', {'ctx': ctx, 'posteos': posteos, 'categorias': categorias})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {'post': post}
    return render(request, 'posts/post_detail.html', ctx)

def categorias_post(request):
    return render(request, 'posts/categorias.html')

def categorias_vistas(request):
    categorias = Categorias.objects.all()
    print(categorias)
    ctx = {'categorias_traidas': categorias}
    return render(request, 'posts/agregar_post.html', ctx )

def comentar_posteo(request):
    comentario = request.POST.get("comentario", None)
    usuario = request.user
    post = request.POST.get("id_post", None)
    #post = request.POST.get("id", None)
    posteo = Post.objects.get(id=post)
    setear_comentario = Comentario.objects.create(
        usuario = usuario,
        post =  posteo,
        texto = comentario

    )
    return redirect("posts:post_detail", post_id = post)


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'posts/contacto.html', data)




class Borrar_Comentario(DeleteView):
    model = Comentario
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("posts:post_realizado")

class Modificar_Comentario(UpdateView):
    model = Comentario
    form_class = Formulario_Modificacion
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("posts:post_realizado")

class Cargar_Post(CreateView):
    model = Post
    template_name = "posts/cargar_post.html"
    form_class = Fom_Post
    success_url = reverse_lazy("posts:post_realizado")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.usuario = self.request.user
        return super(Cargar_Post, self).form_valid(form)
    

class Cargar_Contacto(CreateView):
    model = Contacto
    template_name = "posts/cargar_contacto.html"
    form_class = Form_Contacto
    success_url = reverse_lazy("posts:post_realizado")

    def form_valid(self, form):
        contacto = form.save(commit=False)
        contacto.usuario = self.request.user
        return super(Cargar_Contacto, self).form_valid(form)

    



#Agregar Post
def agregar_post(request):
    categorias = Categorias.objects.all()
    print(categorias)
    #post_nuevo = request.POST.get("agregar_post_nuevo", None)
    #post_titulo = request.POST.get("post_titulo", None)
    #post_cuerpo = request.POST.get("post_cuerpo", None)
    #post_categoria = request.POST.get("post_categoria", None)
    #usuario = request.user
    #post = request.POST.get("id_post", None)
    #post = request.POST.get("id", None)
    #posteo_nuevo = Post.objects.get(id=post)
    #setear_post_nuevo = Post.objects.create(
    #    titulo = post_titulo,
    #    cuerpo = post_cuerpo,        
    #    imagen = post_cuerpo,
    #    categoria_post = post_categoria
    #    #usuario = usuario,
    #    #post =  posteo_nuevo,
        #texto = posteo_nuevo

    #)
    return render(request, "posts:agregar_post.html", {'categorias': categorias})   


