from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# this is for adding choice to a question
class ChoiceInline(admin.TabularInline):
	model = Choice
	# the extra is that besides the existing choices, there will be extra empty slots for admin to add choices
	extra = 3

# this class will be passed into the admin.site.register() function
# in this particular case, the order of display will be pub_date and then question_text (default behaviour is the other way)
class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text'] # this changes the order of display of fields

	# for fieldsets, the first element in each tuple is the title of the fieldset, 
	# while the 2nd is the list of fields under this title
	fieldsets = [
		(None, 			{'fields': ['question_text']}),
		('Date information', 	{'fields': ['pub_date']})
	]
	# this tells Django that Choice objects are edited on the Question admin page;
	# by default provide enough fields for 3 choices
	inlines = [ChoiceInline]

	# this controls what to display on the list of questions
	# interestingly, even the method can be added here..
	list_display = ('question_text', 'pub_date', 'was_published_recently')

	list_filter = ['pub_date']

	search_fields = ['question_text']

#admin.site.register(Question) # this uses the default admin view
admin.site.register(Question, QuestionAdmin)

# not register choice because it is better to create choices from Question
# admin.site.register(Choice)

