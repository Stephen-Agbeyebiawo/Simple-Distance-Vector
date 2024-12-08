def run_DV(dvList): #Computes best path with DV algorithm. It accepts DV database List created with the "create_dvDBList" function
    #Remove dead routes. If link to router route was learnt from is down remote the route from the DV table
    """for i in range(len(neighborDBList)):
        if neighborDBList[i].state == "down":
            for k in range(len(dvList)):
                try:
                    if dvList[k][3] == neighborDBList[i].name:
                        dvList.pop(k)
                    else:
                        pass
                except:
                    pass"""

    #1. remove routes pointing to self
    for i in range(len(dvList)):
        try:
            if dvList[i][0] == R.name:  #if this router's name is the source router of the received route, pop it from the list or received routes
                dvList.pop(i)
        except:
            pass
    dvList.sort()

    #2. remove duplicates and keep best routes. This prevent loops which can infinitely inclrease the cost of incoming routes (split horizon)
    b = set([]) #use set to remove duplicates
    dvIndex = []
    k = 0
    for i in dvList:
        dvIndex.append([k,i[0]])
        k += 1

    dvSet = set([])
    n = []

    dvIndex.sort()  #sort to get least cost routes to the top of the route list
    deleteList = []

    for i in dvList:
        dvSet.add(i[0])
    dvSet = list(dvSet)
    dvSet.sort()

    for i in dvList:
        n.append(i[0])

    #print(dv)

    for k in dvSet:
        if n.count(k) > 1:
            for i in dvIndex:
                if k == i[1]:
                    if k in b:
                        #print(f"{k} already in b")
                        #print(f"{dvList[i[0]]} removed")
                        deleteList.append(dvList[i[0]])
                    else:
                        b.add(k)
                else:
                    pass
    #print(deleteList)
    deleteList.sort()
    for x in deleteList:
        if x in dvList:
            dvList.remove(x)
    #print(dv)
    update_dv_database(dvList)
