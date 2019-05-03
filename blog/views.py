from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import ContactForm
from django.core.mail import EmailMessage

import requests

# Create your views here.


class PostListView(ListView):
    """Homepage list of posts view"""
    model = Post
    template_name =  'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    """Post Detail views"""
    model = Post


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})


def ContactSubmissionView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            ''' check captcha thingy '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            
            if result['success']:
                contact_from_email = form.cleaned_data['from_email']
                contact_body = form.cleaned_data['body']
                contact_name = form.cleaned_data['name']
                                
                email = EmailMessage(f'Message From {contact_name} ({contact_from_email})', contact_body, to=['ben@greendalba.com'])
                email.send()
                return redirect('/success')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            
    return render(request, "blog/contactform.html", {'form': form})

def ContactSuccessView(request):
    return render(request, "blog/contactsuccess.html", {'title': 'Thank You'})

def EasterEgg(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
