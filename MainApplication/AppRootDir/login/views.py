from django.shortcuts import render,redirect
from django.db.models import Max, Min
from . import models
from .forms import UserForm, RegisterForm, ChpasswdForm
from reservation.models import Table, Reservation
from waitlist.models import Waitlist
import hashlib

# Create your views here.
# login/views.py


def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login', None):
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
                request.session['email'] = user.email
                request.session['catagory'] = user.catagory
                if user.password == hash_code(password):
                    return redirect('/index/')
                else:
                    message = 'Incorrect password!'
            except:
                try:
                    # Login by email
                    user = models.User.objects.get(email=username)
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    request.session['email'] = user.email
                    request.session['catagory'] = user.catagory
                    if user.password == hash_code(password):
                        return redirect('/index/')
                    else:
                        message = 'Incorrect password!'
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

def chpasswd(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        change_form = ChpasswdForm(request.POST)
        message = 'Please check the input fields!'
        if change_form.is_valid():
            password = change_form.cleaned_data['password']
            password1 = change_form.cleaned_data['password1']
            password2 = change_form.cleaned_data['password2']
            try:
                user = models.User.objects.get(name=request.session['user_name'])
                if user.password == hash_code(password) or user.password == password:
                    if password1 != password2: 
                        message = "The passwords you entered do not match"
                        return render(request, 'login/register.html', locals())
                    models.User.objects.filter(name=request.session['user_name']).update(password=hash_code(password1))
                    return redirect('/chpasswdsuccess/')
                else:
                    message = 'Incorrect password!'
                    return render(request, 'login/chpasswd.html', locals())
            except:
                return render(request, 'login/chpasswd.html', locals())
    change_form = ChpasswdForm()        
    return render(request, 'login/chpasswd.html', locals())

def chpasswdsuccess(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/chpasswdsuccess.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

def profile(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request,'login/profile.html')

def deleteuser(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name_db = models.User.objects.filter(name=request.session['user_name'])
    if name_db:
        name_db.delete()
        request.session.flush()
    return redirect('/index/')

def managewl(request):
    if request.session.get('catagory', None) != 'staff':
        return redirect('/login/')
    type_a = Waitlist.objects.filter(catagory='a').all()
    type_b = Waitlist.objects.filter(catagory='b').all()
    type_c = Waitlist.objects.filter(catagory='c').all()
    return render(request, 'login/managewl.html', locals())

def managersv(request):
    if request.session.get('catagory', None) != 'staff':
        return redirect('/login/')
    reservations = Reservation.objects.order_by('-date')
    return render(request, 'login/managersv.html', locals())

def pop_waitlist(request):
    if request.session.get('catagory', None) != 'staff':
        return redirect('/login/')
    id = request.GET.get('id')
    try:
        Waitlist.objects.filter(id=id).delete()
    except:
        pass
    return redirect('/managewl/')

def managetb(request):
    if request.session.get('catagory', None) != 'staff':
        return redirect('/login/')
    tables = Table.objects.order_by('table_id')
    return render(request, 'login/managetb.html', locals())

def change_table(request):
    if request.session.get('catagory', None) != 'staff':
        return redirect('/login/')
    id = request.GET.get('table_id')
    occupied = request.GET.get('occupied')
    # print(id, occupied=='False')
    try:
        if occupied == 'True':
            Table.objects.filter(table_id=id).update(occupied=False)
        else:
            Table.objects.filter(table_id=id).update(occupied=True)
    except Exception as e:
        print(e)
    return redirect('/managetb/')

def menu(request):
    return render(request, 'login/menu.html')

def notfound(request):
    return render(request, 'nofunction.html')

def hash_code(s, salt='ece651'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) 
    return h.hexdigest()