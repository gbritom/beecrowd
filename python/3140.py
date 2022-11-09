count = False
while True:
    try:
        a = input()
        if '<body>' in a:
            count = True
        if "</body>" in a:
            count = False
        if count == True and "<body>" not in a:
            print(a)
    except EOFError:
        break
