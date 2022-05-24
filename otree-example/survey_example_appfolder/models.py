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

#this is where we would import andy extra functions or packages we need from python
import random 

author = 'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        '''this is a function by otree (same can not be changed)
        which is creating a new subsession. Any variables that are needed to be custom
        (so declaring it in a different way before) are created here'''
        for p in self.get_players():
            #here we want to declare the players to different groups (2 in total)
            #we use a python function here from 'random' we imported earlier
            p.group_assignment = random.Random().randint(0, 1)
    
class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)
    #this is how you can implement variables that can be used by every player
    #they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    group_assignment = models.IntegerField() #the variable we declared on top
    entry_question = models.StringField(blank = True) #this is an optional field through blank = True
    age_question = models.IntegerField(max=110, min=1)  #we can also have max and min guidelines
    gender = models.IntegerField(initial=-999, label='Gender Question')  #we can add an initial value or a different label
    hidden_input = models.IntegerField(initial=50, blank=True)
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')


    #custom error message
        #has to: 
        #1) be in the class Player (important to indent the right way)
        #2) have a specific name "variablename"_error_message
    def age_question_error_message(player, value):
        if value > 50:
            return 'You are too old. Are you sure you are taking this course?'
                        