from functools import wraps
from time import sleep
import time

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val_undecorated_function = func(*args, **kwargs)
        emphasized = val_undecorated_function.upper() + "!!!!!!"
        return emphasized
    return wrapper

def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "I do DECLARE, " + orig_val
    return wrapper
  
def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2.5)
        return func(*args, **kwargs)
    return wrapper

def timed_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time-start_time} seconds to complete')
        return result
    return wrapper


class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        self.length = 0
        for element in reversed(collection):
            self.insert(element)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __str__(self):
        value_string = ""
        for value in self:
            value_string += f"[ {value} ] -> "
        return value_string + 'None'

    def __len__(self):
        return self.length

    def __eq__(self, another):
        return list(self) == list(another)

    def __getitem__(self, idx):
        if len(self) == 0:
            raise IndexError
        if idx < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == idx:
                return item

        raise IndexError

    def insert(self, value):
        newNode = Node(value, self.head)
        self.head = newNode
        self.length += 1

    def append(self, value):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(value, None)
                self.length += 1
                break
            current = current.next


class Node:
    def __init__(self, data, next=None):
        self.value = data
        self.next = next
