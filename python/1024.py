def cripto(text):
    output = ''
    for i in text:
        if i.isalpha():
            output+=chr(ord(i)+3)
        else:
            output+=i
    output=output[::-1]
    tmp = []
    for i in range(len(output)):
        if i >= len(output)//2:
            tmp +=chr(ord(output[i])-1)
        else:
            tmp +=output[i]
    return ''.join(tmp)
    
x = int(input())
while x > 0:
    text = input()
    print(cripto(text))
    x -= 1
