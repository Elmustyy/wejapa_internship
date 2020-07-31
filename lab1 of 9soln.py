# exploring the methods from the below websites https://docs.python.org/3/library/stdtypes.html#string-methods 
x=4
y=5
#testing boolean
print('Division and modulus test of x and y:{}'.format(divmod(x,y)))
print('power test of x and y:{}'.format(pow(x,y)))
print('bolean test of x and y:{}'.format(x==y))
lists = [1,2,3,4]
lists.insert(1,5)
lists.append(9)
print(list)
print('sorted list:{}'.format(lists.sort()))
print(list(range(1,18,3)))
var = "i love coding"
print(var.startswith('i'))
print(var.endswith('ing'))
print(var.isalpha())
print(var.isalnum())
print(var.isdigit())
print(var.isnumeric())
print(var.isprintable())
print(var.strip())
print(var.split())
print('we\tja\tpa'.expandtabs(tabsize=5))