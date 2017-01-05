class Action:
  pass

class ActionHandler():
    from actions.restaurant_search import RestaurantSearch
    from actions.weather_forecast import WeatherForecast
    
    def get_actions():
        actions = {}
        for obj in Action.__subclasses__():
            instance = obj()
            actions[instance.get_name()] = instance
        return actions
