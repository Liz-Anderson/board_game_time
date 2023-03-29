from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# class PlayerNum(models.Model):
#     number_player = models.IntegerField()

#     def __str__(self):
#         return self.number_player

class Game(models.Model):

    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField(blank=True)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    # num_players = models.ManyToManyField(PlayerNum, related_name='player_counts')
    min_age = models.IntegerField()
    rules = models.URLField()
    notes = models.TextField(blank=True)
    owned_by = models.ManyToManyField(get_user_model(), related_name='owned', blank=True)
    wish_list = models.ManyToManyField(get_user_model(), related_name='wishlist', blank=True)

    def __str__(self):
        return self.name
