from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model= Choice
    extra= 1


class QuestionAdmin(admin.ModelAdmin):
    #fields= ['pub_date', 'question_text']
    list_display = ('question_text','pub_date')
    list_filter= ['pub_date']
    search_fields= ['question_text']
    fieldsets = [
        (None, { 'fields' : ['question_text']}),
        ('Fecha', { 'fields' : ['pub_date']})

    ]
    inlines= [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)