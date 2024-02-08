from django.shortcuts import render, redirect
from .forms import ShortenURLForm
from .models import ShortenedURL
import shortuuid

def shorten_url(request):
    
    if request.method == 'POST':

        form = ShortenURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            try:
                shorten_url = ShortenedURL.objects.get(original_url=original_url)
                short_code = shorten_url.short_code
                return render(request, 'shortener/success.html', {'short_url': f'http://127.0.0.1:8000/{short_code}'})
            except ShortenedURL.DoesNotExist:
                short_code = shortuuid.uuid()[:8]  # Use shortuuid library for short codes
                ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
                return render(request, 'shortener/success.html', {'short_url': f'http://127.0.0.1:8000/{short_code}'})
    else:
        form = ShortenURLForm()

    return render(request, 'shortener/shorten_url.html', {'form': form})


def redirect_original(request, short_code):
    
    try:
        shortened_url = ShortenedURL.objects.get(short_code=short_code)
        return redirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        return render(request, 'shortener/invalid.html', {})
