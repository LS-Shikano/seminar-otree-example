import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number



def counting(self):
    '''here we count the quota once the survey'''

#gender detection
    if self.player.gender == 1:
        print('gender is 1')
        self.session.vars['gender'] == 1
        

# def detect_quota(self):
#     '''this function will check if a quota is already filled'''
#     participant_number = self.group.counter
#     #declare quota reached if we have more than 1 participant that started
#     if participant_number > 10:
#         self.player.quota = 1
#     return None

