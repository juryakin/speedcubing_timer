def avg5(file):
    with open(file) as file:
        solves = []
        text = str(file.read()).split('\n')
        for elem in text:
            try:
                elem = float(elem)
            except:
                pass
            else:
                solves.append(elem)
    if len(solves) >= 5:
        solves = solves[len(solves) - 5:len(solves)]
        solves.remove(max(solves))
        solves.remove(min(solves))
        return round(sum(solves) / len(solves), 2)
    else:
        return 'need more solves'

print(avg5('solves_list.txt'))