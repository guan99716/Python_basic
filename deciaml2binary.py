def decimal2binary(x):
    result = ''
    while x:
        result = str(x%2) + result
        x//=2
    return result
print(decimal2binary(11)) # -> 1011
    