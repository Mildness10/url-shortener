from django.shortcuts import render, redirect
from django.views import View
from .models import ShortenURL


class HomeView(View):
    template_name = 'home.html'
    
    def get(self, request):
        shortened_urls = ShortenURL.objects.all()
        return render(request, self.template_name, {'shortened_urls':shortened_urls})
    
    def post(self, request):
        original_url = request.POST.get('original_url')
        #code to generate the shortened URL using shrtco.de API
        shortened_url = ShortenURL.objects.create(original_url=original_url, short_key="klm789")
        shortened_url.generate_qr_code()
        return redirect('home')
        