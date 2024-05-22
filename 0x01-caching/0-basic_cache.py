#!/usr/bin/env python3
"""
inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """represents BasicCache class"""

    def put(self, key, item):
        """
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        """
        return self.cache_data.get(key, None)
