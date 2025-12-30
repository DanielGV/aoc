diagnostics = []
with open('input3.txt') as f:
    for line in f:
        diagnostics.append(str(line).strip())
f.closed

l = len(diagnostics[0])

def most_frequent(bits):
    if (bits.count('0')> bits.count('1')):
        return '0'
    return '1'

def least_frequent(bits):
    if (bits.count('1') < bits.count('0')):
        return '1'
    return '0'

def search(candidates, find_compare):
    candidates = candidates.copy()
    for idx in range(l):
        candidates_left = []
        compare = find_compare([candidate[idx] for candidate in candidates])
        for diagnos in candidates:
            if (diagnos[idx]==compare):
                candidates_left.append(diagnos)
        if (len(candidates_left)==1):
            return candidates_left[0]
        candidates = candidates_left.copy()

oxygen_generator_rating = search(diagnostics, most_frequent)
CO2_scrubber_rating = search(diagnostics, least_frequent)

print('oxygen_generator_rating', oxygen_generator_rating, int(oxygen_generator_rating, 2))
print('CO2_scrubber_rating', CO2_scrubber_rating, int(CO2_scrubber_rating, 2))
life_support_rating = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)
#life_support_rating = oxygen_generator_rating * CO2_scrubber_rating

print('life support rating', life_support_rating)
exit()
