class Action:
  def get_entity_type(context, t):
      if(len(context['entities']) > 0):
          for entity in context['entities']:
              if(entity['entity'] == t):
                  return entity
      return None

class ActionHandler():
    from actions.restaurant_search import RestaurantSearch
    from actions.weather_forecast import WeatherForecast

    def get_actions():
        actions = {}
        for obj in Action.__subclasses__():
            instance = obj()
            actions[instance.get_name()] = instance
        return actions
