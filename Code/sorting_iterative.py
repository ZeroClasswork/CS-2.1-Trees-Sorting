#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # check each consecutive pair
    #   if later is < previous
    #       return false
    # return true

    # check if list length is less than 2 and therefore is in order
    if len(items) < 2:
        return True
    
    # i and i+1 represent each consecutive pair
    for i in range(len(items)-1):
        if items[i+1] < items[i]:
            return False    # return early in case of counterexample to sorted
    return True             # return true only when every pair checked

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # return early if already sorted
    if is_sorted(items):
        return

    # start with a true value
    # - note: swapped will represent if a value has been swapped.
    # -       if no value has been swapped, the list is already sorted.
    # -       if the list has already been sorted, the function can end.
    swapped = True
    while swapped:
        for i in range(len(items)-1):
            swapped = False # can only be updated when true, keeps it accurate
            if items[i] > items[i+1]: # check each pair
                items[i], items[i+1] = items[i+1], items[i] # first swap
                index = i # represents the "highlighted" index 
                          # (where a smaller value has been found)
                swapped = True # since we're found a swap, change our tracker
                for j in range(i): # check each value before index
                    if items[i-j-1] > items[index]: # found another swap, cont.
                        items[index], items[i-j-1] = items[i-j-1], items[index]
                        index = i-j-1
                    else: # no more swapping for index! we can stop j's loop
                        break

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # if items length is 0 or 1, stop
    if len(items) < 2:
        return

    # i is a marker for the next swapping point with the selection
    for i in range(len(items)):
        # minimum is the index where the lowest number from i on is
        minimum = i
        for j, item in enumerate(items[minimum:]):
            # set minimum according to the next lowest number
            if item < items[minimum]:
                minimum = j+i 
        # swap marker value and minimum value
        items[i], items[minimum] = items[minimum], items[i]

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # if items length is 0 or 1, stop
    if len(items) < 2:
        return

    for index, relevent in enumerate(items):
        for i, item in enumerate(items[:index]):
            if relevent < item:
                items.pop(index)
                items.insert(i, relevent)
                break

if __name__ == "__main__":
    insertion_sort(['A', 'B'])