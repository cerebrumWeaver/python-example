import itertools
friends = ['Team 1','Team 2','Team 3','Team 4','Team 5','Team 6','Team 7','Team 8',]
res = list(itertools.combinations(friends, r=2))
print(res)
