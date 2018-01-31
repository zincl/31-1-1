from uobitems import uobitems , checkoutuobitems
from allredemption import allredemption
import operator
import datetime
from pathlib import Path
import os

def processallitems(user,cardname,cardno):
    allitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            points = points.strip()
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))

        points = point[-1]
        individual_items = a.split(",")

        if (points >= int(individual_items[3])):
            c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                individual_items[4], individual_items[5], individual_items[6],individual_items[7])
            maxquantity = points // int(individual_items[3])
            c.set_maxquantity(maxquantity)
            allitems.append(c)
    avaliableuobpts_file.close()
    return allitems


def processretailitems(user,cardname,cardno):
    retailitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point=[]
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Retail"):
            if (points >= int(individual_items[3])):
                c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                c.set_maxquantity(maxquantity)
                retailitems.append(c)
    uobitems_file.close()
    return retailitems

def processdiningitems(user,cardname,cardno):
    diningitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dining"):
            if (points >= int(individual_items[3])):
                d = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                d.set_maxquantity(maxquantity)
                diningitems.append(d)
    uobitems_file.close()
    return diningitems


def processleisureitems(user,cardname,cardno):
    leisureitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            if (points >= int(individual_items[3])):
                e = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                e.set_maxquantity(maxquantity)
                leisureitems.append(e)
    uobitems_file.close()
    return leisureitems

def processredeemedpoints(user, cardname, cardno):
    redeemedpoint = 0
    my_file = Path("file/redeemuobpts.txt")
    checkout_file = Path("file/uobcheckout.txt")
    pt=[]
    if my_file.exists():
        if checkout_file.exists():
            redeemuobpts_file = open("file/redeemuobpts.txt", "a")
            uobcheckout_file = open("file/uobcheckout.txt","r")
            for points in uobcheckout_file:
                points = points.strip()
                transaction = points.split(",")
                print(transaction)
                if transaction[0] == user:
                    if transaction[1] == cardname:
                        if transaction[2] == cardno:
                            redeemedpoint += int(transaction[6])
                            pt.append(transaction[6])
                            print(pt)
                            totalredeempt = int(pt[-1])
                            redeempointdata = user + ',' + cardname + ',' + str(cardno) + ',' + str(totalredeempt) + '\n'
                            redeemuobpts_file.write(redeempointdata)
        else:
            beginningdata = user + ','+ cardname + ',' + str(cardno) + ',' + str(0) + '\n'
            redeemuobpts_file = open("file/redeemuobpts.txt", "w")
            redeemuobpts_file.write(beginningdata)
            redeemuobpts_file.close()
    else:
        beginningdata = user + ','+ cardname + ',' + str(cardno) + ',' + str(0) + '\n'
        redeemuobpts_file = open("file/redeemuobpts.txt", "w")
        redeemuobpts_file.write(beginningdata)
        redeemuobpts_file.close()
    return redeemedpoint

def processcurrentpoints(user,cardname,cardno):
    #uob_allpoints =[]
    uob_currentpts = 0
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    for j in avaliableuobpts_file:
        transaction = j.split(",")
        if transaction[0] == user and transaction[1] == cardname:
            if transaction[2] == cardno:
                uob_currentpts = transaction[3]
     #           uob_allpoints.append(int(transaction[2]))
    #uob_currentpts = uob_allpoints[-1]
    avaliableuobpts_file.close()
    return uob_currentpts


# in transaction history of redemption
def processallredemption(user,cardname,cardno):
    allredemptionList =[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        i = i.strip()
        list = i.split(',')
        if list[0] == user:
            s = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]),list[6])
            allredemptionList.append(s)
    allredemption_file.close()
    return allredemptionList

def processalluobredemption(user, cardname, cardno):
    alluobredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            bank = list[2].split(" ")
            if bank[0] == "UOB":
                y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alluobredemptionList.append(y)
    allredemption_file.close()
    return alluobredemptionList

def processallocbcredemption(user, cardname,cardno):
    allocbcredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            bank = list[2].split(" ")
            if bank[0] == "OCBC":
                y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allocbcredemptionList.append(y)
    allredemption_file.close()
    return allocbcredemptionList

