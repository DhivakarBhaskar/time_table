from django.shortcuts import render

def home(request):
    return render(request, 'timetable.html')

# Create your views here.
