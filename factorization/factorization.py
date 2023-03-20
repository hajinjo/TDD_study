class Factorization:
    def __init__(self):
        pass

    def factorization(self, num: int):
        factors = []

        divider = 2
        while True:
            while num % divider == 0:
                factors.append(divider)
                num = num//divider
            if num == 1:
                break
            divider += 1
        return factors
