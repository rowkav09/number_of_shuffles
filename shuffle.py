import math

def num_shuffle(a: str) -> int:
    frequency = {}


    # Count frequencies
    for char in a:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1


    total = sum(frequency.values())


    shuffles = math.factorial(total)


    for c in frequency:
        if frequency[c] > 1:
            shuffles //= math.factorial(frequency[c])

    return shuffles



print(num_shuffle('DEAN'))