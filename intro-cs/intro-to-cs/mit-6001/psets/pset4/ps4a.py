# Problem Set 4A
# Name: Sheikh MD Sazidul Islam
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    if len(sequence) == 1:
        return [sequence]
    permutations = []
    for letter in sequence:
        remaining = sequence.replace(letter, '', 1)
        z = get_permutations(remaining)

        for t in z:
            permutations.append(letter+t)
    return permutations

if __name__ == '__main__':
    print(get_permutations('abc'))
    print(get_permutations('abcd'))
    print(get_permutations('abcde'))