import pickle
import requests
from bs4 import BeautifulSoup as bs
import io


class ScrapeTools:
    @staticmethod
    def dump(obj, path):
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def load(path):
        with open(path, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def renamed_load(path):
        with open(path, 'rb') as file_obj:
            return RenameUnpickler(file_obj).load()

    @staticmethod
    def get_soup(response):
        return bs(response.text, 'html.parser')

    @staticmethod
    def get_new_soup(url):
        response = ScrapeTools.get_response(url)
        return bs(response.text, 'html.parser')

    @staticmethod
    def get_response(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        print(f'requesting page: {url}')
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ScrapeTools.Non200Status(url, response.status_code)
        return response

    class Non200Status(Exception):
        def __init__(self, url, status):
            self.url = url
            self.status = status


class RenameUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        renamed_module = module
        if module == "main":
            renamed_module = "d3scrape.teamandpage"
        return super(RenameUnpickler, self).find_class(renamed_module, name)





    def __str__(self):
        return f"""url: {self.url} responded with {self.status}"""
