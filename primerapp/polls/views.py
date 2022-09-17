from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.

"""def index(request):
    return HttpResponse("Hola mundo")"""


def detail(request, question_id):
    return HttpResponse("Detail %s" % question_id)
    
def results(request, question_id):
    response = "Results %s" 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote %s" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    context = {
        'questions' : latest_question_list,
    }


    #Lo que aparece comentado es una forma de crear un render de un template
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request))
    
    return render(request, 'polls/index.html', context )