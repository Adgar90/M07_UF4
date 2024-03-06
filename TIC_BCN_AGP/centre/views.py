from django.shortcuts import render
# Index view

def index(request):
    return render(request, 'index.html')
