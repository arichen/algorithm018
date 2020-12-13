## Bit Operation
- Odd and even
    - odd: x & 1 == 1
    - even: x & 1 == 0
- Divide by 2:
    - x >> 1
    - bit operation is faster than division
- x & (x - 1): flip the least significant 1-bit to 0
- x & -x: get the lowest bit 1