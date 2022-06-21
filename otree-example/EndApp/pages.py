from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from .models import Constants, Player
from ._builtin import Page as oTreePage


class EndPage(Page):
    form_model= Player
    # def before_next_page(self):
    #     self.participant.gender_count_male = self.participant.gender_count_male +1

class RedirectPage(Page):
    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label)}
    form_model = Player

page_sequence = [EndPage,
                RedirectPage]