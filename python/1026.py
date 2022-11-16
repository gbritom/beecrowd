while True:
    try: a,b = input().split(" ")
    except EOFError: break
    print(int(int(a) ^ int(b)))
