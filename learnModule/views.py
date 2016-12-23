from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q
from .forms import StoryForm
from string import ascii_lowercase
from users.models import *
from story.models import *
from library.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os, re, math
from django.db.models import Sum, Avg, Count, Max


def index(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    context = {'langContent': langContent, }
    return render(request, 'learnModule/index.html', context)


def language(request, value , next= '/'):
    request.session['language'] = value
    if request.GET.has_key('next'):
        next = request.GET['next']
    return HttpResponseRedirect(next)

def help(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    context = {'langContent': langContent, }
    return render(request, 'learnModule/help.html', context)


def team(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    context = {'langContent': langContent, }
    return render(request, 'learnModule/team.html', context)

def FPIC(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    Data = Library.objects.all().filter(language=request.session['language'], libraryFor='1')
    DataInfo = Library.objects.all().filter(language=request.session['language'], libraryFor='1', highlight='1')
    DataToolkit = Library.objects.all().filter(language=request.session['language'], libraryFor='1', highlight='2')
    if "user_id" in request.session:
        CFC1 = UserFavouriteResource.objects.filter(Q(user_id=request.session['user_id'])).values_list('library_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []
    if "user_id" in request.session:
        CLC = UserContent.objects.filter(Q(user_id=request.session['user_id']), Q(content_id=1))
    else:
        CLC = []
    instance = get_object_or_404(Library, id=22)
    share_string = quote_plus(instance.description)
    context = {'LibraryData' : Data, 'DataInfo' : DataInfo, 'DataToolkit' : DataToolkit, 'CFC': CFC,
    'CLC': CLC, 'share_string': share_string, 'langContent': langContent, }
    return render(request, 'learnModule/FPIC.html', context)


def Consultation(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    Data = Library.objects.all().filter(language=request.session['language'], libraryFor='2')
    DataInfo = Library.objects.all().filter(language=request.session['language'], libraryFor='2', highlight='1')
    DataToolkit = Library.objects.all().filter(language=request.session['language'], libraryFor='2', highlight='2')
    if "user_id" in request.session:
        CFC1 = UserFavouriteResource.objects.filter(Q(user_id=request.session['user_id'])).values_list('library_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []
    if "user_id" in request.session:
        CLC = UserContent.objects.filter(Q(user_id=request.session['user_id']), Q(content_id=1))
    else:
        CLC = []
    instance = get_object_or_404(Library, id=22)
    share_string = quote_plus(instance.description)
    context = {'LibraryData' : Data, 'DataInfo' : DataInfo, 'DataToolkit' : DataToolkit, 'CFC': CFC,
    'CLC': CLC, 'share_string': share_string, 'langContent': langContent, }
    return render(request, 'learnModule/Consultation.html', context)

def FPICCourses(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    Data = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(contentFor='1')))[:12]
    Data1 = Data.values_list('id', flat=True)
    cfcList = list(Data1)
    int_list = map(int, cfcList)
    ContentTitle = Content.objects.filter(course_id__in = int_list)
    DataNew = Course.objects.all().filter(language=request.session['language'], contentFor='1').order_by('createdDate')[:4]
    DataRecommended = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(contentFor='1'), ~Q(recommend = '0'))).order_by('-recommend')[:4]
    if "user_id" in request.session:
        CFC1 = UserFavouriteCourse.objects.filter(Q(user_id=request.session['user_id'])).values_list('course_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []

    context = {'Data' : Data, 'DataNew' : DataNew, 'DataRecommended' : DataRecommended,
        'ContentTitle': ContentTitle, 'CFC': CFC, 'langContent': langContent,}
    return render(request, 'learnModule/FPICCourses.html', context)


def ConsultCourses(request):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    Data = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(contentFor='2')))[:12]
    Data1 = Data.values_list('id', flat=True)
    cfcList = list(Data1)
    int_list = map(int, cfcList)
    ContentTitle = Content.objects.filter(course_id__in = int_list)
    DataNew = Course.objects.all().filter(language=request.session['language'], contentFor='2').order_by('createdDate')[:4]
    DataRecommended = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(contentFor='2'), ~Q(recommend = '0'))).order_by('-recommend')[:4]
    if "user_id" in request.session:
        CFC1 = UserFavouriteCourse.objects.filter(Q(user_id=request.session['user_id'])).values_list('course_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []
    context = {'Data' : Data, 'DataNew' : DataNew, 'DataRecommended' : DataRecommended,
        'ContentTitle': ContentTitle, 'CFC': CFC, 'langContent': langContent,}
    return render(request, 'learnModule/ConsultCourses.html', context)

def courseHome(request, pk, content_id=''):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    CourseData = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(id=pk)))
    Data1 = CourseData.values_list('id', flat=True)
    cfcList = list(Data1)
    int_list = map(int, cfcList)
    ContentTitle = Content.objects.filter(course_id__in = int_list).order_by('srNo')

    if "user_id" in request.session:
        CFC1 = UserFavouriteContent.objects.filter(Q(user_id=request.session['user_id'])).values_list('content_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []
    context = {'CourseData': CourseData, 'ContentTitle': ContentTitle, 'CFC': CFC, 'langContent': langContent,}
    return render(request, 'learnModule/CourseHome.html', context)


def contentHome(request, pk):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    # Query for Content Data
    contentData = Content.objects.get(id = pk)
    # Query for Quiz, Question and Choice list
    QuizList = Quiz.objects.filter(content_id=pk)
    QuizList1 = Quiz.objects.filter(content_id=pk).values('id')
    QuestionList = Question.objects.filter(quiz_id__in=QuizList)
    QuestionList1 = Question.objects.filter(quiz_id__in=QuizList).values('id')
    ChoiceList = Choice.objects.filter(question_id__in=QuestionList)
    # Save data for quiz answer
    if request.method == 'POST' and request.POST['submit'] == 'Check Result':
        findAttempt = UserQuiz.objects.filter(user_id=request.session['user_id'], quiz_id=QuizList)
        findAttempt1 = findAttempt.aggregate(Max('attempt')).values()[0]
        for q in QuestionList1:
            userQuiz = UserQuiz()
            userQuiz.user_id = request.session['user_id']
            userQuiz.quiz_id = QuizList1[0]['id']
            if findAttempt1:
                userQuiz.attempt = int(findAttempt1)+1
            else:
                userQuiz.attempt = 1
            userQuiz.question_id = q['id']
            result = request.POST.get(str(userQuiz.question_id))
            userQuiz.choice_id = result
            userQuiz.createdDate = datetime.datetime.now()
            choice_course1 = ChoiceList.filter(question_id=q['id'], isAnswer = True).values('id')
            if result:
                if int(result) == choice_course1[0]['id']:
                    userQuiz.isCorrect = True
                else:
                    userQuiz.isCorrect = False
            else:
                userQuiz.isCorrect = False
            userQuiz.save()

    # Query for Favourite Content and Learned Content BUTTON
    CFC = UserFavouriteContent.objects.filter(Q(user_id = request.session['user_id']), Q(content_id = pk))

    CLC = UserContent.objects.filter(Q(user_id = request.session['user_id']), Q(content_id = pk))

    context = {'contentData': contentData, 'QuizList': QuizList,
                'QuestionList': QuestionList, 'ChoiceList': ChoiceList, 'CFC':CFC, 'CLC':CLC, 'langContent': langContent,}
    return render(request, 'learnModule/contentHome.html', context)


def contentsHome(request, pk):
    if "language" not in request.session:
        request.session['language'] = '2'

    langList = Language.objects.all()
    langContent = langList.order_by('name')

    # Query for Content Data
    CourseData = Course.objects.all().filter(Q(Q(language=request.session['language']), Q(id=pk)))
    Data1 = CourseData.values_list('id', flat=True)
    cfcList = list(Data1)
    int_list = map(int, cfcList)
    ContentLists = Content.objects.filter(course_id__in = int_list).order_by('srNo')
    ContentIds = ContentLists.values_list('id', flat=True)
    idlist = list(ContentIds)
    int_idlist = map(int, idlist)
    contentsCount = ContentLists.aggregate(qCount = Count('id')).values()
    print contentsCount
    # contentData = Content.objects.get(id = pk)
    # Query for Quiz, Question and Choice list
    QuizList = Quiz.objects.filter(content_id__in=int_idlist)
    Data2 = QuizList.values_list('id', flat=True)
    cfcList2 = list(Data2)
    int_list2 = map(int, cfcList2)
    QuestionList = Question.objects.filter(quiz_id__in=int_list2)
    Data3 = QuestionList.values_list('id', flat=True)
    cfcList3 = list(Data3)
    int_list3 = map(int, cfcList3)
    ChoiceList = Choice.objects.filter(question_id__in=int_list3)
    Data4 = ChoiceList.values_list('id', flat=True)
    cfcList4 = list(Data4)
    int_list4 = map(int, cfcList4)

    # Query for Favourite Content and Learned Content BUTTON
    if "user_id" in request.session:
        CFC1 = UserFavouriteContent.objects.filter(Q(user_id=request.session['user_id']), Q(content_id__in = int_idlist)).values_list('content_id', flat=True)
        CFC2 = list(CFC1)
        CFC = map(int, CFC2)
    else:
        CFC = []

    if "user_id" in request.session:
        CLC = UserContent.objects.filter(Q(user_id=request.session['user_id']), Q(content_id__in = int_idlist)).values_list('content_id', flat=True)
        CLC = list(CLC)
        CLC = map(int, CLC)
    else:
        CLC = []

    paginator = Paginator(ContentLists, 1)
    page = request.GET.get('page')
    try:
        ContentList = paginator.page(page)
    except PageNotAnInteger:
        ContentList = paginator.page(1)
    except EmptyPage:
        ContentList = paginator.page(paginator.num_pages)

    checkList = CheckList.objects.filter(content_id__in = int_idlist).order_by('srNo')
    cl1 = checkList.values_list('id', flat=True)
    cl1 = list(cl1)
    cl1 = map(int, cl1)
    summaryList = Summary.objects.filter(content_id__in = int_idlist)
    sl1 = summaryList.values_list('id', flat=True)
    sl1 = list(sl1)
    sl1 = map(int, sl1)
    summaryChildList = SummaryChild.objects.filter(summary_id__in = sl1)
    finishList = Finish.objects.filter(content_id__in = int_idlist)

    Data = Library.objects.all().filter(language=request.session['language'], course=pk)

    context = {'ContentList': ContentList, 'CFC':CFC, 'CLC':CLC, 'QuizList': QuizList,
        'QuestionList': QuestionList, 'ChoiceList': ChoiceList, 'checkList': checkList,
        'summaryList': summaryList, 'summaryChildList': summaryChildList,
        'finishList': finishList, 'Data': Data, 'langContent': langContent,} #
    return render(request, 'learnModule/contentsHome.html', context)


def pdfDownload(request, filename, pk):
    Static_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    f = open(Static_path+'/staticfiles/learnModule/images/'+filename, 'rb')
    response = HttpResponse(f.read(),content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename='+filename
    return HttpResponseRedirect('/learnModule/contentsHome/')

def checklist_save(request):
    querystring = request.META['QUERY_STRING']
    querystring = querystring.split('&')
    for ques_ans in querystring:
        ques = ques_ans.split('=')
        checklistID = ques[0]
        isChecked = ques[1]
        userCheckList = UserChecklist()
        userCheckList.user_id = request.session['user_id']
        userCheckList.checkList_id = checklistID
        if isChecked == "checked" :
            isChecked = True
        else:
            isChecked = False
        userCheckList.isChecked = isChecked
        # Delete Previous Data
        delUserChecklist = UserChecklist.objects.filter(user_id=request.session['user_id'], checkList_id=checklistID)
        if delUserChecklist:
            delUserChecklist.delete()
        userCheckList.save()

    uCLDetail = UserChecklist.objects.filter(user_id=request.session['user_id'])
    listCount = uCLDetail.aggregate(qCount = Count('checkList_id')).values()
    lc = map(float, listCount)
    checkedCount = uCLDetail.filter(isChecked=True).aggregate(cCount = Count('checkList_id')).values()
    cc = map(float, checkedCount)
    if int(cc[0]) < 1:
        score = 0.0
    else:
        score = cc[0] * 100 / lc[0]

    if score < 21 :
        fbWords = "Feedback A"
    elif score < 51 :
        fbWords = "Feedback B"
    elif score < 76 :
        fbWords = "Feedback C"
    elif score < 101 :
        fbWords = "Feedback D"

    context = {'uCLDetail': uCLDetail, 'score': score, 'fbWords': fbWords}
    return render(request, 'learnModule/checkListAns.html', context)


def checkListAns(request):
    uCLDetail = UserChecklist.objects.filter(user_id=request.session['user_id'])
    listCount = uCLDetail.aggregate(qCount = Count('checkList_id')).values()
    lc = map(float, listCount)
    checkedCount = uCLDetail.filter(isChecked=True).aggregate(cCount = Count('checkList_id')).values()
    cc = map(float, checkedCount)
    if int(cc[0]) < 1:
        score = 0.0
    else:
        score = cc[0] * 100 / lc[0]

    if score < 21 :
        fbWords = "Feedback A"
    elif score < 51 :
        fbWords = "Feedback B"
    elif score < 76 :
        fbWords = "Feedback C"
    elif score < 101 :
        fbWords = "Feedback D"
    context = {'uCLDetail': uCLDetail, 'score': score, 'fbWords': fbWords}
    return render(request, 'learnModule/checkListAns.html', context)


def quiz_save(request,pk):
    querystring = request.META['QUERY_STRING']
    querystring = querystring.split('&')
    quizid = pk
    findAttempt = UserQuiz.objects.filter(user_id=request.session['user_id'], quiz_id=quizid)
    findAttempt1 = findAttempt.aggregate(Max('attempt')).values()[0]
    if findAttempt1:
        attempt = int(findAttempt1)+1
    else:
        attempt = 1
    for ques_ans in querystring:
        ques = ques_ans.split('=')
        questionid = ques[0]
        choiceid = ques[1]
        userQuiz = UserQuiz()
        userQuiz.user_id = request.session['user_id']
        userQuiz.quiz_id = quizid
        userQuiz.attempt = attempt
        userQuiz.question_id = questionid
        userQuiz.choice_id = choiceid
        correctChoice = Choice.objects.filter(question_id=questionid, isAnswer=True).values('id')
        correctChoice = correctChoice[0]['id']
        correctChoice = int(correctChoice)
        if int(choiceid) == correctChoice:
            userQuiz.isCorrect = True
        else:
            userQuiz.isCorrect = False
        userQuiz.save()

    maxAttempt1 = UserQuiz.objects.filter(user_id=request.session['user_id'], quiz_id=quizid)
    maxAttempt2 = maxAttempt1.aggregate(Max('attempt')).values()[0]
    uQDetail = UserQuiz.objects.filter(user_id=request.session['user_id'], attempt=maxAttempt2, quiz_id=quizid)
    correctChoice = Choice.objects.filter(isAnswer=True)
    questionCount = uQDetail.aggregate(qCount = Count('question_id')).values()
    qc = map(float, questionCount)
    correctCount = uQDetail.filter(isCorrect=True).aggregate(cCount = Count('question_id')).values()
    cc = map(float, correctCount)

    if int(cc[0]) < 1:
        score = 0
    else:
        score = cc[0] * 100 / qc[0]

    if score < 21 :
        fbWords = "Feedback A"
    elif score < 51 :
        fbWords = "Feedback B"
    elif score < 76 :
        fbWords = "Feedback C"
    elif score < 101 :
        fbWords = "Feedback D"
    context = {'uQDetail': uQDetail, 'correctChoice': correctChoice, 'score': score, 'fbWords': fbWords}
    return render(request, 'learnModule/quiz_result.html', context)


def quiz_result(request):
    if "user_id" in request.session:
        maxAttempt1 = UserQuiz.objects.filter(user_id=request.session['user_id'])#, quiz_id=request.POST.get(str('quizNo')))
        maxAttempt2 = maxAttempt1.aggregate(Max('attempt')).values()[0]
        uQDetail = UserQuiz.objects.filter(user_id=request.session['user_id'], attempt=maxAttempt2)#, quiz_id=request.POST.get(str('quizNo')))
        correctChoice = Choice.objects.filter(isAnswer=True)
        questionCount = uQDetail.aggregate(qCount = Count('question_id')).values()
        qc = map(float, questionCount)
        correctCount = uQDetail.filter(isCorrect=True).aggregate(cCount = Count('question_id')).values()
        cc = map(float, correctCount)
        if int(cc[0]) < 1:
            score = 0
        else:
            score = cc[0] * 100 / qc[0]

        if score < 21 :
            fbWords = "Feedback A"
        elif score < 51 :
            fbWords = "Feedback B"
        elif score < 76 :
            fbWords = "Feedback C"
        elif score < 101 :
            fbWords = "Feedback D"

        context = {'uQDetail': uQDetail, 'correctChoice': correctChoice, 'score': score, 'fbWords': fbWords}
        return render(request, 'learnModule/quiz_result.html', context)
    else:
        return render(request, 'users/index.html', '')


def boolQuiz_save(request,pk):
    querystring = request.META['QUERY_STRING']
    querystring = querystring.split('&')
    quizid = pk
    findAttempt = UserQuiz.objects.filter(user_id=request.session['user_id'], quiz_id=quizid)
    findAttempt1 = findAttempt.aggregate(Max('attempt')).values()[0]
    if findAttempt1:
        attempt = int(findAttempt1)+1
    else:
        attempt = 1
    for ques_ans in querystring:
        ques = ques_ans.split('=')
        questionid = ques[0]
        choiceid = ques[1]
        userQuiz = UserQuiz()
        userQuiz.user_id = request.session['user_id']
        userQuiz.quiz_id = quizid
        userQuiz.attempt = attempt
        userQuiz.question_id = questionid
        userQuiz.choice_id = choiceid
        correctChoice = Choice.objects.filter(question_id=questionid, isAnswer=True).values('id')
        correctChoice = correctChoice[0]['id']
        correctChoice = int(correctChoice)
        if int(choiceid) == correctChoice:
            userQuiz.isCorrect = True
        else:
            userQuiz.isCorrect = False
        userQuiz.save()

    maxAttempt1 = UserQuiz.objects.filter(user_id=request.session['user_id'], quiz_id=quizid)
    maxAttempt2 = maxAttempt1.aggregate(Max('attempt')).values()[0]
    uBQDetail = UserQuiz.objects.filter(user_id=request.session['user_id'], attempt=maxAttempt2, quiz_id=quizid)
    correctChoice = Choice.objects.filter(isAnswer=True)
    questionCount = uBQDetail.aggregate(qCount = Count('question_id')).values()
    qc = map(float, questionCount)
    correctCount = uBQDetail.filter(isCorrect=True).aggregate(cCount = Count('question_id')).values()
    cc = map(float, correctCount)
    if int(cc[0]) < 1:
        score = 0
    else:
        score = cc[0] * 100 / qc[0]

    if score < 21 :
        fbWords = "Feedback A"
    elif score < 51 :
        fbWords = "Feedback B"
    elif score < 76 :
        fbWords = "Feedback C"
    elif score < 101 :
        fbWords = "Feedback D"
    context = {'uBQDetail': uBQDetail, 'correctChoice': correctChoice, 'score': score, 'fbWords': fbWords}
    return render(request, 'learnModule/boolQuiz_result.html', context)


def boolQuiz_result(request):
    if "user_id" in request.session:
        maxAttempt1 = UserQuiz.objects.filter(user_id=request.session['user_id'])#, quiz_id=request.POST.get(str('quizNo')))
        maxAttempt2 = maxAttempt1.aggregate(Max('attempt')).values()[0]
        uBQDetail = UserQuiz.objects.filter(user_id=request.session['user_id'], attempt=maxAttempt2)#, quiz_id=request.POST.get(str('quizNo')))
        correctChoice = Choice.objects.filter(isAnswer=True)
        questionCount = uBQDetail.aggregate(qCount = Count('question_id')).values()
        qc = map(float, questionCount)
        correctCount = uBQDetail.filter(isCorrect=True).aggregate(cCount = Count('question_id')).values()
        cc = map(float, correctCount)
        if int(cc[0]) < 1:
            score = 0
        else:
            score = cc[0] * 100 / qc[0]

        if score < 21 :
            fbWords = "Feedback A"
        elif score < 51 :
            fbWords = "Feedback B"
        elif score < 76 :
            fbWords = "Feedback C"
        elif score < 101 :
            fbWords = "Feedback D"
        context = {'uBQDetail': uBQDetail, 'correctChoice': correctChoice, 'score': score, 'fbWords': fbWords}
        return render(request, 'learnModule/boolQuiz_result.html', context)
    else:
        return render(request, 'users/index.html', '')


def favourite_content_user(request, pk):
    chkFavouriteContent = UserFavouriteContent.objects.filter(Q(user_id = request.session['user_id']), Q(content_id = pk))
    if not chkFavouriteContent:
        userFavouriteContent = UserFavouriteContent()
        userFavouriteContent.user_id = request.session['user_id']
        userFavouriteContent.content_id = pk
        userFavouriteContent.save()
    return HttpResponse('Favourite')


def delete_favourite_content_user(request, pk):
    result = deletefavouritecontentuser(request.session['user_id'], pk)
    return HttpResponse('DelFavourite')


def delete_content_user(request, pk):
    result = deletefavouritecontentuser(request.session['user_id'], pk)
    return HttpResponseRedirect('/users/Profile/')


def deletefavouritecontentuser(userid, pk):
    chkFavouriteContent = UserFavouriteContent.objects.filter(Q(user_id = userid), Q(content_id = pk))
    if chkFavouriteContent:
        userFavouriteContent = UserFavouriteContent.objects.get(Q(user_id = userid), Q(content_id = pk))
        result = userFavouriteContent.delete()
        return result


def learned_user(request, pk):
    chkContent = UserContent.objects.filter(Q(user_id = request.session['user_id']), Q(content_id = pk))
    if not chkContent:
        userContent = UserContent()
        userContent.user_id = request.session['user_id']
        userContent.content_id = pk
        userContent.isCompleted = True
        userContent.save()
    return HttpResponse('Favourite')


    """
    findTopic = Topic.objects.filter(Q(content__pk=pk)).values('id')[0]['id']
    print("Topic ID", findTopic)
    findTopicContents = Content.objects.filter(topic__id=findTopic).values('id')
    print(findTopicContents)

    for ftc in findTopicContents:
        chkTopicContents = UserContent.objects.filter(Q(user_id = request.session['user_id']), Q(content_id = ftc.id), Q(isCompleted=0))
        if chkTopicContents:
            break
        userTopic = UserTopic()
        userTopic.user_id = request.session['user_id']
        userTopic.topic_id = ctc.id
        userTopic.isCompleted = True
        userTopic.save()
    """


def delete_learned_content_user(request, pk):
    result = deletelearnedcontentuser(request.session['user_id'], pk)
    return HttpResponse('DelFavourite')


def delete_content_user(request, pk):
    result = deletelearnedcontentuser(request.session['user_id'], pk)
    return HttpResponseRedirect('/users/Profile/')


def deletelearnedcontentuser(userid, pk):
    chkLearnedContent = UserContent.objects.filter(Q(user_id = userid), Q(content_id = pk))
    if chkLearnedContent:
        userContent = UserContent.objects.get(Q(user_id = userid), Q(content_id = pk))
        result = userContent.delete()
        return result


def favourite_course_user(request, pk):
    chkFavouriteCourse = UserFavouriteCourse.objects.filter(Q(user_id = request.session['user_id']), Q(course_id = pk))
    if not chkFavouriteCourse:
        userFavouriteCourse = UserFavouriteCourse()
        userFavouriteCourse.user_id = request.session['user_id']
        userFavouriteCourse.course_id = pk
        userFavouriteCourse.save()
    return HttpResponse('Favourite')


def delete_favourite_course_user(request, pk):
    result = deletefavouritecourseuser(request.session['user_id'], pk)
    return HttpResponse('DelFavourite')


def delete_course_user(request, pk):
    result = deletefavouritecourseuser(request.session['user_id'], pk)
    return HttpResponseRedirect('/users/Profile/')


def deletefavouritecourseuser(userid, pk):
    chkFavouriteCourse = UserFavouriteCourse.objects.filter(Q(user_id = userid), Q(course_id = pk))
    if chkFavouriteCourse:
        userFavouriteCourse = UserFavouriteCourse.objects.get(Q(user_id = userid), Q(course_id = pk))
        result = userFavouriteCourse.delete()
        return result

    '''
    message = 'You are not logged in.'
    context = {'message': message }
    return render(request, 'users/index.html', context)
    '''
