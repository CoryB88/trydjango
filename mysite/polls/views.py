from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/templates/polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls\detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(results, question_id):
    return HttpResponse("You're voting on question %s" % question_id)