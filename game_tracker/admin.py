from django.contrib import admin

# Register your models here.
from django.contrib import admin
from game_tracker.Models import *

admin.site.register((Gamer, Log, Game))