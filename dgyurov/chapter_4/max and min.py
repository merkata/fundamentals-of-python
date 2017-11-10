print('Please enter five numbers separated by a comma : ')
a = (int(input('first: ')))
b = (int(input('second: ')))
c = (int(input('third: ')))
d = (int(input('fourth: ')))
e = (int(input('fifth: ')))
print(a, b, c, d, e )
if a >= b and a >= c and a >= d and a >= e:
    Max = a
elif b >= a and b >= c and b >= d and b >= e:
    Max = b
elif c >= a and c >= b and c >= d and c >= e:
    Max = c
elif d >= a and d >= c and d >= b and d >= e:
    Max = d
elif e >= a and e >= c and e >= d and e >= b:
    Max = e
if a <= b and a <= c and a <= d and a <= e:
    Min = a
elif b <= a and b <= c and a <= d and b <= e:
    Min = b
elif c <= a and c <= b and c <= d and c <= e:
    Min = c
elif d <= a and d <= c and d <= b and d <= e:
    Min = d
elif e <= a and e <= c and e <= d and e <= b:
    Min = e
print('The Maximum and Minimum values are ')
print(Max) 
print(Min)