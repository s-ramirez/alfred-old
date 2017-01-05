import requests
from actions.handler import Action

class RestaurantSearch(Action):
    def get_name(self):
        return "restaurant_search"

    def respond(self, settings, context):
        return "Are you sure you don't want tacos?"
