from django.db import models

class Gamer(models.Model):
    Name = models.TextField()

    def __unicode__(self):
        return self.Name
    def __str__(self):
        return unicode(self)