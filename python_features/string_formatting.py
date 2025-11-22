# Add separators to an existing number at print time
n: int = 1000000000000
print(f'{n:_}')
print(f'{n:,}')
# print(f'{n:.}') This does not work, unfortunately

# Des not work for decimal places
n: float = 1000000000000.000015
print(f'{n:_}')
print(f'{n:,}')
