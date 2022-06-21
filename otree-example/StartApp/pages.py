from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 


# from HelperFunctions import detect_screenout, detect_quota


from ._builtin import Page as oTreePage
import json
import random
from otree.lookup import url_i_should_be_on, get_page_lookup, get_min_idx_for_app


class Page(oTreePage):
    def post(self):
        '''randomization'''
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



#Welcome Page for explaination of the survey and catching the metadata
class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width']

#Page to ask about our quota
class QuotaQuestions(Page):
    form_model = Player
    form_fields = ['age', 'gender', 'federalstate']
    
    def before_next_page(self):
        # detect_screenout(self)
        # detect_quota(self)
        pass

#Page used for redirecting and otherwise text to guide them to the first survey
class RedirectPage(Page):
    form_model = Player
    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label)}
    
page_sequence = [Welcome,
                QuotaQuestions,
                RedirectPage]