from django.db import models
from django.db import models

class FeelingChoice(models.IntegerChoices):
    REJECT = 5, 'Rejected'
    UNKNOWN = 6, 'Unknown'
    VERYBAD = 10, 'Very Bad'
    BAD = 15, 'Bad'
    OKAY = 20, 'Okay'
    GOOD = 25, 'Good'
    GOOD_SUSPENDED_DUE_TO_OTHER_OFFER = 27, 'Good, but suspended due to other offer'
    VERYGOOD = 30, 'Very Good'
    OFFER = 100, 'Offer'


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='Open')
    last_contact = models.DateField(null=True, blank=True)
    feeling = models.IntegerField(choices=FeelingChoice.choices, default=FeelingChoice.UNKNOWN)

    def __str__(self):
        return self.title + ' - ' + self.short_description

    @property
    def short_description(self):
        MAX_SIZE = 60
        return self.description[:MAX_SIZE] + ("..." if len(self.description) > MAX_SIZE else "")
