from django.shortcuts import render
from .models import CustomModel

def user(request):
    CustomModel.objects.create(
        location="user"
    )
    
    return render(request, 'user.html')


