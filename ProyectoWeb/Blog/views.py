from django.shortcuts import render
from Blog.models import Post, Categoria

# Create your views here.

# ------------------------------ BLOG

# Renderizado de posts generales
def blog(request):
    posts = Post.objects.all()
    return render(request, "Blog/blog.html", {"posts": posts})
    

# Renderizado de categorias - pagina de posts filtrados por categoria
def categorias(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)    
    return render(request, "Blog/categorias.html", {"categoria": categoria, "posts": posts})
