from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from .models import Constants, Player

class DemoPage(Page):
    form_model = Player
    form_fields = ['age_question', 'gender', 'hidden_input']

page_sequence = [DemoPage]