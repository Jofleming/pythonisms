import pytest

from pythonisms import LinkedList

def test_iteration():

    items = LinkedList(('wallet','keys','pen'))

    items_list = []

    for item in items:
        items_list.append(item)

    assert items_list == ['wallet','keys','pen']


def test_list_comprehension():

    items = LinkedList(('wallet','keys','pen'))

    cap_items = [item.upper() for item in items]

    assert cap_items == ['WALLET','KEYS','PEN']

def test_list_cast():

    item_list = ['wallet','keys','pen']

    items = LinkedList(item_list)

    assert list(items) == item_list

def test_range():

    num_range = range(1,20+1)

    nums = LinkedList(num_range)

    assert len(nums) == 20


def test_filter():

    nums = LinkedList(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]

def test_next():

    items = LinkedList(['wallet','keys','pen'])

    iterator = iter(items)

    assert next(iterator) == 'wallet'
    assert next(iterator) == 'keys'
    assert next(iterator) == 'pen'

def test_stop_iteration():

    items = LinkedList(['wallet','keys','pen'])

    iterator = iter(items)

    with pytest.raises(StopIteration):
        while True:
            item = next(iterator)


def test_str():
    items = LinkedList(['wallet','keys','pen'])
    assert str(items) == '[ wallet ] -> [ keys ] -> [ pen ] -> None'


def test_equals():

    lla = LinkedList(['wallet','keys','pen'])
    llb = LinkedList(['wallet','keys','pen'])

    assert lla == llb

def test_get_item():

    items = LinkedList(['wallet','keys','pen'])

    assert items[0] == 'wallet'

def test_get_item_out_of_range():

    items = LinkedList(['wallet','keys','pen'])

    with pytest.raises(IndexError):
        items[100]