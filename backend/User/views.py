from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login as loginf , logout
from .models import Users

def Register(request):
    # Delete previous user
    Users.objects.filter(username='moh').delete()

    # Create new user
    newuser = Users.objects.create_user(
        username="h",
        password="12",
        UserInputID="U002",
        UserOutputID="O002"
    )
    newuser.is_active = True
    newuser.save()
    return HttpResponse('The user has been successfully created, check your database')

def login_view(request):
    user = authenticate(username='h', password='12')
    if user is not None:
        loginf(request, user)
        return HttpResponse("Login successful!")
    else:
        return HttpResponse("Login failed!")
    
def logout_view(request):
    logout(request)
    return HttpResponse('Loggedout')
