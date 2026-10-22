
a = [40, 25, 60, 15, 30]

left, right = 0, len(a) - 1

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1

print(a)
