import pulp

my_prob = pulp.LpProblem("Second_Problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

# Objective function
my_prob += 4*x1 - x2 + 2*x3, 'Z'
# constraints
my_prob += 2*x1 + 1*x2 + 2*x3 <= 6, 'c1'
my_prob += 1*x1 - 4*x2 + 2*x3 <= 0, 'c2'
my_prob += 5*x1 - 2*x2 - 2*x3 <= 4, 'c3'

print(my_prob)

status = my_prob.solve()

print(pulp.LpStatus[my_prob.status])
# print(pulp.value(c))
# print(pulp.value(w))

# =============================================
for v in my_prob.variables():
    print(v.name, "=", v.varValue)

print("\nMaximum Objective :")
print(pulp.value(my_prob.objective))