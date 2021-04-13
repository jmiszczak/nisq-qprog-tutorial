from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.NewBoolVar('x')
y = model.NewBoolVar('y')
x*y