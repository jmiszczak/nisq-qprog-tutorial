from ortools.sat.python import cp_model

model = cp_model.CpModel()
city_no = 4

my_var = {}
for t in range(city_no):
    for v in range(city_no):
        my_var[(t, v)] = model.NewBoolVar('var_t%iv%i' % (t, v))

for t in range(city_no):
    model.Add(sum(my_var[(t,v)] for v in range(city_no)) == 1) 
for v in range(city_no):
    model.Add(sum(my_var[(t,v)] for t in range(city_no)) == 1) 

print(model)
x = model.NewBoolVar('var_t%iv%i' % (t, v))