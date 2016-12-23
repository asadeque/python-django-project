from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignupForm
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.translation import gettext
from users.models import *
from learnModule.models import *
from library.models import *
import datetime
import learnModule.views
from passlib.hash import pbkdf2_sha256
from django.contrib import messages


def index(request):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    context = {'langContent': langContent, }
    if "user_id" in request.session:
        return render(request, 'learnModule/index.html', context)
    else:
        return render(request, 'users/index.html', context)


def signup(request):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    context = {'langContent': langContent, }
    if "user_id" in request.session:
        return render(request, 'users/profileDetail.html', context)
    else:
        return render(request, 'users/signup.html', context)


def edit_profile(request):
    user = User.objects.get(id=request.session['user_id'])
    upword = User.objects.filter(id=request.session['user_id']).values('password')
    uform = EditUserForm(request.POST or None, request.FILES or None, instance = user)
    if request.method == 'POST' and request.POST['submit'] == 'SUBMIT':
        if uform.is_valid():
            editform = uform.save(commit=False)
            if request.POST.get('password') == '':
                password = upword[0]['password']
            else:
                pword = request.POST.get('password')
                password = pbkdf2_sha256.encrypt(pword, rounds=12000, salt_size=32)
            editform.password = password
            editform.save()
            if request.GET.has_key('next'):
                    next = request.GET['next']
            return HttpResponseRedirect("/users/Profile/")


def signup_create(request):
     langList = Language.objects.all()
     langContent = langList.order_by('name')
     context = {'langContent': langContent, }

     if request.method == 'POST' and request.POST['submit'] == 'Sign me up!':
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        email = request.POST.get('email')

        user = User()
        dupEmail = User.objects.filter(Q(email = email))
        if not dupEmail:
            user.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
            user.firstName = fname
            user.email = email
            user.userType_id=1
            user.save()
            loginuser = User.objects.filter(Q(email = email)).values('id', 'email','firstName')
            if loginuser:
                request.session['user_id'] = loginuser[0]['id']
                request.session['user_fname'] = loginuser[0]['firstName']

                userLog = UserLog()
                userLog.user_id = request.session['user_id']
                userLog.logInTime = datetime.datetime.now()
                userLog.save()
                return HttpResponseRedirect("/users/Profile/")
        else:
            messages.success(request, "Email should be unique")
            #return HttpResponseRedirect(user.get_absolute_url())
            return render(request, 'users/signup.html', context)

     else:
        return render(request, 'users/index.html', context)


def profile_detail(request):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    if "user_id" in request.session:
        user = User.objects.get(id=request.session['user_id'])
        uform = EditUserForm(request.POST or None, request.FILES or None, instance = user)

        pdetail = User.objects.filter(pk=request.session['user_id'])[:1].values('id',
             'firstName', 'lastName', 'email', 'userType', 'image')
        learnedContent = Content.objects.filter(usercontent__user_id = request.session['user_id']).order_by('-createdDate')
        learnedContent = learnedContent.values('id', 'title', 'imageURL', 'description', 'style__name')
        favContent = Content.objects.filter(userfavouritecontent__user_id = request.session['user_id']).order_by('-createdDate')
        favContent = favContent.values('id', 'title', 'imageURL', 'description', 'style__name')
        favResource = Library.objects.filter(userfavouriteresource__user_id = request.session['user_id']).order_by('-createdDate').distinct()
        favResource = favResource.values('id', 'title', 'imageURL', 'description', 'LibraryType__name')
        dlResource = Library.objects.filter(userresourcedownload__user_id = request.session['user_id']).order_by('-createdDate').distinct()
        dlResource = dlResource.values('id', 'title', 'imageURL', 'description', 'LibraryType__name')
        # favCourse = Course.objects.filter(userfavouritecourse__user_id = request.session['user_id']).order_by('-createdDate')
        dataContent = Content.objects.filter(Q(Q(usercontent__user_id = request.session['user_id'])|
                                    Q(userfavouritecontent__user_id = request.session['user_id']))).distinct().order_by('-createdDate')
        dataContent = dataContent.values('id', 'title', 'imageURL', 'description', 'style__name', 'usercontent__type', 'userfavouritecontent__type')
        dataResource = Library.objects.filter(Q(Q(userfavouriteresource__user_id = request.session['user_id'])|
                                    Q(userresourcedownload__user_id = request.session['user_id']))).distinct().order_by('-createdDate')
        dataResource = dataResource.values('id', 'title', 'imageURL', 'description', 'LibraryType__name', 'userfavouriteresource__type', 'userresourcedownload__type')
        # data = dlResource | favResource
        context = {'pdetail': pdetail, 'learnedContent': learnedContent, 'dataResource': dataResource,
                'favContent': favContent, 'favResource': favResource, # 'favCourse': favCourse,
                'dlResource':dlResource, 'dataContent': dataContent, 'user': user, 'uform': uform,
                'langContent': langContent,}
        return render(request, 'users/profileDetail.html', context)
    else:
        context = {'langContent': langContent, }
        return render(request, 'users/index.html', context)


def login_user(request, next= '/'):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    message = gettext('Login User')
    if request.method == 'POST':
        if request.GET.has_key('next'):
            next = request.GET['next']
        if request.POST['submit'] == 'Sign In':
            email = request.POST['email']
            uPass = request.POST['password']
            # user = authenticate(username=uName, password=uPass)
            user = User.objects.filter(Q(email = email)).values('id', 'email','firstName', 'password')
            if user:
                if pbkdf2_sha256.verify(uPass, user[0]['password']):
                    request.session['user_id'] = user[0]['id']
                    request.session['user_fname'] = user[0]['firstName']

                    userLog = UserLog()
                    userLog.user_id = request.session['user_id']
                    userLog.logInTime = datetime.datetime.now()
                    userLog.save()

                    return HttpResponseRedirect(next)
                    # return render(request, 'users/.html', '')
                # else:
                    # message = 'Account Deactivated'
            else:
                message = 'Login Incorrect'
                context = {'message': message, 'langContent': langContent }
                return render(request, 'users/index.html', context)
        else:
            message = "Please enable cookies and try again."

    context = {'message': message, 'langContent': langContent }
    return render(request, 'users/index.html', context)

def logout_user(request):
    userLog = UserLog()
    userLog.user_id = request.session['user_id']
    userLog.logOutTime = datetime.datetime.now()
    userLog.save()
    del request.session['user_id']
    # del request.session['email']
    return HttpResponseRedirect('/')
