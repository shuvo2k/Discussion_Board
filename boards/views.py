from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User 
from . forms import NewTopicForm
# Create your views here.

def home(request):
	boards = Board.objects.all()
	return render(request, 'includes/home.html', {'boards':boards})


def board_topics(request, pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'includes/topics.html', {'board':board})

def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user =  User.objects.first()

	if request.method == 'POST':
		form = NewTopicForm(request.POST)

		if form.is_valid():
			topic = form.save()
			return redirect('board_topics', pk=board.pk)
	else:
		form = NewTopicForm()

	return render(request, 'includes/new_topic.html', {'board':board,'form':form})

	#return render(request, 'new_topic.html',{'board':board})

