from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *


# Create your views here.
def index(request):
    boards = {'boards': Board.objects.all()}

    if boards is not None:
        return render(request, 'list.html', boards)
    else:
        return render(request, 'list.html')
    # return render(request, 'list.html')

def post(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')
