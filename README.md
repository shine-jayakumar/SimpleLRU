# SimpleLRU

A simple LRU caching class in Python

### Usage:
```
from caching import LRUCache

lrucache = LRUCache()

data = {
    "name": "Bob",
    "emp_id": 101
}

lrucache.set('hello world', data=data)

print(f'Key exists?: {lrucache.exists("hello world")}')

print(lrucache.get('hello world'))

```