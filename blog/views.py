from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

from .models import Post, Comment

latest_post_list = Post.objects.all()
def index(request):
	title_list = [post.title for post in latest_post_list]
	snippet_list = [post.body[:180] for post in latest_post_list]
	post_preview = zip(title_list, snippet_list, latest_post_list)
	context = {'post_preview': post_preview,}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {'post': post,}
	return render(request, 'blog/detail.html', context)
