## Binary Search
- Answer why a problem can be solved by binary search: increasing/decreasing, bounded.

## Note
- trick
```python
(left + right) // 2  # may overflow
left + (right - left) // 2  # preven overflow when values are large
```