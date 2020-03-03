from django.shortcuts import render,redirect
from . import models
from .forms import UserForm, RegisterForm
import hashlib

# Create your views here.
# login/views.py


def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = 'Please check the input fields!'
        if login_form.is_valid():  # Make sure that the username and password are not empty
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # ......
            # Other verifications and validations
            # ......
            try:
                # Login by username
                user = models.User.objects.get(name=username)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                if user.password == hash_code(password):
                    return redirect('/index/')
                else:
                    message = 'Incorrect passwotd!'
            except:
                try:
                    # Login by email
                    user = models.User.objects.get(email=username)
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    if user.password == hash_code(password):
                        return redirect('/index/')
                    else:
                        message = 'Incorrect passwotd!'
                except:
                    message = 'Username does not exist!'
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request,'login/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        # Registration is not allowed while loged in
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Please check the input fields!"
        if register_form.is_valid():  
            # Get the data
            username = register_form.cleaned_data['username']
            firstname = register_form.cleaned_data['firstname']
            lastname = register_form.cleaned_data['lastname']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2: 
                message = "The passwords you entered do not match"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  
                    message = 'Username cannot be used. Please choose another username'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  
                    message = 'Email address cannot be used. Please choose another email address'
                    return render(request, 'login/register.html', locals())

                # Create new user if all the information is valid
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.first_name = firstname
                new_user.last_name = lastname
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.save()
                # jump to log in page
                return redirect('/login/')  
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

def hash_code(s, salt='ece651'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) 
    return h.hexdigest()