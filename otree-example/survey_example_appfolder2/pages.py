from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from .models import Constants, Player




class PopoutPage(Page):
    form_model = Player
    form_fields = []

page_sequence = [PopoutPage]