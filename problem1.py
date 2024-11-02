import pulp

my_prob = pulp.LpProblem("First_Problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, upBound=34)
x2 = pulp.LpVariable("x2", lowBound=0, upBound=14)

# Objective function
my_prob += 1000*x1 + 1200*x2, 'Z'
# constraints
my_prob += 10*x1 + 5*x2 <= 200, 'c1'
my_prob += 2*x1 + 3*x2 <= 60, 'c2'

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