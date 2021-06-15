# if statements to dictionarys


# old
if a == a.go:
    b = c.go
elif a == a.stop:
    b = c.stop













# new
opFunc = {
    a.go: c.go
    a.stop: c.stop
}

# call
try:
    b = opFunc[b]()
except:
    b = c.DefaultObject()

strategy = operationFuncs.get(operation(), DefaultObject())