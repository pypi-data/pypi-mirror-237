"""
Cloudflare KV Store

This module provides a simple interface to the Cloudflare KV.

Requires:
Cloudflare api key with the following permissions:
    - Account Storage KV Storage: Write
"""

import os
import json
import requests
from datetime import datetime

class KVStore():

    def __init__(self, namespace_id = None, account_id = None, api_key = None):
        
        if not namespace_id:
            namespace_id = os.environ.get('KV_NAMESPACE_ID', None)
        if not account_id:
            account_id = os.environ.get('CF_ACCOUNT_ID', None)
        if not api_key:
            api_key = os.environ.get('CF_API_KEY', None)

        if not namespace_id:
            raise Exception('namespace_id is required')
        if not account_id:
            raise Exception('account_id is required')
        if not api_key:
            raise Exception('api_key is required')

        self.namespace_id = namespace_id
        self.account_id = account_id
        self.api_key = api_key


    def __get_url(self, key):
        return f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/storage/kv/namespaces/{self.namespace_id}/values/{key}"

    def __set_url(self, key):
        return f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/storage/kv/namespaces/{self.namespace_id}/values/{key}"
    
    def __get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}'
        }
    
    
    def get(self, key):
        """Get a value from the KV Cache

        Args:
            key (str): The key to get

        Returns:
            str: The value
        """
        url = self.__get_url(key)
        headers = self.__get_headers()
        response = requests.request("GET", url, headers=headers)
        js = response.json()

        if js.get('success') is False:
            return None
        else:
            return js
    

        
    def set(self, key, value, expiresMinutes = None):
        """
            Set a value in the KV Cache

            Args:
                key (str): The key to set
                value (dict): The value to set
                expires (minutes (int)): The number of minutes to expire the value in the cache

            Returns:
                bool: True if successful, False otherwise
        """

        if expiresMinutes is not None and expiresMinutes > 0:
            expiresMinutes = int(datetime.now().timestamp()) + (expiresMinutes * 60)
            value = {
                'value': json.dumps(value),
                'expiration_ttl': expiresMinutes
            }

        url = self.__set_url(key)
        headers = self.__get_headers()
        response = requests.put(url, headers=headers, data=json.dumps(value))

        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error setting value: {response.status_code} {response.text}")