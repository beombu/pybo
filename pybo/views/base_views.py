

from ..models import Question
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


def index(request):
    """
    pybo목록 출력
    """
    page = request.GET.get('page','1') #페이지

    question_list = Question.objects.order_by('-create_date')#조회
    paginator = Paginator(question_list,10)#페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}

    return render(request, 'pybo/question_list.html',context)# render = 템플릿 파일을 사용하여 화면에 출력하는 함수

    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id = question_id)#qeustion은 Question 객체의 id값을 추출한다.
    question = get_object_or_404(Question, pk=question_id)#Question객체의 id같을 추출하는데 해당하는 값이 없으면 오류페이지 404를 반환
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)
