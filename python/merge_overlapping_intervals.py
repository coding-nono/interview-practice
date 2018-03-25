
# Problem Statement
# We have an list containing intervals we want to merge intervals that overlap each other.
#  Example : [(1,4), (3,5), (6,8), (9,10)]) ==>  [(1,5), (6,8), (9,10)]
#

def overlap_next(cur, n):
    if n[0] >= cur[0] and n[0] <= cur[1]:
        return True
    return False

def merge_arrays(cur, n):
    if n[1] < cur[1]:
        return cur
    return (cur[0], n[1])


def merge_overlaping_intervals(arr):
    # First sort the array
    arr = sorted(arr)
    i = 0
    while i < len(arr) -1:
        if overlap_next(arr[i], arr[i+1]):
            arr[i] = merge_arrays(arr[i], arr[i+1])
            arr.pop(i+1)
            # go back for that case
            i -= 1
        i +=1
    return arr

 

if __name__ == '__main__':
    assert merge_overlaping_intervals([(1,4), (6,8), (3,5), (9,10)]) == [(1, 5), (6, 8), (9, 10)]
    assert merge_overlaping_intervals([(1,4), (3,5), (6,8), (9,12), (11, 20)]) == [(1, 5), (6,8), (9, 20)]
    assert merge_overlaping_intervals([]) == []
    assert merge_overlaping_intervals([(1,4),(2,3)]) == [(1,4)]
    assert merge_overlaping_intervals([(1,2)]) == [(1,2)]
    assert merge_overlaping_intervals([(1,2), (2,4)]) == [(1,4)]
    assert merge_overlaping_intervals([(1,4),(0,2),(3,5)]) == [(0,5)]
    
