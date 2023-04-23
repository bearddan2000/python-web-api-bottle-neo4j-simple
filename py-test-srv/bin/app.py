import requests
import testify

from consts.smoke.const import *
from consts.get.const import *
from consts.filter.const import *

def fun_call(url: str, fun):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    return fun(url, headers=headers)

def assert_url(url: str, fun_ptr):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr)

    testify.assert_equal(resp.status_code, 200)

    return 0

class TestSmoke(testify.TestCase):
    """docstring for TestSmoke."""

    def test_smoke_url(self):
        return assert_url(SMOKE_URL, requests.get)

    def test_smoke_output(self):
        resp = fun_call(SMOKE_URL, requests.get)
        testify.assert_equal(resp.json(), SMOKE)

class TestGet(testify.TestCase):
    """docstring for TestGet."""    

    def test_get_all_url(self):
        return assert_url(GET_ALL_URL, requests.get)
    
    def test_get_all_output(self):
        resp = fun_call(GET_ALL_URL, requests.get)
        testify.assert_equal(resp.json(), GET_ALL)

class TestFilterByName(testify.TestCase):
    """docstring for TestFilterByName."""    

    def test_filter_name_url(self):
        return assert_url(FILTER_BY_NAME_URL, requests.get)
    
    def test_filter_name_output(self):
        resp = fun_call(FILTER_BY_NAME_URL, requests.get)
        testify.assert_equal(resp.json(), FILTER_BY_NAME)

class TestFilterByBreed(testify.TestCase):
    """docstring for TestFilterByBreed."""    

    def test_filter_breed_url(self):
        return assert_url(FILTER_BY_BREED_URL, requests.get)
    
    def test_filter_breed_output(self):
        resp = fun_call(FILTER_BY_BREED_URL, requests.get)
        testify.assert_equal(resp.json(), FILTER_BY_BREED)

class TestFilterByColor(testify.TestCase):
    """docstring for TestFilterByColor."""    

    def test_filter_color_url(self):
        return assert_url(FILTER_BY_COLOR_URL, requests.get)
    
    def test_filter_color_output(self):
        resp = fun_call(FILTER_BY_COLOR_URL, requests.get)
        testify.assert_equal(resp.json(), FILTER_BY_COLOR)

if __name__ == '__main__':
    testify.run()
