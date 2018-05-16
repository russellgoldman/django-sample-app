from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


# FOREIGN KEY USAGE
# ------------------
# Since our Choice model is associated with the Question model as a Foreign Key,
# each Choice instance must be created under a Question instance

# e.g.
#      q = Question(question_text = "What's your name", pub_date = timezone.now())
#      q.choice_set.create(choice_text = "bob", votes = 0)
#      q.choice_set.all()       // lists all Choice instances under the Question instance q
#      q.save()                 // saves the Question instance and all Choice instances under it to the database

class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    # reference to the Question model (each choice has an associated Question)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text