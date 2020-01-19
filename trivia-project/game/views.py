from django.shortcuts import render
from .models import Question, Score
from django.db import connection
from random import randint, shuffle


def index(request):
    top_five = Score.objects.order_by('-score')[:5].values()
    top_five = list(top_five)
    return render(request, 'game/index.html', {'top_five': top_five})

def gameboard(request, category_id=1):
    base_q = Question.objects.filter(category=category_id)
    count = base_q.count()
    limit = 5
    offset = randint(0, count - 1)
    if offset > count - limit:
        offset = count - limit
    questions = base_q.order_by('id')[offset:offset+limit].values()
    questions = list(questions)
    shuffle(questions)
    return render(request, 'game/gameboard.html', {'questions': questions})

def gameover(request):
    return render(request, 'game/gameover.html')