from django.shortcuts import render_to_response
from django.template import RequestContext
from game_tracker.Models import *


def index(request):
    if request.method == "GET":
        return indexGet(request)
    elif request.method == "POST":
        return indexPost(request)

def indexGet(request):
    Logs = Log.objects.all()
    return render_to_response("index.html", {"Logs": Logs}, context_instance=RequestContext(request))

def indexPost(request):
    try:
        log = Log()

        game = Game.objects.filter(Name=request.POST['game'])
        if game:
            if len(game) == 1:
                log.Game = game[0]
            else:
                raise IOError("No winner specified")
        else:
            game = Game(Name=request.POST['game'], Type=0)
            game.save()
            log.Game = game

        user = Gamer.objects.filter(Name=request.POST['winner'])
        if user:
            if len(user) == 1:
                log.Winner = user[0]
            else:
                raise IOError("No winner specified")
        else:
            user = Gamer(Name=request.POST['winner'])
            user.save()
            log.Winner = user

        points = request.POST['points']

        #log.Losers = []
        log.WinnerScore = points
        log.save()

        return render_to_response("index.html", context_instance=RequestContext(request))
    except Exception as e:
        return render_to_response("error.html", {"exception" : e.message}, context_instance=RequestContext(request))