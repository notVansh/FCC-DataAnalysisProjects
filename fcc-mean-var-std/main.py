import mean_var_std

mat = [0,1,2,3,4,5,6,7,8]
res = {}
res = mean_var_std.calculate(mat)
for key, value in res.items():
  print (key, value)