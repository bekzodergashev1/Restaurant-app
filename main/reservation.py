from .models import *

def commentariya(request):
    reservation=Reservations.objects.all()
    return {'reservation.html', reservation}