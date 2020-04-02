#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) in the worst case because it would have to run the full 
                      for loop (dependent on n) in the case that it is sorted 
                      or is sorted to the last item
    Memory usage: O(n) because we always have items under consideration with no 
                      other variables"""
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
    Running time: O(n^2) - worst case if every item needs to be moved.
                  O(n)   - best case if every item is already sorted; only 
                      needs one pass.
    Memory usage: O(n) since we are only working on items."""
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
    Running time: O(n^2) because we need to embed for loops to find the
                      appropriate value for each index (every case)
    Memory usage: O(n) because we only work on list items."""
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
    Running time: O(n^2) - (triangular) worst case because each item must 
                      iterate through all already inserted items to find it's 
                      place.
                  O(n)   - best case because it could constantly be inserted to 
                      the beginning of the already inserted items  
    Memory usage: O(n) with this implementation since we are only concerned with
                      changing items one placement at a time which is 2 (a 
                      constant) operations"""
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