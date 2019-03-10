from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# from django.template import loader

# Create your views here.

from django.http import HttpResponse

# note that this is list view
# list view is the concept of displaying a list of objects
class IndexView(generic.ListView):
	# if i don't specify a template name, the default name will be polls/question_list.html
	template_name = 'polls/index.html'
	# by default the context_object_name in template is "question_list", but we can override it 
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
			Return the last five published questions 
			(not including those set to be published in the future).
		"""
		queryset = Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]
#		print (queryset.query) # this is to print the sql command; but better to see this from logging, set in setting.py
		return queryset
		#return Question.objects.order_by('-pub_date')[:5]
# old style:
#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#	# context is a dictionary mapping template variable names to python objects
#	context = {
#		'latest_question_list': latest_question_list,
#	}
#
#	return render(request, 'polls/index.html', context) # a shortcut compared to the line above


# note that this is detail view.
# detail view is displaying a detail page for a particular type of object.
# detail view expects the primary key value captured from the url to be called 'pk'.
class DetailView(generic.DetailView):
	# i think the model will tell this function which model to get the object from, based on pk
	model = Question
	# and then by default, the object will be passed into the template.
	# how the template will use this object is not this function's business
	# if i don't specify the template name, the default template name will be "polls/question_detail.html"
	template_name = 'polls/detail.html'

	# because we only want to display questions have the timestamp <= now, we need to filter the question
	# wait.. is this make django less efficient by calling the sql to get the queryset first, as what we really want is only 1 object..
	# i think maybe later the whole sql command will be combined by django
	def get_queryset(self):
		"""
		excludes any questions that aren't published yet
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

# old style: 
#def detail(request, question_id):
#	# instead of raise http404 in a separate step, we can do it at one go with the getting object
#	question = get_object_or_404 (Question, pk=question_id)
#
#	return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404 (Question, pk=question_id)
	try:
		# note that 'choice' is specified as the name in the form in detail.html;
		# request.POST is a dictionary-like object.
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the question voting form, i.e. the detail form
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		# remember to save to database
		selected_choice.save()

		# always return an HttpResponseRedirect after successfully dealing 
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button
		# obviously, the reverse() function acts the same as the {% url %} method in template
		return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )
