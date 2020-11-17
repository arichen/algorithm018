## Binary Search
- Answer why a problem can be solved by binary search: increasing/decreasing, bounded.

## Problem: Find Minimum in Rotated Sorted Array
https://github.com/arichen/algorithm-notes/blob/main/binary_search/minimum_in_rotated_sorted_array.md

## Note
- half..
```python
(left + right) // 2  # may overflow
left + (right - left) // 2  # preven overflow when values are large
```