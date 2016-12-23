from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from .models import *
from django.db.models import Q
from string import ascii_lowercase
from users.models import *
from learnModule.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os, re, math
from django.db.models import Sum, Avg, Count, Max
# Create your views here.


def language(request, value , next= '/'):
        request.session['language'] = value
        if request.GET.has_key('next'):
            next = request.GET['next']
        return HttpResponseRedirect(next)


def libraryDetails(request, pk):
    langList = Language.objects.all()
    langContent = langList.order_by('name')
    if "language" not in request.session:
        request.session['language'] = '2'

    complexityData = Complexity.objects.filter().values('level')[0]['level']
    contentData = Library.objects.get(pk=pk)
    contentKeywords = Library.objects.filter(pk=pk).values('keywords')[0]['keywords']

    if contentKeywords != '':
        keywordForSearch = contentKeywords.split(';')
        keywordForSearch = map(str, keywordForSearch)
        id_list = Library.objects.filter(Q
            (Q(reduce(lambda x, y: x | y, [Q(title__icontains=word) for word in keywordForSearch]))
                |Q(reduce(lambda x, y: x | y, [Q(keywords__icontains=word) for word in keywordForSearch]))
                |Q(reduce(lambda x, y: x | y, [Q(topic__title__icontains=word) for word in keywordForSearch]))
                |Q(reduce(lambda x, y: x | y, [Q(topic__description__icontains=word) for word in keywordForSearch]))
                |Q(reduce(lambda x, y: x | y, [Q(author__icontains=word) for word in keywordForSearch]))
        )).values_list('id',flat=True)
        id_list = list(id_list)
        id_list = map(int, id_list)
    else:
        id_list = []

    LibraryData = Library.objects.filter(Q(Q(language=request.session['language']), ~Q(id=pk), Q(id__in=id_list)))[:40]

    if "user_id" in request.session:
        CFR = UserFavouriteResource.objects.filter(Q(user_id=request.session['user_id']), Q(library_id=pk)).values_list('library_id', flat=True)
        CFR = list(CFR)
        CFR = map(int, CFR)

        CFRALL = UserFavouriteResource.objects.filter(Q(user_id=request.session['user_id'])).values_list('library_id', flat=True)
        CFRALL = list(CFRALL)
        CFRALL = map(int, CFRALL)
        CLC = UserContent.objects.filter(Q(user_id=request.session['user_id']), Q(content_id=pk))
    else:
        CFR = []
        CFRALL = []
        CLC = []

    context = {'contentData': contentData, 'complexityData': complexityData,
               'LibraryData': LibraryData, 'CFR': CFR, 'CLC': CLC, 'CFRALL': CFRALL,
               'langContent': langContent,  }
    return render(request, 'library/libraryDetails.html', context)


