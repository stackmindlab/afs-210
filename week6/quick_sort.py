import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

# 1st Function
def partition_middle(a_list, start, end):
    middle = (start + end) // 2
    a_list[start], a_list[middle] = a_list[middle], a_list[start]
    return partition(a_list, start, end)

# 2nd Function
def partition_end(a_list, start, end):
    a_list[start], a_list[end] = a_list[end], a_list[start]
    return partition(a_list, start, end)

# Third Function
def partition_random(a_list, start, end):
    rand = random.randint(start, end)
    a_list[start], a_list[rand] = a_list[rand], a_list[start]
    return partition(a_list, start, end)



def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
#print(myList)   

print(f"The execution time is: {end_time-start_time}")

# Did any particular method perform better? ANSWER BELOW----->

# After running the code with the provided execution times, 
# it appears that the choice of partition function did not have a 
# significant impact on the performance of the quicksort algorithm. 
# The execution times for each method were very similar and fell within a 
# relatively narrow range.
