![Build Status](https://www.repostatus.org/badges/latest/active.svg)

#  Weather API's requests

Repo para probar distintas API's que me entreguen la metereología de una zona del país.

# Tree

```sh
│   .gitignore
│   keys.json  --> archivo que solo esta en local con las api keys
│   README.md
│
├───apis
│       weatherstack.py
│
└───images
        weatherstack.png
```

# Weatherstack

<p align="center">
  <img src="./images/weatherstack.png">
</p>


Hay que hacer una cuenta (capa gratuita), entrega 1000 request por mes y lo bueno es que te entrega varios datos climaticos como, descripciones del clima, inclinación del viento, presión atmosferica, precipitaciones, humedad, oclusión en nubes, indice de rayos uv, visibilidad, velocidad del viento, etc. Bien completa la API, pagando 5 dolares al mes, tienes 50000 requests y acceso a info historica. 


```yaml
{'request': {'type': 'City', 'query': 'Santiago, Chile', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Santiago', 'country': 'Chile', 'region': 'Region Metropolitana', 'lat': '-33.450', 'lon': '-70.667', 'timezone_id': 'America/Santiago', 'localtime': '2021-04-11 22:46', 'localtime_epoch': 1618181160, 'utc_offset': '-4.0'}, 'current': {'observation_time': '02:46 AM', 'temperature': 18, 'weather_code': 113, 'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear'], 'wind_speed': 7, 'wind_degree': 180, 'wind_dir': 'S', 'pressure': 1014, 'precip': 0, 'humidity': 37, 'cloudcover': 0, 'feelslike': 18, 'uv_index': 1, 'visibility': 10, 'is_day': 'no'}}

```

# Bibliografía

* [1] https://devresourc.es/
* [2] https://weatherstack.com/
