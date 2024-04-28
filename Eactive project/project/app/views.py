from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users1
from django.shortcuts import render, get_object_or_404
from django.http import Http404



# Create your views here.

# get the string

def hello(request):
    return HttpResponse ("HELLO WORLD")

#get Users_list form database

def Users_list(request):
    users = Users1.objects.all()
    return render(request, 'users_list.html',{'users':users})

#Get user name with id

def user_detail(request, user_id):
    user = get_object_or_404(Users1, pk=user_id)
    return render(request, 'user_details.html', {'user':user})


#Page not found views

def user_detail(request, user_id):
    try:
        user = get_object_or_404(Users1, pk=user_id)
    except Http404:
        return render(request, 'page_not_found.html', status=404)
    return render(request, 'user_details.html', {'user':user})

#Get new user names

def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = Users1.objects.create(name=name, email=email)
        # You can perform additional tasks such as validation here
        return redirect('user_detail', user_id=user.id)  # Redirect to user detail page
    return render(request, 'new_user.html')

#Delete User
def delete_user(request, user_id):
    user = get_object_or_404(Users1, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('User_list')  # Redirect to user list page
    return render(request, 'delete_user.html', {'user':user})