def processalldbsredemption(user, cardname,cardno):
    alldbsredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            bank = list[2].split(" ")
            if bank[0] == "DBS":
                y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldbsredemptionList.append(y)
    allredemption_file.close()
    return alldbsredemptionList

def processsalldecredemption(user, cardname,cardno):
    alldecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                z = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldecredemptionList.append(z)
    allredemption_file.close()
    return alldecredemptionList

def processuobdecredemption(user, cardname,cardno):
    uobdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobdecredemptionList.append(y)
    allredemption_file.close()
    return uobdecredemptionList

def processocbcdecredemption(user,cardname, cardno):
    ocbcdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcdecredemptionList.append(y)
    allredemption_file.close()
    return ocbcdecredemptionList

def processdbsdecredemption(user, cardname,cardno):
    dbsdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsdecredemptionList.append(y)
    allredemption_file.close()
    return dbsdecredemptionList

def processsalljanredemption(user, cardname,cardno):
    alljanredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1]== "01" and individual[2]=="2018":
                z = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alljanredemptionList.append(z)
    allredemption_file.close()
    return alljanredemptionList

def processuobjanredemption(user, cardname,cardno):
    uobjanredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "01" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobjanredemptionList.append(y)
    allredemption_file.close()
    return uobjanredemptionList

def processocbcjanredemption(user,cardname ,cardno):
    ocbcjanredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "01" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcjanredemptionList.append(y)
    allredemption_file.close()
    return ocbcjanredemptionList

def processdbsjanredemption(user, cardname,cardno):
    dbsjanredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "01" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsjanredemptionList.append(y)
    allredemption_file.close()
    return dbsjanredemptionList

def processsallfebredemption(user, cardname,cardno):
    allfebredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1]== "02" and individual[2]=="2018":
                z = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allfebredemptionList.append(z)
    allredemption_file.close()
    return allfebredemptionList

def processuobfebredemption(user, cardname,cardno):
    uobfebredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "02" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobfebredemptionList.append(y)
    allredemption_file.close()
    return uobfebredemptionList

def processocbcfebredemption(user, cardname,cardno):
    ocbcfebredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "02" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcfebredemptionList.append(y)
    allredemption_file.close()
    return ocbcfebredemptionList

def processdbsfebredemption(user, cardname,cardno):
    dbsfebredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == user:
            individual = list[1].split("/")
            if individual[1] == "02" and individual[2]=="2018":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[0],list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsfebredemptionList.append(y)
    allredemption_file.close()
    return dbsfebredemptionList


def processpreferreduob(user,cardname, cardno):
    uobpreferredList=[]
    qtyanditemdictionary = processget_quantityuob(user,cardname,cardno)  # returns a dictionary; {user:[[item1,qty1] , [] , [] ]
    if qtyanditemdictionary == {'user': []}:
        uobpreferredList.append("no redemption made")
        print(uobpreferredList)
        return  uobpreferredList

    qtyanditem = qtyanditemdictionary[user]

    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    point = []
    for currentpoints in avaliableuobpts_file:
        currentpoints = currentpoints.strip()
        usert = currentpoints.split(",")
        if usert[0] == user and usert[1] == cardname:
            if usert[2] == cardno:
                point.append(int(usert[3]))
    avaliableuobpts_file.close()
    points = point[-1]

    alluobitems = open("file/uobitems.txt", "r")
    for individual in alluobitems:
        individual= individual.strip()
        individual=individual.split(",")
        b = individual[7]
        for i in qtyanditem:
            itemname=i[0]
            qty = i[1]
            if str(itemname) == str(b):
                if (points >= int(individual[3])):
                    preferreditems = uobitems(individual[1], individual[2], individual[3], individual[4],
                                            individual[5],individual[6], individual[7])
                    preferreditems.set_count(int(qty))
                    currentcount = preferreditems.get_count()
                    maxquantity = points // int(individual[3])
                    preferreditems.set_maxquantity(maxquantity)
                    uobpreferredList.append(preferreditems)
    avaliableuobpts_file.close()
    return uobpreferredList

