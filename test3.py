with open("test.py","r+") as g:
    print(g.mode)
    for line in g:
        print(line, end="")
#it will read all the lines at a time
#end means it wont print one empty line after a line of execution
