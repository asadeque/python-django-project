from urllib import quote_plus
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Blog, Comment, UserFavouriteBlog
from users.models import User
from .forms import BlogForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, Avg, Count
from django.db.models import Q
from learnModule.models import *


# Create your views here.

def blog_list(request):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    #if "user_id" in request.session:
    queryset_list = Blog.objects.all() #.order_by("-createdDate")
    comments = Comment.objects.all().values('blog').annotate(score = Count('blog')).order_by('-score')
    '''
    paginator = Paginator(queryset_list, 4) # Show 10 contacts per page

    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    '''
    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    try:
        LibraryDatas = paginator.page(page)
    except PageNotAnInteger:
        LibraryDatas = paginator.page(1)
    except EmptyPage:
        LibraryDatas = paginator.page(paginator.num_pages)

    if "user_id" in request.session:
        CFB1 = UserFavouriteBlog.objects.filter(Q(user_id=request.session['user_id'])).values_list('blog_id', flat=True)
        CFB2 = list(CFB1)
        CFB = map(int, CFB2)
    else:
        CFB = []

    context = { "blog_list": LibraryDatas, "title": "Blog & News", "LibraryDatas": LibraryDatas, 'comments': comments,
                'CFB': CFB, 'langContent': langContent, }
    return render(request, "blog/blog_list.html", context)
    #else:
        #context = { "title": "Not logged in" }
        #return render(request, "blog/blog_list.html", context)

def blog_create(request):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    if not "user_id" in request.session:
        raise Http404
    f = User.objects.get(pk=request.session['user_id'])
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = f
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    #else:
        #messages.error(request, "Not Successfully Created")
        #return HttpResponseRedirect(instance.get_absolute_url())
    '''
    if request.method == 'POST':
        print request.POST.get("title")
        print request.POST.get("content")
        Blog.objects.create(title=request.POST.get("title"), content=request.POST.get("content"))
    '''
    context = { "form": form, 'langContent': langContent,  }
    return render(request, "blog/blog_form.html", context)

def blog_detail(request, id=None): # Retrieve
    # instance = Blog.objects.get(id=id)
    langList = Language.objects.all()
    langContent = langList.order_by('name')

    instance = get_object_or_404(Blog, id=id)
    form = CommentForm(request.POST or None)
    #if request.POST['submit'] == 'Submit':
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = instance
        comment.save()
        form = CommentForm()
        messages.success(request, "Comments successfully saved.")
        return HttpResponseRedirect(instance.get_absolute_url())
    blog_list = Blog.objects.exclude(id=id).order_by('-createdDate')[:4]
    comments = Comment.objects.all().values('blog').annotate(score = Count('blog')).order_by('-score')
    share_string = quote_plus(instance.content)
    context = { "title": "Blog & News", "instance": instance, "share_string": share_string,
        'form': form, 'blog_list': blog_list, 'comments': comments, 'langContent': langContent,  }
    return render(request, "blog/blog_detail.html", context)

def blog_update(request, id=None):
    langList = Language.objects.all()
    langContent = langList.order_by('name')

    if not "user_id" in request.session:
        raise Http404
    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = { "title": instance.title, "instance": instance, "form": form, 'langContent': langContent, }
    return render(request, "blog/blog_form.html", context)


def blog_delete(request, id=None):
    if not "user_id" in request.session:
        raise Http404
    instance = get_object_or_404(Blog, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("blog:list")


def favourite_blog_user(request, pk):
    chkFavouriteBlog = UserFavouriteBlog.objects.filter(Q(user_id = request.session['user_id']), Q(blog_id = pk))
    if not chkFavouriteBlog:
        userFavouriteBlog = UserFavouriteBlog()
        userFavouriteBlog.user_id = request.session['user_id']
        userFavouriteBlog.blog_id = pk
        userFavouriteBlog.save()
    return HttpResponse('Favourite')


def delete_favourite_blog_user(request, pk):
    chkFavouriteBlog = UserFavouriteBlog.objects.filter(Q(user_id = request.session['user_id']), Q(blog_id = pk))
    if chkFavouriteBlog:
        userFavouriteBlog = UserFavouriteBlog.objects.get(Q(user_id = request.session['user_id']), Q(blog_id = pk))
        userFavouriteBlog.delete()
    return HttpResponse('DelFavourite')



