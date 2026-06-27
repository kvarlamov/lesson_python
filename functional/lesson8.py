def odometer(oksana: list[int]) -> int:
    spd = oksana[0::2]
    tim = oksana[1::2]
    prev_tim = [0] + tim[:-1]

    return sum(s * (t - p) for s, t, p in zip(spd, tim, prev_tim) )

# проверка
lst = [15,1,25,2,30,3,10,5]
print(odometer(lst))