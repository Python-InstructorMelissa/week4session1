from data import data

# 1. Print back all of the data
def printAll(d):
    print("1. print all data: ", d)

printAll(data)

# 2. Print back just the name of all the characters
def printNames(d):
    # print("2. print names: ", d['name'])  Error was list indices must be integers or slices, not str
    for name in d:
        print('2. print names: ', name['name'])

printNames(data) # This prints each name as it's own line

def printNamespt2(d):
    theNames = []
    for name in d:
        theNames.append(name['name'])
    print('print names take 2: ', theNames)
    return theNames

printNamespt2(data) # This adds each name to a list (called theNames) and prints back that list

# Print back 1 entry
# def printBugs(d[0]):
#     print('3. printing back just bugs:', d[0])

# printBugs(data)

def printOneEntry(d, i):
    print('3. print 1 entry: ', d[i])

printOneEntry(data, 0)

# 3 would be the equivalent of clicking on the picture of a tune and looking at just that tunes page so like 1 entry

# 4. Print back just 1 entries img link
def printOneImg(d, i):
    print('4. print back 1 entries img link: ', d[i]['img'])

printOneImg(data, 3)

# 5.  just the list of names
print('just the names list again: ', printNamespt2(data)) # will just print 1
# adding a return to that function to see if that fixes this print
theNames = []
print("calling just the var theNames before function", theNames)
def printNamespt3(d):
    for name in d:
        theNames.append(name['name'])
    print('print names take 3: ', theNames)

printNamespt3(data)
print("calling just the var theNames after function", theNames)

# 6. print back a sentence that says the characters name and who voiced them

def printSentence(d, i):
    print(f"{d[i]['name']} is voiced by {d[i]['voice']}")

printSentence(data, 17)