import itertools


def strong_connect(vertex):
    global edges, indices, lowlinks, connected_components, index, stack
    indices[vertex] = index
    lowlinks[vertex] = index
    index += 1
    stack.append(vertex)

    for v, w in (e for e in edges if e[0] == vertex):
        if indices[w] < 0:
            strong_connect(w)
            lowlinks[v] = min(lowlinks[v], lowlinks[w])
        elif w in stack:
            lowlinks[v] = min(lowlinks[v], indices[w])

    if indices[vertex] == lowlinks[vertex]:
        connected_components.append([])
        while stack[-1] != vertex:
            connected_components[-1].append(stack.pop())
        connected_components[-1].append(stack.pop())


# *******************************************************************************************
# read the exported file of the PRISM

f = open("/content/1-1", "r")
edges = []
for x in f:
    x = x.rstrip()
    y = x.split(" ")
    z11 = int(y[0])
    z12 = int(y[2])
    edges.append((z11, z12))
# ******************************************************************************************************

vertices = set(v for v in itertools.chain(*edges))
indices = dict((v, -1) for v in vertices)
lowlinks = indices.copy()
connected_components = []

index = 0
stack = []
for v in vertices:
    if indices[v] < 0:
        strong_connect(v)


# ________________________________________________________________________
def FindMaxLength(lst):
    maxLength = max(len(x) for x in lst)

    count = 0
    for elem in lst:
        if len(elem) == maxLength:
            count += 1

    return maxLength, count


# _________________________________________________________________
# this function helps to find the different number
# of states in each components.

def getSizeOfNestedList(listOfElem):
    count1 = 0
    for elem in listOfElem:
        # Check if type of element is list
        if len(elem) == 1:
            count1 += 1
    return count1, 1


# print Components
print(connected_components)

# Print number of components
print(len(connected_components))

# max len of each component will be printed.
print(FindMaxLength(connected_components))

print(getSizeOfNestedList(connected_components))

# ----------------------------------------------------------------------------------------

