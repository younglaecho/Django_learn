from django import forms
from .models import Deathuser
from django.contrib.auth.hashers import check_password

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
            deathuser = Deathuser.objects.get(username=username)
            if not check_password(password, deathuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.') # 특정 필드에 에러를 넣는 함수
            else:
                self.user_id = deathuser.id
            