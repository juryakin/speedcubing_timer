import random
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def generate_scramble():
    moves = ['R', 'L', 'D', 'U', 'F', 'B']
    adds = ['', "'", '2']
    contraposed_dict = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U', 'F': 'B', 'B': 'F'}
    scramble = [random.choice(moves) + random.choice(adds) for i in range(21)]
    for index in range(len(scramble)):
        if len(scramble) - index > 2:
            while scramble[index + 1][0] == scramble[index][0] or scramble[index - 1][0] == scramble[index][0]:
                scramble[index] = random.choice(moves) + random.choice(adds)
    for index in range(len(scramble)):
        if len(scramble) - index > 3:
            try:
                while scramble[index - 1][0] == contraposed_dict[scramble[index]] and scramble[index - 2] == scramble[index]:
                    scramble[index] = random.choice(moves) + random.choice(adds)
            except:
                pass
    while scramble[len(scramble) - 1][0] == scramble[len(scramble) - 2][0]:
        scramble[len(scramble) - 1] = random.choice(moves) + random.choice(adds)
    return [elem + ' ' for elem in scramble]

