from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()   # Traemos todos los Posts
        context={
            'posts':posts  
        }
        return render(request, 'blog_list.html', context)   # Retorna el request, en el html solicitado, con el context


class BlogCreateViews(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()   # Traigo el PostCreateForm dentro de esta variable para poder agregarlo al context
        context = {
            'form':form   # Una vez agregado al context me aparecera en la vista en linea
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":   # Hace referencia al <form> de blog_create con method="POST"
            form = PostCreateForm(request.POST)   # 1ro traemos el PostCreateForm y le pasamos la inf dentro de POST
            if form.is_valid():   # Si el form es valido...
                title = form.cleaned_data.get('title')   # Obtengo los datos que ingresaron en 'title'
                content = form.cleaned_data.get('content')   # Obtengo los datos que ingresaron en 'content'

                p, created = Post.objects.get_or_create(title=title, content=content)   # p, viene de post. Con la info del form, crearemos un Post.   El title y content en rojo vienen del model Post, y los otros de esta funcion
                p.save()
                return redirect('blog:home')   # Redirijo al home

        context={
            
        }
        return render(request, 'blog_create.html', context)


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):   # Agrego el pk
        post = get_object_or_404(Post, pk=pk)   # Llamo un post especifico
        context={
            'post':post
        }
        return render(request, 'blog_detail.html', context)


class BlogUpdateView(UpdateView):
    model=Post
    fields=['title', 'content']
    template_name='blog_update.html'

    # Vuelvo a blog_detail ya actualizado
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})


class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url= reverse_lazy('blog:home')



