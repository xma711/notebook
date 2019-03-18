from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for questions whose pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		# note that this checks the function in the model, not in the view
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

# a shortcut function to create question: 
# this will create an object in the current database - may not be a good idea
# however, it seems that it will create a new table for this model, and then it will remove it later.. 
# is it possible? seems Question.objects.create() makes use of the common function, not test-specific function
# it turns out that indeed the objects created in the test environment are not saved in the database at the end.
# this is really interesting...
# in fact, after running test, the screen says: Destroying test database for alias 'default'...
# which means that it does create a database, but it will destroy at the end
def create_question(question_text, days):
	"""
	create a question with the given 'question_text' and published 
	the given number of 'days' offset to now (negative for questions published
	in the past, positive for questions that have yet to be published).
	"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

# now we are going to test the view...
# basically we will get the response and then analyze if the response is what is expected
class QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		"""
		if no question exist, an appropriate message is displayed.
		"""
		# client variable exists in every TestCase
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		# what if the existing database has something inside??
		self.assertContains(response, "No polls are available.")
		# following is a powerful feature - it can extract the latest_question_list for the response!
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_past_question(self):
		"""
		question with a pub_date in the past are displayed on the index page
		"""
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
		)

	def test_future_question(self):
		"""
		questions with a pub_date in the future are not displayed on the index page.
		"""
		create_question(question_text = "Future question", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])


	def test_future_question_and_past_question(self):
		"""
		even if both past and future question exist, only past questions are displayed.
		"""
		create_question(question_text = "Past question.", days = -30)
		create_question(question_text = "Future question.", days = 30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
		)

	def test_two_past_questions(self):
		"""
		the questions index page may display multiple questions
		"""
		create_question(question_text = "Past question 1.", days=-30)
		create_question(question_text = "Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question 2.>', '<Question: Past question 1.>']
		)

class QuestionDetailViewTests(TestCase):
	def test_future_quetion(self):
		"""
		the detail view of a question with a pub_date in the future returns a 404 not found.
		"""
		future_question = create_question(question_text = 'Future question.', days=5)
		url = reverse('polls:detail', args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		"""
		the detail view of a question with a pub_date in the past displays the question's text.
		"""
		past_question = create_question(question_text='Past Question.', days = -5)
		url = reverse('polls:detail', args=(past_question.id,))
		response = self.client.get(url)
		self.assertContains(response, past_question.question_text)