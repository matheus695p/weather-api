import pandas as pd
from src.scraper_module import (ask_google_weather, cities_weather)

# Una sola ciudad
# Santiago
santiago = ask_google_weather(city="Santiago de Chile")
print(santiago)
# hacerlo dataframe
santiago = pd.DataFrame.from_dict(santiago)
print(santiago)

# Varias ciudades al mismo tiempo
cities = ["Santiago de Chile", "Tierra Amarilla Chile", "Coquimbo Chile",
          "Magallanes Chile", "Isla de Pascua Chile", "Lima Peru"]
result = cities_weather(cities)
print(result.to_dict())
