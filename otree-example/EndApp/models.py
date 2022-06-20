from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random 
import json


author = 'EndApp'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'EndApp'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


    
class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)



class Player(BasePlayer):
    #EndPage
    #group_assignment = models.IntegerField() #the variable we declared on top
    pass
