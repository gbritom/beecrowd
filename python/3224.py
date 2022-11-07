def ah_count(cliente, medico):
    if len(cliente) > 3 or len(cliente) < 1000:
        if len(cliente) < len(medico):
            return 'no'
        else:
            return 'go'
a = input()
b = input()
print(ah_count(a,b))
