__author__ = 'joel'
from game_tracker.Models.Enumerations import Games
from django.db import models
class Game(models.Model):
    Name = models.TextField()
    Type = models.IntegerField()

    def __unicode__(self):
        return self.Name + "(" + Games(self.Type).name+ ")"
    def __str__(self):
        return unicode(self)