from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력하세요.'
        },
        max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력하세요.'
        },
        widget=forms.Textarea, label="내용") # widget=forms.Textarea : 입력이 텍스트에어리어 형태로..
    tags = forms.CharField(
        required= False, label="태그")
