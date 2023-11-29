from django.shortcuts import render, redirect
from django.views import View
from .models import ShortenURL
from .forms import URLSubmissionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .services import URLShortenerService


class HomeView(View):
    template_name = 'home.html'
    login_url = '/login/'
    redirect_field_name = 'url_app/home.html'
    
    def get(self, request):
        form = URLSubmissionForm()
        shortened_urls = ShortenURL.objects.filter(user=request.user) if request.user.is_authenticated else []
        return render(request, self.template_name, {'form':form, 'shortened_urls':shortened_urls})
    
    def post(self, request):
        form = URLSubmissionForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = URLShortenerService.shorten_url(original_url)
            
            if shortened_url:
                shortened_url_instance = ShortenURL.objects.create(original_url=original_url, short_url=shortened_url, user=request.user)
                shortened_url_instance.generate_qr_code()
                return redirect('home')
        shortened_urls = ShortenURL.objects.filter(user=request.user) if request.user.is_authenticated else []
        return render(request, self.template_name, {'form':form, 'shortened_urls':shortened_urls})

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)