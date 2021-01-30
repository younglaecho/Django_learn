from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password 
# make_password : 비밀번호를 암호화     check_password : 비밀번호를 확인
from .models import Deathuser
from .forms import LoginForm
# Create your views here.
# views.py : 비즈니스 로직을 관리하는 파이썬 파일

def home(request):
    user_id = request.session.get('user')  # 세션으로부터 가져옴.

    if user_id:
        deathuser = Deathuser.objects.get(pk=user_id) # user_id를 기본키로 함
        return HttpResponse(deathuser.username)

    return HttpResponse('Home')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}  
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력하세요'
#         else:
#             deathuser = Deathuser.objects.get(username=username)  # 모델에서 username이라는 uaername을 가진 객체를 가져옴
#             if check_password(password, deathuser.password):  # 객체에 입력된 비밀번호와 입력한 비밀번호를 비교
#                 request.session['user'] = deathuser.id  # 사용자의 아이디 값을 세션에 저장
#                 return redirect('/')
#                 pass
#             else:
#                 res_data['error'] = '비밀번호를 틀럈습니다.'

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            # session_code
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') 
        # GET 방식으로 접근할 떄 

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        # request.POST의 get 메소드의 두번째 매개변수는 기본 값을 의미한다.

        # username = request.POST['username']
        # password = request.POST['password']
        # re_password = request.POST['re-password']

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            # return HttpResponse('비밀번호가 다릅니다!')
        else:
            deathuser = Deathuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

        deathuser.save()

        return render(request, 'login.html', res_data) # res_data라는 변수를 html 코드로 전송
        # POST 방식으로 접근할 떄

