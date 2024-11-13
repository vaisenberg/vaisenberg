with open('starwars.txt','r',encoding= 'utf-8') as f:
    f.seek(0)
    content = f.read()
    print(content)

    