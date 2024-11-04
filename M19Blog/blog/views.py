from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    posts_per_page = request.GET.get('size', 5)
    paginator = Paginator(post_list, posts_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Замените на URL, куда перенаправить после создания поста
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

