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
    template = loader.get_template('polls/index.html')
    context = {
        'questions' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))