from django.shortcuts import render
from .models import News
# Create your views here.
def home(request):
    first_news=News.objects.first()
    return render(request, 'home.html')