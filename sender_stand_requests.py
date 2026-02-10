import data
import configuration
import requests

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE_PATH + configuration.CREATE_ORDER_PATH, json=order_body, headers=data.headers)

def get_order(track):
    return requests.get(configuration.URL_SERVICE_PATH + configuration.ORDERS_PATH + str(track))