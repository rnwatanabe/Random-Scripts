def varName(variable): 
'''
Return the name of variable.

Inputs:
 + variable: variable of a any type
 
Outputs:
  + var_as_str: string with the name of the variable
'''
  for k, v in list(globals().items()):
    if v is variable and k.find('_')==-1:
      var_as_str = k
  return var_as_str  
