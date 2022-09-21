
# caching.py
# A simple LRU Cache implementation

# MIT License

# Copyright (c) 2022 Shine Jayakumar

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from hashlib import md5

LRU_DEFAULT_SIZE = 100

class LRUCache:
    def __init__(self, maxsize:int = LRU_DEFAULT_SIZE):
        self.memstore = {}
        self.keyref = []
        self.maxsize = maxsize

    def set(self, key:str, data):
        """
        Stores data against a key
        """
        keyhash = md5(key.lower().encode('utf-8')).hexdigest()
        # if key exists, remove the keyhash from its current position
        self._remove_keyhash_if_exists(keyhash)
        # add it to the most recent
        self.keyref.insert(0, keyhash)
        self.memstore[keyhash] = data
        # remove old unused keyhash
        self._remove_lru()
        
    def get(self, key:str):
        """
        Get data against a key
        """
        keyhash = md5(key.lower().encode('utf-8')).hexdigest()
        # remove the keyhash from its current position
        self._remove_keyhash_if_exists(keyhash)
        # add it to the most recent
        self.keyref.insert(0, keyhash)
        return self.memstore.get(keyhash)

    def exists(self, key:str):
        """
        Check if a key exists
        """
        keyhash = md5(key.lower().encode('utf-8')).hexdigest()
        if keyhash in self.keyref:
            return True
        return False

    def _remove_lru(self):
        while len(self.keyref) > self.maxsize:
            keyhash = self.keyref.pop()
            self.memstore.pop(keyhash, 'Key Error')
    
    def _remove_keyhash_if_exists(self, keyhash):
        """
        Removes keyhash from the current position in the keyref
        """
        if keyhash in self.keyref:
            self.keyref.remove(keyhash)





