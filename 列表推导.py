alist = [7,23,8,31,10,8]
blist = [2,7,34,8]
union = [b*2 for a in alist for b in blist if a==b]
print(union)