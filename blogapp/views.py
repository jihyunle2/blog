from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .models import Blog
from django.utils import timezone
from .forms import BlogPost

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'detail':details})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title = request.POST['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.POST['body']
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    delete_blog=get_object_or_404(Blog,pk=blog_id)
    delete_blog.delete()
    return redirect('home')

def update(request, blog_id):
    update_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'update.html', {'update_blog':update_blog})

def edit(request, blog_id):
    edit_blog=Blog.objects.get(pk=blog_id)
    edit_blog.title=request.POST['title']
    edit_blog.pub_date=timezone.datetime.now()
    edit_blog.body=request.POST['body']
    edit_blog.save()
    return redirect('/blog/'+str(edit_blog.id))

def blogpost(request):
    if request.method=="POST":
        form = BlogPost(request.POST)
        if form.is_vaild():
            post = form.save(commit=False) #commit=false는 완성된게 아니라는 뜻, pub_date도 넣어야하니까.
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form=BlogPost()
        return render(request, 'new.html',{'form':form})


