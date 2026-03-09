import modul2 as m
f = [1]
m.init(f)

for i in range(100):
    f[0] = i
    print(f)
    m.show()