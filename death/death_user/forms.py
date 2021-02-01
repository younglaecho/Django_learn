from django import forms
from .models import Deathuser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력하세요.'
        },
        max_length=32, label="사용자 이름")
    useremail = forms.EmailField(
        error_messages={
            'required': '이메일을 입력하세요.'
        },
        max_length=128, label='이메일')
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호 확인을 입력하세요'
        },
        widget=forms.PasswordInput, label="비밀번호 확인")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if Deathuser.objects.filter(username=username).exists():
            self.add_error('username', '아이디가 이미 존재합니다.')
        if password != re_password:
            self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
        else:
            self.username = username
            self.useremail = useremail
            self.password = password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력하세요.'
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label="비밀번호") # widget=forms.PasswordInput : 입력이 비밀번호 형태로..

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                deathuser = Deathuser.objects.get(username=username)
            except Deathuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return
            if not check_password(password, deathuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.') # 특정 필드에 에러를 넣는 함수
            else:
                self.user_id = deathuser.id
            