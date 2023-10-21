from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import BlogPost, Comment, Topic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.forms import BlogPostForm
# Create your views here.


def home(request):
    topics = Topic.objects.all()
    blogPosts = BlogPost.objects.all()
    context = {'topics': topics, 'blogposts': blogPosts}
    return render(request, 'blog/home.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    # blogs = user.blog_set.all()
    # blog_comments = user.comments_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'topics': topics}
    return render(request, 'blog/profile.html', context)


def blog(request, pk):

    blog = BlogPost.objects.get(id=pk)
    room_messages = blog.message_set.all()
    participants = blog.participants.all()

    if request.method == 'POST':
        message = Comment.objects.create(
            user=request.user,
            blog=blog,
            body=request.POST.get('body')
        )
        blog.participants.add(request.user)

        return redirect('room', pk=blog.id)

    context = {'room': blog, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'base/room.html', context)


@login_required(login_url='/login')
def createBlog(request):
    # form = RoomForm(request.POST)
    topics = Topic.objects.all()
    form = BlogPostForm()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        BlogPost.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
    # if request.method == 'POST':
    #     form = RoomForm(request.POST)
    #     if form.is_valid:
    #         room = form.save(commit=False)
    #         room.host= request.user
    #         form.save()
        return redirect('/')

    context = {'topics': topics, 'form': form}
    return render(request, 'blog/blog_create.html', context)
