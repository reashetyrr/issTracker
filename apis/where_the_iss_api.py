import config
import requests


class WhereTheIssApi(object):
    @staticmethod
    def get_sattelite(satellite=25544):
        return requests.get("{base_url}/satellites/{satellite}".format(base_url=config.settings["api"]["where_the_iss"]["base_url"], satellite=satellite)).json()
