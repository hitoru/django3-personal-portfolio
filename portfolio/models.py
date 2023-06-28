from django.db import models

# Create your models here.
class Project(models.Model):
    # set title with maximum length 100
    title = models.CharField(max_length=100)
    # set description with max 250 characters
    description = models.CharField(max_length=250)
    # set image with upload directory path
    image = models.ImageField(upload_to='portfolio/images/')
    # set URL with allowing blank url, image need pillow packages
    url = models.URLField(blank=True)

    def __str__(self):
        # this is class property so does not need to
        # run migration because this does not do anything
        # with database
        return self.title

    