def processget_quantityuob(user, cardname,cardno): #based on the quantity of your redemptionhistory
    dictionary={}
    dictvalue = []
    allredemption_file = open("file/allredemption.txt", "r")
    for redeemed in allredemption_file:
        listed = redeemed.strip()
        lists = listed.split(",")
        if lists[0] == user and lists[2]== cardname:
            if lists[3] == cardno:
                bank = lists[2].split(" ")
                if bank[0] == "UOB":
                    individualitemandqty = []
                    individualitemandqty.append(lists[4])
                    individualitemandqty.append(int(lists[5]))
                dictvalue.append(individualitemandqty)

    allredemption_file.close()
    totals = {}
    for k, v in dictvalue:
        totals[k] = totals.get(k, 0) + v
    dictvalue = sorted(map(list, totals.items()))
    dictvalue = sorted(dictvalue, key=operator.itemgetter(1), reverse=True)
    print(dictvalue)

    if (len(dictvalue))> 3:
        empty = []
        for i in range(3):
            value = dictvalue[i]
            empty.append(value)
        dictionary[user] = empty

    else:
        dictionary[user] = dictvalue
    print(dictionary)
    return dictionary



cart=[]
def cartdict(user, cardname,cardno, fullname, itempoint, currentpoint, redeempoint,quantity):
    totalitempt = int(itempoint) * int(quantity)
    pointsleft = int(currentpoint) - int(totalitempt)
    redeempoint = int(redeempoint) + int(totalitempt)
#current point left after redemption
    avaliablepointsdata = user + ',' + cardname + ',' + cardno + ',' + str(pointsleft) + '\n'
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(avaliablepointsdata)
    avaliableuobpts_file.close()
    #redemption point after remdeem
    redeempointsdata = user + ',' + cardname + ',' + cardno + ',' + str(redeempoint) + '\n'
    redeemuobpts_file = open("file/redeemuobpts.txt", "a")
    redeemuobpts_file.write(redeempointsdata)
    redeemuobpts_file.close()

    processingadd =open("file/processingadd.txt", "a")
    add = user + ',' + cardname + ',' + str(cardno) + ',' + fullname + ',' + itempoint + ',' + quantity + ',' + str(totalitempt) + '\n'
    processingadd.write(add)
    processingadd.close()

    reading = open("file/processingadd.txt", "r")
    redeemuobpts_file = open("file/uobcheckout.txt", "w")
    data = []
    for items in reading:
        i =[]
        items = items.strip()
        items = items.split(",")
        item = items[0] + ',' + items[1] + ',' + str(items[2]) + ',' + items[3] + ',' + str(
            items[4]) + ',' + str(items[5]) + ',' + str(items[6]) + '\n'

        i.append(item)
        data.append(item)
    reading.close()

    for row in data:
        redeemuobpts_file.write("".join(row) + "")
    redeemuobpts_file.close()




def checkout(user,cardname,cardno):
    uobcheckout = []
    count=0
    redeem_file = Path("file/uobcheckout.txt")  # check if u got add to cart a not, if exist
    if redeem_file.exists():
        print(uobcheckout)
        print("adding")
        redeemuobpts_file = open("file/uobcheckout.txt", "r")

        for items in redeemuobpts_file:
            items = items.strip()
            items = items.split(",")
            if items[0] == user:
                if items[1] == cardname:
                    if items[2] == cardno:
                        uobitems_file = open("file/uobitems.txt", "r")
                        for a in uobitems_file:
                            a = a.strip()
                            a = a.split(",")
                            if a[7] == items[3]:
                                item = checkoutuobitems(a[1], a[2], a[3],a[4], a[5], a[6], a[7], items[5], items[6],str(count))

                                uobcheckout.append(item)
                                count+=1
        return uobcheckout




    else:
        uobcheckout = []
        return uobcheckout


