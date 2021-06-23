from django import forms
from captcha.fields import ReCaptchaField, ReCaptchaV3


class CommentsBlog(forms.Form):
    captcha = ReCaptchaField(
        label='تصویر امنیتی',
        widget=ReCaptchaV3(api_params={
            'hl': 'fa'
        }),
        error_messages={
            'required': 'لطفا تصویر امنیتی را تایید کنید'
        }
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام خود را وارد کنید'}),
        label='نام')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل')

    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'لطفا شماره خود را وارد کنید(نمایش داده نمیشود)'}),
        label='شماره همراه')
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'لطفا نظر خود را بنویسید'}), label='نظر')
