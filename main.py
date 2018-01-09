from apis.where_the_iss_api import WhereTheIssApi
from apis.yandex_api import YandexApi
from random import choice
import config
from time import sleep


def execute(iss, yandex):
    satellite_info = iss.get_sattelite(satellite=25544)
    iss_geocode_info = yandex.get_geocodes(lat=satellite_info["latitude"], lng=satellite_info["longitude"])
    random_word = choice(config.words)
    country_code = yandex.get_country_code(yandex_object=iss_geocode_info)
    if(country_code is not False):
        translated_word = yandex.get_translation(query=random_word,
                                             target_language=country_code)

    print "now sleeping for %r seconds" % config.settings.get("time").get("interval")
    sleep(config.settings.get("time").get("interval"))


if __name__ == "__main__":
    execute(
        iss=WhereTheIssApi(),
        yandex=YandexApi(),
    )
