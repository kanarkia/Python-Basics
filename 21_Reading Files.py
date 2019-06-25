
'''''''''
employess_var = open('employees.txt','r')

print(employess_var.readable())

print(employess_var.read())

employess_var.close()
'''''''''

employess_var = open('employees.txt','r')

for for_var in employess_var.readlines():
    print(for_var)

employess_var.close()