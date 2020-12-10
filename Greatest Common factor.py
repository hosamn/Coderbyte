# def gcf(x, y):
#     x_factors = [i for i in range(1, x + 1) if x % i == 0]
#     y_factors = [i for i in range(1, y + 1) if y % i == 0]
#     common = set(x_factors).intersection(y_factors)
#     return max(common)

# print(gcf(12, 8))

import math
print(math.gcd(12, 8))


