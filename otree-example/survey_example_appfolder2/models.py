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
from HelperFunctions import random_number


author = 'survey_example_appfolder2'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

    
class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass