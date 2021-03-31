from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models import SET_NULL


# Create your models here.
ISSUE_STATUS_CHOICES = (
    ('new', 'New'),
    ('accepted', 'Accepted'),
    ('reviewed','Reviewed'),
    ('started', 'Started'),
    ('closed', 'Closed')
)

class Issue(models.Model):
    # owner wil be a foreign key ro the User model wich is already build in Django
    owner = models.ForeignKey(User,null=True,blank=True,on_delete=SET_NULL)
    # multichoice with defaulting to "new"
    status = models.CharField(max_length=25,choices=ISSUE_STATUS_CHOICES,default='new')
    summary = models.TextField()
    # date time field witch will be set to the date time when the record is created
    opened_on = models.DateTimeField('date_ opened', auto_now=True)

    def name(self):
        return self.summary.split('\n',1)[0]

