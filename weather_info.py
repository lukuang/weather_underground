"""
get weather information about one place
"""

import os
import json
import sys
import re
from myUtility.rest import Rest
from country_code import Country_Code, resource_filename


class Weather_info(Rest):
    def __init__(self):
        self._country_code_finder = Country_Code()
        self._key = self.read_key()
        self._COMMON_END_POINT = 'http://api.wunderground.com/api/'+self._key +'/'

    
    def find_country_code(self,name):
        return  self._country_code_finder.get_country_code(name)

    @staticmethod
    def read_key():
        key_file_path = resource_filename('weather_underground', "key")
        key = ""
        try:
            with open(key_file_path) as f:
                key = f.read()
        except IOError:
            raise NoKeyFileException(key_file_path)
        else:
            return key


    def find_city(self,city,country=None):
        end_point = 'http://autocomplete.wunderground.com/aq?'
        para = {
            'query': city
        }
        if not country:
            code = self.find_country_code(country)
            para['c'] = code
        content = self.call_api(para,end_point)
        print content
        # TODO: add utility to choose city, and then call the api to get forcast



    def get_10dayforcast_for_link(self,link):
        end_point = self._COMMON_END_POINT +'forecast10day/' + link + '.json'
        content = self.call_api({},end_point)
        print content


    def get_10dayforcast(self,country,city):
        end_point = self._COMMON_END_POINT +'forecast10day/q/' + country+'/'+city + '.json'
        content = self.call_api({},end_point)
        print content
        return content


    # def get_forcast(self, ):






