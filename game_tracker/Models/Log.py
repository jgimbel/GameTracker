from django.db import models

from game_tracker.Models.Users import Gamer
from game_tracker.Models.Games import Game


class Log(models.Model):
    Winner = models.ForeignKey(Gamer)
    #Losers = models.ForeignKey(Gamer)
    DatePlayed = models.DateTimeField(auto_now_add=True)
    Game = models.ForeignKey(Game)
    WinnerScore = models.IntegerField()

    def __unicode__(self):
        return "Winner: %s scored %s in the game %s on %s" % (self.Winner, self.WinnerScore, self.Game, str(self.DatePlayed.strftime("%Y-%m-%d")))
    def __str__(self):
        return str(unicode(self))
