from django.shortcuts import render,redirect
from . import models
from .forms import ReservationForm
import datetime

# Create your views here.
def booktable(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        message = 'Please check the input fields!'
        username = request.session['user_name']
        if reservation_form.is_valid():
            no_of_guests = reservation_form.cleaned_data['no_of_guests']
            bookdate = reservation_form.cleaned_data['bookdate']
            if bookdate < datetime.date.today():
                message = 'Please select a date that is later than today.'
                return render(request, 'booktable.html', locals())
            previous = models.Reservation.objects.filter(user=username, date=bookdate)
            if previous:
                message = 'You have already booked a table on that day. Please pick another date.'
                return render(request, 'booktable.html', locals())
            try:
                reserved = models.Reservation.objects.filter(date=bookdate).values('table_id')
                allocate = models.Table.objects.filter(cap__gte=no_of_guests).exclude(table_id__in=reserved).first()
                #print(allocate)
                if allocate:
                    new_rsv = models.Reservation.objects.create(
                        table_id = allocate,
                        no_of_guests = no_of_guests,
                        user = request.session['user_name'],
                        date = bookdate,
                        expired = False
                    )
                    new_rsv.save()
                    return redirect('/booksuccess/')
                else:
                    message = 'Selected date is fully booked. Please pick another day.'
                    return render(request, 'booktable.html', locals())
            except Exception as e:
                #print(e)
                message = 'Book table failed. Please check the input fields!'
                return render(request, 'booktable.html', locals())
    reservation_form = ReservationForm()
    return render(request, 'booktable.html', locals())

def booksuccess(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'booksuccess.html', locals())

def checkrev(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    username = request.session['user_name']
    reservations = models.Reservation.objects.filter(user=username).all()
    return render(request, 'checkrev.html', locals())