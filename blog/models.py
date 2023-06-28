from django.db import models

# Create your models here.
class Blog(models.Model):
    # set title with maximum length 100
    title = models.CharField(max_length=200)
    # set description with max 250 characters
    description = models.TextField()
    # set date
    date = models.DateField()

    def __str__(self):
        # this is class property so does not need to
        # run migration because this does not do anything
        # with database
        return self.title



