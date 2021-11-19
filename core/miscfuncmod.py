pathval = ".\/"
def rmpathval(name):
    for x in range(len(pathval)):
        name = name.replace(pathval[x],"")
    return name

def iscorrect(a,b):
    return a==b