def addtoredemptionhistory(user, cardname, cardno):
    checkouts = open("file/uobcheckout.txt", "r")
    addtoredemption = open("file/allredemption.txt", "a")
    for a in checkouts: # add in all redemption history
        redemptiondate = datetime.datetime.today().strftime('%d/%m/%Y')
        a = a.strip()
        a = a.split(",")
        if a[0] == user and a[1] == cardname:
            if a[2] == cardno:
                bank = a[1].split(" ")
                if bank[0] =="UOB":
                    points = "UNI$" + str(a[6])
                    addtoredemption.write(user + ',' + redemptiondate + ',' + cardname + ',' + str(cardno) + ',' + a[3] + ',' + str(a[5]) + ',' + points + '\n')
    addtoredemption.close()
    checkouts.close()

    clearuobredeempt = open("file/redeemuobpts.txt", "w")
    enddata = user + ',' + cardname + ',' + str(cardno) + ',' + str(0) + '\n'
    clearuobredeempt.write(enddata)
    clearuobredeempt.close()

    clearedit = open("file/processingadd.txt", "w")
    clearedit.write("")
    clearedit.close()

    clearcheckout = open("file/uobcheckout.txt", "w")
    clearcheckout.write("")
    clearcheckout.close()


def removeitem(user,cardname,cardno,position):
    itemlist = []
    checkout_file = open("file/uobcheckout.txt", "r")
    for items in checkout_file:
        items = items.strip()
        items = items.split(",")
        if items[0] == user:
            if items[1] == cardname:
                if items[2] == cardno:
                    itemlist.append(items)
    checkout_file.close()
    print(itemlist)
    print("hello")
    item = itemlist[int(position)]

    pts = item[6]
    print(pts)
    avaliablepoint_file = open("file/avaliableuobpts.txt","r")
    point =[]
    for points in avaliablepoint_file:
        points = points.strip()
        points = points.split(",")
        if points[0] == user:
            if points[1] == cardname:
                if points[2] ==cardno:
                    point.append(points[3])
    avaliablepoint_file.close()
    currentpoint = point[-1]
    print(currentpoint)
    editcurrentpoint = open("file/avaliableuobpts.txt","a")
    currentpt = int(currentpoint) + int(pts)
    currentptdata = user + ',' + cardname + ',' + cardno + ',' + str(currentpt) + '\n'
    editcurrentpoint.write(currentptdata)
    editcurrentpoint.close()

    redeempts=[]
    redeempoint_file = open("file/redeemuobpts.txt", "r")
    for i in redeempoint_file:
        i = i.strip()
        i = i.split(",")
        if i[0] == user:
            if i[1] == cardname:
                if i[2] == cardno:
                    redeempts.append(points[3])
    redeempoint_file.close()
    redeempoint = redeempts[-1]

    editredeempoint = open("file/redeemuobpts.txt", "a")
    redeempt = int(redeempoint) - int(pts)
    print(redeempoint)
    redeemptdata = user + ',' + cardname + ',' + cardno + ',' + str(redeempt) + '\n'
    editredeempoint.write(currentptdata)
    editredeempoint.close()

    removeitem = itemlist.pop(int(position))

    reading = open("file/processingadd.txt", "r")

    data = []
    for items in reading:
        i =[]
        items = items.split(",")
        item = items[0] + ',' + items[1] + ',' + str(items[2]) + ',' + items[3] + ',' + str(
            items[4]) + ',' + str(items[5]) + ',' + str(items[6]) + '\n'

        i.append(item)
        data.append(item)
    reading.close()

    checkout_file = open("file/uobcheckout.txt", "w")
    for item in itemlist:
        checkout_file.write(",".join(item) + '\n')
    checkout_file.close()

    removing_file = open("file/processingadd.txt", "w")
    for ritem in itemlist:
        removing_file.write(",".join(ritem) + '\n')
    removing_file.close()


"""
def enternameof(user, cardno,current_point, redeem_point, points, quantity):
    amount = int(points) * int(quantity)
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
    avaliableuobpts_file.close()
    currentpoint_file = open("file/currentuobpts.txt", "a")
    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
    currentpoint_file.close()



#def removefromcart(self, user, cardno,current_point, redeem_point, points, quantity):
#    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
#    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
#    avaliableuobpts_file.close()
#    currentpoint_file = open("file/currentuobpts.txt", "a")
#    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
#    currentpoint_file.close()



def processredemptionpoints(user,cardno):
    redeemuobpts_file = open("file/redeemuobpts.txt", "r+")
    for i in redeemuobpts_file:
        if i == "":
            userredeemptdata = user + ',' + cardno + ',' + 0 + '\n'
            redeemuobpts_file.write(userredeemptdata)
            print(userredeemptdata)
    for i in redeemuobpts_file:
        redeemuobpts_file.read()
"""
