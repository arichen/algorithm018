# Idea:
# Use the array.index function as the sorting key.
# Combine arr2 and sorted arr1, so the overlapping elements will use index of arr2,
# and non-overlapping elements will be in acsending order.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)