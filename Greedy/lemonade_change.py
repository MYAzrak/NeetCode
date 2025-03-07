# Greedy since we preferred to save fives (if we can) we a person gives $20
# Time: O(N)
# Space: O(1)
def lemonadeChange(bills) -> bool:
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        elif bill == 20:
            if tens > 0:  # check if you can give then a ten first since it is less imp
                if fives > 0:
                    tens -= 1
                    fives -= 1
                else:
                    return False
            elif fives >= 3:
                fives -= 3
            else:
                return False

    return True
