from django.shortcuts import render
from .models import mails

# Create your views here.


def home(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        m = mails()
        m.email = data
        m.save()
        #as simple as that we are using model method to receive data
    return render(request, 'index.html')