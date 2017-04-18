from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
# A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response.
# A view is a "type" of Web page in your Django application that generally serves a specific function and has a
# specific template.

from .models import Question


def index(request):
    # make list of most recent questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # load template
    template = loader.get_template('polls/index.html')
    # set context variables for template
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # this could be replaced with:
    #    question = get_object_or_404(Question, pk=question_id)
    #    return render(request, 'polls/detail.html', {'question': question})
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(loader.get_template('polls/detail.html').render(
        context={'question': question},
        request=request)
    )


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

