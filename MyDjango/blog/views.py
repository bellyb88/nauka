from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import *
from .forms import *

# Create your views here.



def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status = 'published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = 'blblablalbal'
            message = 'afjdgfnsdlknfsdklnf'
            send_mail(subject, message, 'bozenabrzuszek@gmail.com', [cd['to']])
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post, 'form':form})

class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    context_object_name = 'posts'
    template_name='blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status= 'published', publish__year=year, publish__month= month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})