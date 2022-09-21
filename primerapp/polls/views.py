from multiprocessing import context
#from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
#from django.template import loader

# Create your views here.
\
"""def index(request):
    return HttpResponse("Hola mundo")"""

class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'questions'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DeatilView(generic.DeleteView):
    model=Question
    template_name= "polls/detail.html"

class ResultView(generic.DeleteView):
    model=Question
    template_name= "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':'No se ha seleccionado ninguna opción'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question_id]))

    seleccionado = str(request.POST['choice'])
    print(seleccionado)
    context = {
        'seleccionado' : seleccionado,
    }
    return render(request, 'polls/vote.html', context )


"""
def detail(request, question_id):
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Esta página de detalle no existe")'''
    question = get_object_or_404(Question, pk=question_id)
    #choices = question.choice_set.all()
    return render(request, 'polls/detail.html', {'question':question} )
    #return HttpResponse("Detail %s" % question_id)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question} )

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
    
    return render(request, 'polls/index.html', context )"""