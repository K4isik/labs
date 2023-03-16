def solve(numheads, numlegs):
    chicken = int((4 * numheads - numlegs) / 2)
    rab = int(numheads - chicken)

    return f'Num of chicken is {chicken}. Num of rabbits is {rab}.'


print(solve(35, 94))