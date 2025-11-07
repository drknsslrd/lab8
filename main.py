# N - масса частицы
N = int(input("Введите количество чисел: "))
x = []
k = 0.5

for i in range(N):
    x.append(int(input("Введите числа по очереди: ")))

while len(x) > 1:
    x = sorted(x)
    mCh = (x[0] + x[1]) - (k * (x[0] + x[1]))
    x.remove(x[0])
    print(mCh)
    print(x)
