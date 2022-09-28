from django.shortcuts import render
from .models import CustomModel

def user(request):
    # case 1
    """
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()
    """
    # case 2
    CustomModel.objects.create(
        location="user"
    )
    
    return render(request, 'user.html')


