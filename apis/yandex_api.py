import config
import requests


class YandexApi(object):
    # https://geocode-maps.yandex.ru/1.x/?format=json&geocode=4.2756423,52.0993438&lang=en_US
    # geocode = long,lat
    @staticmethod
    def get_geocodes(lat, lng):
        return requests.get(
            "{base_url}".format(base_url=config.settings["api"]["yandex"]["maps"]["base_url"]),
            dict(
                format="json",
                geocode="{lng},{lat}".format(lng=lng, lat=lat),
                lang="en_US",
            )
        ).json()

    @staticmethod
    def get_country_code(yandex_object):
        response = yandex_object.get("response")
        geo_collection = response.get("GeoObjectCollection")
        feature_member = geo_collection.get("featureMember")[0]
        geo = feature_member.get("GeoObject")
        meta_data = geo.get("metaDataProperty")
        geocoder = meta_data.get("GeocoderMetaData")
        address = geocoder.get("Address")
        return False if address.get("country_code") is None else address.get("country_code").lower()

    @staticmethod
    def get_translation(query, target_language, source_language="en"):
        return requests.get(
            "{base_url}".format(base_url=config.settings["api"]["yandex"]["translate"]["base_url"]),
            dict(
                key=config.settings["api"]["yandex"]["api_key"],
                text=query,
                lang="{source}-{target}".format(source=source_language, target=target_language)
            )).json()
