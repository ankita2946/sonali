import itertools
variables=["A","B","C","D"]
colors=["Red","Blue","Yellow","Green"]
#All possible assign ments
all_assignments =itertools.product(colors,repeat=len(variables))

def valid (assignment):
    A,B,C,D=assignment
    return (A!=B) and (B!=C) and (C!=D) and (A!=D) 
solution=[]
for assignment in all_assignments:
    if valid(assignment):
        solution.append(dict(zip(variables,assignment)))
print("Valid Coloring of the map:")
for sol in solution:
    print(sol)
