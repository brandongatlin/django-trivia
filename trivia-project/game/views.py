from django.shortcuts import render
from .models import Question, Score, Category
from django.db import connection
from random import randint, shuffle


def index(request):
    top_five = Score.objects.order_by('-score')[:5].values()
    top_five = list(top_five)
    categories = Category.objects.all().values()
    categories = list(categories)
    title = 'Trivia Game'
    return render(request, 'game/index.html', {'title': title, 'top_five': top_five, 'categories': categories})
        
def gameboard(request):
    if request.method == 'POST':
        categories = Category.objects.all().values()
        categories = list(categories)
        player_name = request.POST['name']
        category_data = request.POST['category']
        category_id = category_data.split(None, 1)[0]
        category = category_data.split(None, 1)[1]
        print(category_id, category)
        if category == 'Random':
            print('random selected')
            category_id = categories[randint(0, len(categories) - 1)]['id']
        base_q = Question.objects.filter(category=category_id)
        count = base_q.count()
        limit = 5
        offset = randint(0, count - 1)
        if offset > count - limit:
            offset = count - limit
        questions = base_q.order_by('id')[offset:offset+limit].values()
        questions = list(questions)
        shuffle(questions)
        for idx, q in enumerate(questions, start=0):
            questions[idx]['index'] = idx

        request.session['questions'] = questions            
        title = 'Trivia Game'
    return render(request, 'game/gameboard.html', {'title': title, 'questions': questions})

def gameover(request):
    right_answers = 0
    idx = 0
    questions = request.session['questions']
    print(questions)
    if request.method == 'POST':
        answers = request.POST.copy()
        print(answers)

        for dict in questions:
            right = dict['answer']
            choice = answers[str(idx)]
            print(right, choice)
            idx += 1
            if choice == right:
                right_answers += 1
    print(right_answers)
    return render(request, 'game/gameover.html')