def pdfDownload(request, filename, pk):
    Static_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    f = open(Static_path+'/staticfiles/library/pdf/'+filename, 'rb')
    response = HttpResponse(f.read(),content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+filename

    # Save download information to the database
    if "user_id" in request.session:
        userResourceDownload = UserResourceDownload()
        userResourceDownload.user_id = request.session['user_id']
        userResourceDownload.library_id = pk
        userResourceDownload.save()
        return response
    else:
        return response


def searchData(FieldName, arrayList):
    field_name = FieldName
    arrayList = arrayList.split(',')
    arrayList = [int(x) for x in arrayList]
    id_list = Library.objects.filter(Q(**{field_name: arrayList})).values_list('id', flat=True)
    id_list = list(id_list)
    id_list = map(int, id_list)
    return id_list


def library(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    if request.method == 'POST' and request.POST.get('SearchinLibrary') == '' and request.POST.get('SearchFilter') == 'Search':
        if 'writtenBy__in' in request.session:
            del request.session['writtenBy__in']
        if 'libraryType__in' in request.session:
            del request.session['libraryType__in']
        if 'writtenFor__in' in request.session:
            del request.session['writtenFor__in']
        if 'topic__in' in request.session:
            del request.session['topic__in']
        if 'complexity__in' in request.session:
            del request.session['complexity__in']
        if 'keywordForSearch__in' in request.session:
            del request.session['keywordForSearch__in']
        if 'search__in' in request.session:
            del request.session['search__in']

        search = request.POST.get('search')
        keywordForSearch = request.POST.get('keywordForSearch')
        topicForSearch = request.POST.get('topicForSearch')
        ContentForSearch = request.POST.get('ContentForSearch')
        writternbyForSearch = request.POST.get('writternbyForSearch')
        writternforForSearch = request.POST.get('writternforForSearch')
        complexityForSearch = request.POST.get('complexityForSearch')

        q_object = Q()

        if keywordForSearch != '':
            keywordForSearch = keywordForSearch.split(',')
            keywordForSearch = map(str, keywordForSearch)
            id_list = Library.objects.filter(Q
                (Q(reduce(lambda x, y: x | y, [Q(title__icontains=word) for word in keywordForSearch]))
                 |Q(reduce(lambda x, y: x | y, [Q(keywords__icontains=word) for word in keywordForSearch]))
                 |Q(reduce(lambda x, y: x | y, [Q(topic__title__icontains=word) for word in keywordForSearch]))
                 |Q(reduce(lambda x, y: x | y, [Q(topic__description__icontains=word) for word in keywordForSearch]))
                 |Q(reduce(lambda x, y: x | y, [Q(author__icontains=word) for word in keywordForSearch]))
            )).values_list('id',flat=True)
            id_list = list(id_list)
            id_list = map(int, id_list)
            request.session['keywordForSearch__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if search != '':
            id_list = Library.objects.filter(Q(title__icontains=search)|Q(description__icontains=search)
                        |Q(keywords__icontains=search)|Q(author__icontains=search)
                        |Q(writtenBy__name__icontains=search)|Q(writtenFor__name__icontains=search)
                        |Q(topic__title__icontains=search)|Q(topic__description__icontains=search))
            id_list = id_list.values_list('id', flat=True)
            id_list = list(id_list)
            id_list = map(int, id_list)
            print id_list
            request.session['search__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if writternforForSearch != '':
            id_list = searchData('writtenFor__in', writternforForSearch)
            request.session['writtenFor__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if complexityForSearch != '':
            id_list = searchData('complexity__in', complexityForSearch)
            request.session['complexity__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if topicForSearch != '':
            id_list = searchData('topic__in', topicForSearch)
            request.session['topic__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if ContentForSearch != '':
            id_list = searchData('LibraryType__in', ContentForSearch)
            request.session['libraryType__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        if writternbyForSearch != '':
            id_list = searchData('writtenBy__in', writternbyForSearch)
            request.session['writtenBy__in'] = id_list
            q_object.add(Q(id__in=id_list), Q.AND)

        LibraryData = Library.objects.filter(q_object, language=request.session['language'])

    elif request.GET.get('page') != '' and request.GET.get('Filter') == 'search':
        q_object = Q()

        if 'search__in' in request.session:
            q_object.add(Q(id__in=request.session['search__in']), Q.AND)

        if 'keywordForSearch__in' in request.session:
            q_object.add(Q(id__in=request.session['keywordForSearch__in']), Q.AND)

        if 'writtenFor__in' in request.session:
            q_object.add(Q(id__in=request.session['writtenFor__in']), Q.AND)

        if 'complexity__in' in request.session:
            q_object.add(Q(id__in=request.session['complexity__in']), Q.AND)

        if 'topic__in' in request.session:
            q_object.add(Q(id__in=request.session['topic__in']), Q.AND)

        if 'libraryType__in' in request.session:
            q_object.add(Q(id__in=request.session['libraryType__in']), Q.AND)

        if 'writtenBy__in' in request.session:
            q_object.add(Q(id__in=request.session['writtenBy__in']), Q.AND)

        LibraryData = Library.objects.filter(q_object, language=request.session['language'])

    else:
        if 'search__in' in request.session:
            del request.session['search__in']
        if 'writtenBy__in' in request.session:
            del request.session['writtenBy__in']
        if 'libraryType__in' in request.session:
            del request.session['libraryType__in']
        if 'writtenFor__in' in request.session:
            del request.session['writtenFor__in']
        if 'topic__in' in request.session:
            del request.session['topic__in']
        if 'complexity__in' in request.session:
            del request.session['complexity__in']
        if 'keywordForSearch__in' in request.session:
            del request.session['keywordForSearch__in']

        LibraryData = Library.objects.all().filter(language=request.session['language'])

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    Topic_title = Topic.objects.filter(language=request.session['language']).all()
    TopicContent = Topic_title.order_by('title')

    writternByList = WrittenBy.objects.filter(language=request.session['language']).all()
    writternByContent = writternByList.order_by('name')

    writternForList = WrittenFor.objects.filter(language=request.session['language']).all()
    writternForContent = writternForList.order_by('name')

    complexityList = Complexity.objects.filter(language=request.session['language']).all()
    complexityContent = complexityList.order_by('level')

    LibraryTypeList = LibraryType.objects.filter(language=request.session['language']).all()
    LibraryTypeContent = LibraryTypeList.order_by('name')

    if "user_id" in request.session:
        CFR = UserFavouriteResource.objects.filter(Q(user_id=request.session['user_id'])).values_list('library_id', flat=True)
        CFRList = list(CFR)
        int_list = map(int, CFRList)
    else:
        int_list = []

    paginator = Paginator(LibraryData, 5)
    page = request.GET.get('page')
    try:
        LibraryDatas = paginator.page(page)
    except PageNotAnInteger:
        LibraryDatas = paginator.page(1)
    except EmptyPage:
        LibraryDatas = paginator.page(paginator.num_pages)

    instance = get_object_or_404(Library, id=22)
    share_string = quote_plus(instance.description)
    context = {'langContent': langContent, 'TopicContent': TopicContent, 'writternByContent': writternByContent,
               'writternForContent': writternForContent, 'complexityContent': complexityContent,
               'LibraryTypeContent': LibraryTypeContent, 'LibraryDatas': LibraryDatas, 'CFR': int_list,
               'page': page, 'share_string': share_string, }

    return render(request, 'library/library.html', context)


def favourite_resource_user(request, pk):
    chkFavouriteResource = UserFavouriteResource.objects.filter(Q(user_id = request.session['user_id']), Q(library_id = pk))
    if not chkFavouriteResource:
        userFavouriteResource = UserFavouriteResource()
        userFavouriteResource.user_id = request.session['user_id']
        userFavouriteResource.library_id = pk
        userFavouriteResource.save()
    return HttpResponse('Favourite')


def delete_favourite_resource_user(request, pk):
    result = deletefavouriteresourseuser(request.session['user_id'], pk)
    return HttpResponse('DelFavourite')


def delete_resource_user(request, pk):
    result = deletefavouriteresourseuser(request.session['user_id'], pk)
    return HttpResponseRedirect('/users/Profile/')


def deletefavouriteresourseuser(userid, pk):
    chkFavouriteResource = UserFavouriteResource.objects.filter(Q(user_id = userid), Q(library_id = pk))
    if chkFavouriteResource:
        userFavouriteResource = UserFavouriteResource.objects.get(Q(user_id = userid), Q(library_id = pk))
        result = userFavouriteResource.delete()
        return result


def delete_downloaded_resource_user(request, pk):
    chkDLResource = UserResourceDownload.objects.filter(Q(user_id = request.session['user_id']), Q(library_id = pk))
    if chkDLResource:
        userDLResource = UserResourceDownload.objects.filter(Q(user_id = request.session['user_id']), Q(library_id = pk))
        result = userDLResource.delete()
    return HttpResponseRedirect('/users/Profile/')
