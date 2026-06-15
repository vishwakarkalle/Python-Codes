from django.http import HttpResponse

def home(request):
    return HttpResponse("Coffee & Tea Shop Running Successfully!")