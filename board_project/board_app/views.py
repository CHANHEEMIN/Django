from django.core import paginator
from django.shortcuts import redirect, render
from .models import Board
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def register(request): #url정보가 request변수를 통해 들어옴
    if request.method == 'GET':   
        return render(request,'register.html') # request를 같이 써줘야함 뒤는 템플릿 폴더를 기본적으로 바라본다
    elif request.method =='POST':
        name = request.POST.get('name',None)
        birthday = request.POST.get('birthday',None)
       
        res_data ={}
        if not (name and birthday):
            res_data['error'] = "모두 다 입력해야됩니다."
        else:
            user = Board( #모델구조의 테이블과 연동
                name=name,  #db데이터필드 = 템플릿
                birthday=birthday
            )
            user.save()
        return render(request,'register.html',res_data)
def board_list(request):
    all_boards = Board.objects.all().order_by('id')
    page = request.GET.get('p',1)
    paginator = Paginator(all_boards,5)
    boards = paginator.get_page(page)

    return render(request , "board_list.html", {'boards' : boards})

def board_detail(request,pk):
    try:
        board = Board.objects.get(id=pk)
    except Board.DoesNotExist:
        raise Http404('404 error')

    return render(request,'board_detail.html',{'board':board})

def board_update(request , pk):
    boards = Board.objects.get(id=pk)
    if request.method == 'GET':   
        return render(request,'update.html')
    elif request.method =='POST':       
        boards.name = request.POST['name']
        boards.birthday = request.POST['birthday']

        boards.save()
        return render(request,'update.html',{'boards':boards})

def board_delete(request,pk):
    boards = Board.objects.get(id=pk)
    boards.delete()
    return redirect('/board_list')

def home(request):
    return render(request,"base.html")