from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

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
    # get_object_or_404 tries first to query the instances off a Model, but if it fails then it catches
    # the 404 error and returns it

    # pk is the primary key, which by default is set to the id assigned for each instance of a unique Model
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Seeks out a form POST request that was made to the votes view with an element of 'name'
        # "choice". It then pulls the 'id' off the element and sets that to 'pk'.
        # i.e. the input radio has name="choice" and id="{{choice.id}}", so pk="{{choice_id}}"
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # KeyError is brought up if the 'key' requested in POST is not in the form, and Choice.DoesNotExist
    # is brought up if the 'id' that the 'key' links to does not exist as a Choice model instance id (>=1)
    except (KeyError, Choice.DoesNotExist):
        # If there is an error with requesting from the form POST request (i.e. user does not select
        # a radio button before clicking submit), then display an error message and let the user
        # select a new option
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a choice",
        })
    else:
        # if the try works...
        selected_choice.votes += 1      # increment the votes for the current choice
        selected_choice.save()          # save the modified Choice model instance to the database

        # The reverse() function finds the route to redirect to by searching for the namespace (i.e. 'polls'),
        # going to the namespaces' urls.py, and then finding the url with the name of the view (i.e. 'results').
        # Once it finds the name, it looks at the route associated with the 'namespace:view', makes sure that
        # any parameters are fulfilled in the reverse() call (i.e. question.id) and then inserts the parameters
        # (if any) into the route. The reverse() function then returns the full route for HttpResponseRedirect to
        # redirect the user to.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))