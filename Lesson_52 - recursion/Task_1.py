from typing import Optional, Union

def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp == 0:
        return 1
    elif exp == 1:
        return x
    elif exp < 0:
        raise ValueError('This function works only with exp > 0.')
    elif exp % 2 == 0:
        return to_power(x*x, exp//2)
    else:
        return x*to_power(x*x, (exp-1)//2)

print(to_power(2, 3) == 8)
print(to_power(3.5, 2) == 12.25)
print(to_power(2, -1))