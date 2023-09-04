from django.shortcuts import render

def index(request):
 """Landing page"""
 return render(request, 'learning_logs/index.html')