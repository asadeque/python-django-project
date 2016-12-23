from django.shortcuts import render
from .models import *
from learnModule.models import *
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def story_list(request):
    if "language" not in request.session:
        request.session['language'] = '2'
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    Data = Story.objects.all().filter(language=request.session['language'])
    DataGood = Story.objects.all().filter(language=request.session['language'], storyType='3')
    DataBad = Story.objects.all().filter(language=request.session['language'], storyType='2')
    DataUgly = Story.objects.all().filter(language=request.session['language'], storyType='1')
    context = {'Data' : Data, 'DataGood' : DataGood, 'DataBad' : DataBad, 'DataUgly': DataUgly,'langContent': langContent, }
    return render(request, 'story/story_list.html', context)


def story_detail(request, pk):
    if "language" not in request.session:
        request.session['language'] = '2'
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    Data = Story.objects.all().filter(language=request.session['language'], id=pk)
    instance = get_object_or_404(Story, id=pk)
    context = {'Data' : Data, 'instance': instance,'langContent': langContent, }
    return render(request, 'story/story_detail.html', context)
