from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
from django.views import generic
import logging
logger = logging.getLogger(__name__)
# from .forms import VoteForm
# Create your views here.

# def index(request):
#   latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#   context = {'latest_question_list': latest_question_list}
#   return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'
  def get_queryset(self):
    return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'
  context = 'question'


class VoteView(generic.View):
  def post(self, request, question_id):
    logger.debug("vote().question.id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
      return render(request, 'polls/detail.html', {
        'question':question,
        'error_message': "You didn't select a choice"
      })
    else:
      logger.debug("vote().selected_choice.choice_text: %s" % selected_choice.choice_text)
      selected_choice.votes+=1
      selected_choice.save()
      return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
# def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError, Choice.DoesNotExist):
#     return render(request, 'polls/details.html', {
#       'question':question,
#       'error_message': "You didn't select a choice"
#     })
#   else:
#     selected_choice.votes+=1
#     selected_choice.save()

#     return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

# def result(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/result.html', {'question':question})

class ResultView(generic.DetailView):
  model = Question
  template_name = 'polls/result.html'