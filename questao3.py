
print("MATRIZ A")

a11, a12, a13, a14 = input().split()
a21, a22, a23, a24 = input().split()
a31, a32, a33, a34 = input().split()
a41, a42, a43, a44 = input().split()

a11 = int(a11)
a12 = int(a12)
a13 = int(a13)
a14 = int(a14)

a21 = int(a21)
a22 = int(a22)
a23 = int(a23)
a24 = int(a24)

a31 = int(a31)
a32 = int(a32)
a33 = int(a33)
a34 = int(a34)

a41 = int(a41)
a42 = int(a42)
a43 = int(a43)
a44 = int(a44)
print()
print("MATRIZ B")

b11, b12, b13, b14 = input().split()
b21, b22, b23, b24 = input().split()
b31, b32, b33, b34 = input().split()
b41, b42, b43, b44 = input().split()

b11 = int(b11)
b12 = int(b12)
b13 = int(b13)
b14 = int(b14)

b21 = int(b21)
b22 = int(b22)
b23 = int(b23)
b24 = int(b24)

b31 = int(b31)
b32 = int(b32)
b33 = int(b33)
b34 = int(b34)

b41 = int(b41)
b42 = int(b42)
b43 = int(b43)
b44 = int(b44)

print()
print('MATRIZ SOMA')

print("{}  {}  {}  {}".format(a11+b11, a12+b12, a13+b13, a14+b14))
print("{}  {}  {}  {}".format(a21+b21, a22+b22, a23+b23, a24+b24))
print("{}  {}  {}  {}".format(a31+b31, a32+b32, a33+b33, a34+b34))
print("{}  {}  {}  {}".format(a41+b41, a42+b42, a43+b43, a44+b44))

