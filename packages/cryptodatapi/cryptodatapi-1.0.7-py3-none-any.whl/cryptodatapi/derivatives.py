import requests
import json
import os

def get_derivatives(id=None, sym=None):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = 'https://cryptodatapi.com/v1/derivatives/'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearerToken}'
    }
    if id != None: 
        url += id
    response = requests.get(url=url, headers=headers)
    return response.json()

def put_derivatives(id, payload): 
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f'https://cryptodatapi.com/v1/derivatives/{id}'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearerToken}'
    }
    response = requests.put(url=url, headers=headers, data=payload)
    return response.json()

def delete_derivatives(id): 
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f'https://cryptodatapi.com/v1/derivatives/{id}'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearerToken}'
    }
    payload = json.dumps({
        'id': id
    })
    response = requests.delete(url=url, headers=headers, data=payload)
    return response.json()

def add_derivatives(payload):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = 'https://cryptodatapi.com/v1/derivatives'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearerToken}'
    }
    response = requests.post(url=url, headers=headers, data=payload)
    return response.json()