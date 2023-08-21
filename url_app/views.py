from django.shortcuts import render, redirect
from django.views import View
from .models import ShortenURL
from .forms import URLSubmissionForm


class HomeView(View):
    template_name = 'home.html'
    
    def get(self, request):
        form = URLSubmissionForm()
        shortened_urls = ShortenURL.objects.all()
        return render(request, self.template_name, {'form':form, 'shortened_urls':shortened_urls})
    
    def post(self, request):
        form = URLSubmissionForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
        # original_url = request.POST.get('original_url')
        #code to generate the shortened URL using shrtco.de API
            shortened_url = ShortenURL.objects.create(original_url=original_url, short_key="ghi789")
            shortened_url.generate_qr_code()
            return redirect('home')
        
        shortened_urls = ShortenURL.objects.all()
        return render(request, self.template_name, {'form':form, 'shortened_urls':shortened_urls})
        