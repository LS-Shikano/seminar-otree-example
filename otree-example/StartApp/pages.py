from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 


from survey_example_appfolder2.HelperFunctions import detect_screenout, detect_quota


from ._builtin import Page as oTreePage
import json
import random
from otree.lookup import url_i_should_be_on, get_page_lookup, get_min_idx_for_app


class Page(oTreePage):
    def post(self):
        r = super().post()
        current_app = self._lookup.app_name
        try:
            next_app = get_page_lookup(self.session.code, self.participant._index_in_pages).app_name
        except KeyError:
            # in this case it's apparently the last app in the original app_sequence
            next_app = None
        if current_app == next_app:
            return r
        seq_dict = self.participant.vars.get('_updated_seq_apps')
        if seq_dict:
            app_to_skip_to = seq_dict.get(current_app)
            if app_to_skip_to:
                where_to = get_min_idx_for_app(self.participant._session_code, app_to_skip_to)
            else:
                where_to = self.participant._max_page_index + 1
            self.participant._index_in_pages = where_to
            self._is_frozen = False
            self._index_in_pages = where_to
            return self._redirect_to_page_the_user_should_be_on()
        else:
            return r



class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width', 'entry_question', 'eligible_question']
    




#with the function before_next_page you can can control what should happen. It is a nice feature for filtering
#or also setting variables
    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1

#we want to detect all the screenouts and the quota reached right away
        detect_screenout(self)
        detect_quota(self)


class DemoPage(Page):
    form_model = Player
    form_fields = ['age_question', 'gender', 'hidden_input']

    def before_next_page(self):
        self.participant.gender = 'hello'


    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label),
                'screenout': safe_json(self.player.screenout),
                'quota': safe_json(self.player.quota)
                }

class Html_overview(Page):
    form_model = Player

    def is_displayed(self):
        '''this is another otree specific function that regulates if a page is displayed or not '''
        #this will show the page to anybody who has the right assignment so in this case 
        return self.player.group_assignment == 1

class PopoutPage(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout'] #'gender' needed here?

class EndPage(Page):
    def vars_for_template(self):
        '''this is another function by otree which allows you to "send" variables
        to html files if you need to access them from there'''
        return {"group_assignment": safe_json(self.player.group_assignment)}

class RedirectPage(Page):
    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label)}
    

    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                Html_overview,
                PopoutPage,
                EndPage,
                RedirectPage]