from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.urls import reverse

# Create your views here.
# A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response.
# A view is a "type" of Web page in your Django application that generally serves a specific function and has a
# specific template.

from .models import Choice, Question


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
        request=request,
        context={'question': question})
    )


def results(request, question_id):
    # get the question if exists, else 404 error
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name='polls/results.html', context={'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # access submitted data from POST form methods by key name from request.POST
        # FIXME: accessing shared data, but not automatically thread safe
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form if valid choice was submitted
        return render(request, template_name='polls/detail.html', context={
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # reverse() helps avoid having to hardcode a URL in a view function. It is given the name of the view that
        # we want to pass control to and the variable portion of the URL pattern that points to that view
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

