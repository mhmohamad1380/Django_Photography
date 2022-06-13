from captcha.fields import ReCaptchaField,ReCaptchaV3
from django import forms


class ContactUsForm(forms.Form):
    captcha = ReCaptchaField(
        label='تصویر امنیتی',
        widget=ReCaptchaV3(api_params={
            'hl': 'fa'
        }),
        error_messages={
            'required':'لطفا تصویر امنیتی را تایید کنید'
        }
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'لطفا نام خود را وارد کنید',
                   'style': 'border-radius:20px;border:none'}),
        label='نام :')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'لطفا ایمیل خود را وارد کنید',
                                       'style': 'border-radius:20px;border:none'}),
        label='ایمیل :')
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'لطفا پیام خود را وارد کنید',
                                     'style': 'border-radius:20px;border:none'}),
        label='پیام :')
