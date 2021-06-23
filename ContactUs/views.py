from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from ContactUs.forms import ContactUsForm
from ContactUs.models import ContactUs, About


def contact_us(request):
    contact_form = ContactUsForm(request.POST or None)
    about_section: About = About.objects.first()
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        ContactUs.objects.create(name=name, email=email, message=message)
        messages.success(request, 'پیام شما با موفقیت ارسال شد')
        return redirect('/contact-us')
    contact_form = ContactUsForm()
    context = {
        'contact_form': contact_form,
        'about_section': about_section
    }
    return render(request, 'contactus.html', context)
