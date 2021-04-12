import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup


def ask_google_weather(city="Santiago"):
    """
    Scrapper una pregunta en google rápida, que devuelva un HTML como
    respuesta
    Parameters
    ----------
    city : string, optional
        Ciudad a saber el clima. The default is "Tiempo en Santiago".
    Returns
    -------
    dict_ : dict
        diccionario con la respuesta.

    """

    # url donde ir a buscar la info de google
    url = "https://www.google.com/search?q=" + "Tiempo en " + city
    print(url)
    # hacer request de html
    HTML = requests.get(url)
    # parsear html
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # encontrar el div que tenga el precio
    temperature = soup.find("div",
                            attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find(
        "div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    print(temperature)
    content = soup.find("div",
                        attrs={'class': 'BNeawe tAd8D AP7Wnd'}).find(
        "div", attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    print(content)
    date, comments = content.split("\n")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # diccionario a sacar
    dict_ = {
        "ciudad": [city],
        "fecha": [date],
        "temperatura": [temperature],
        "comentario": [comments]
    }
    return dict_


def cities_weather(cities):
    """
    Scrapper tiempo de varias ciudades a la vez y devolver un dataframe
    con la info

    Parameters
    ----------
    cities : list
        Lista de ciudades.

    Returns
    -------
    result : dataframe
        Dataframe con la temperatura, comentario y fecha de la consulta para
        cada ciudad.

    """
    result = pd.DataFrame()
    for city in cities:
        print(city)
        weather = ask_google_weather(city=city)
        weather = pd.DataFrame.from_dict(weather)
        result = pd.concat([result, weather], axis=0)
    result.reset_index(drop=True, inplace=True)
    return result
