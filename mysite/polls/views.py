from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

# Create your views here.


def index(request):
    # Question.objects.order_by() returns a QuerySet object containing the Question instances
    # '-pub_date' selects by publication date
    # [:5] tells Django to select the objects from 0 to 5 (first 5 objects) from the query
    # If we did [5:], this would tell us to select all objects (including and after) the 5th index in the QuerySet
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # For each Question instance in latest_question_list, extract each instances question_text attribute
    # and separate them by a comma (except for the last item)
    # e.g. output = ', '.join(q.question_text for q in latest_question_list)

    context = {'latest_question_list': latest_question_list}

    # rendering our output to the page by passing in our HTML file and our required parameters as context
    return render(request, 'polls/index.html', context)


# whatever value is in <int:question_id> in the route will be the value stored in question_id below
def detail(request, question_id):
    # rendering text with a parameter
    return HttpResponse("This is the detail view of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)