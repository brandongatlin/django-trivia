from django.shortcuts import render
from .models import Question
from django.db import connection
from random import randint, shuffle
from pprint import PrettyPrinter


def index(request):
    return render(request, 'game/index.html')

def gameboard(request, category_id=1):
    pp = PrettyPrinter(indent=4)

    base_q = Question.objects.filter(category=category_id)
    count = base_q.count()
    limit = 5
    offset = randint(0, count - 1)
    if offset > count - limit:
        offset = count - limit
    questions = base_q.order_by('id')[offset:offset+limit].values()
    questions = list(questions)
    shuffle(questions)
    for dict in questions:
        pp.pprint(dict)
    return render(request, 'game/gameboard.html', {'questions': questions})


def gameover(request):
    return render(request, 'game/gameover.html')