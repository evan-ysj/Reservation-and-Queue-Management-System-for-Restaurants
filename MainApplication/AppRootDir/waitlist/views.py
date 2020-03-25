from django.shortcuts import render, redirect
from .forms import TakenoForm, CheckstateForm
from . import models
from django.db.models import Max

# Create your views here.

def takeno(request):
    if request.method == 'POST':
        message = ''
        waitlist_form = TakenoForm(request.POST)
        if waitlist_form.is_valid():
            no_of_guests = waitlist_form.cleaned_data['no_of_guests']
            lastname = waitlist_form.cleaned_data['name']
            id = 0
            catagory = ''
            try:
                if no_of_guests <= 4:
                    if models.Waitlist.objects.count():
                        id = models.Waitlist.objects.aggregate(Max('id'))['id__max'] + 1
                        
                    catagory = 'a'
                elif no_of_guests <= 6:
                    if models.Waitlist.objects.count():
                        id = models.Waitlist.objects.aggregate(Max('id'))['id__max'] + 1
                    catagory = 'b'
                else:
                    if models.Waitlist.objects.count():
                        id = models.Waitlist.objects.aggregate(Max('id'))['id__max'] + 1
                    catagory = 'c'
                request.session['number'] = catagory + str(id)
                new_wl = models.Waitlist.objects.create(
                        id = id,
                        guests = no_of_guests,
                        lastname = lastname,
                        catagory = catagory
                    )
                new_wl.save()
                getrank(request, catagory, id)
                return redirect('/takesuccess/')
            except Exception as e:
                print(e)
                message = "Sorry, something went wrong. Please try again!"
                return render(request, 'takeno.html', locals())
    waitlist_form = TakenoForm()
    return render(request, 'takeno.html', locals())

def takesuccess(request):
    if not request.session.get('number', None):
        return redirect('/takeno/')
    return render(request, 'takesuccess.html', locals())

def checkstate(request):
    if request.method == 'POST':
        checkstate_form = CheckstateForm(request.POST)
        result = -1
        message = ''
        if checkstate_form.is_valid():
            number = checkstate_form.cleaned_data['number']
            try:
                catagory = number[0]
                id = int(number[1:])
                cur = models.Waitlist.objects.filter(catagory=catagory).get(id=id)
                if not cur:
                    message = "Invalid number!"
                    return render(request, 'checkstate.html', locals()) 
                result = getrank(request, catagory, id)
                return render(request, 'checkstate.html', locals())
            except:
                message = "Invalid number!"
                return render(request, 'checkstate.html', locals()) 
        else:
            message = "Please check the input!"   
            return render(request, 'checkstate.html', locals()) 
    checkstate_form = CheckstateForm()
    return render(request, 'checkstate.html', locals())

def getrank(request, catagory, id):
    request.session['rank'] = models.Waitlist.objects.filter(catagory=catagory, id__lt=id).count()
    return request.session['rank']