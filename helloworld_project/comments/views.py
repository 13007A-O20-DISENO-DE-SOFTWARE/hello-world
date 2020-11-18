from django.shortcuts import render

# Create your views here.
def commentsView(request):
    return render(request, 'comments.html', {})