from django.shortcuts import render
from .models import Post
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html',context)

def submit(request):
    return render(request, 'blog/submit.html')

def blogPost(request, slug):
    allPost = Post.objects.filter(slug=slug).first()
#   comments = BlogComment.objects.filter(post=post)
    context = {'allPost': allPost}
    return render(request, "blog/blogPost.html", context)