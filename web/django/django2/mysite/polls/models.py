import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# just imagine one object of each class will be a row in the table
class Question(models.Model):
	# there are 2 columns in the table
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= now - datetime.timedelta(days = 1)

	# follows control the 'was_published_recently' field in the admin page

	# when click this column in admin page, sort using pub_date
	was_published_recently.admin_order_field = 'pub_date' 

	# let django admin konw it is a boolean value 
	# and it displays a green tick and red cross, which makes it look nicer
	was_published_recently.boolean = True 

	# let admin page to display this instead of the value name
	was_published_recently.short_description = 'Published recently?' 

class Choice(models.Model):
	# the 'question' field will be the type Question defined by the class Question above, and the value will be one of the existing values in the database
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	answer = models.IntegerField(default = 0)
