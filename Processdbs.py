from dbsitems import dbsitems , checkoutdbsitems
from allredemption import allredemption
import operator
import datetime
from pathlib import Path
import os

def processallitemsdbs(user,cardname,cardno):
    allitems = []
    dbsitems_file = open("file/dbsitems.txt", "r")
    for a in dbsitems_file:
        avaliableuobpts_file = open("file/avaliabledbspts.txt", "r")
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
            c = dbsitems(individual_items[1], individual_items[2], individual_items[3],
                individual_items[4], individual_items[5], individual_items[6],individual_items[7])
            maxquantity = points // int(individual_items[3])
            c.set_maxquantity(maxquantity)
            allitems.append(c)
    avaliableuobpts_file.close()
    return allitems


def processdineitemsdbs(user,cardname,cardno):
    dineitems = []
    dbsitems_file = open("file/dbsitems.txt", "r")
    for a in dbsitems_file:
        avaliableuobpts_file = open("file/avaliabledbspts.txt", "r")
        point=[]
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dine"):
            if (points >= int(individual_items[3])):
                c = dbsitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                c.set_maxquantity(maxquantity)
                dineitems.append(c)
    dbsitems_file.close()
    return dineitems

def processleisureitemsdbs(user,cardname,cardno):
    leisureitems = []
    dbsitems_file = open("file/dbsitems.txt", "r")
    for a in dbsitems_file:
        avaliableuobpts_file = open("file/avaliabledbspts.txt", "r")
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
                d = dbsitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                d.set_maxquantity(maxquantity)
                leisureitems.append(d)
    dbsitems_file.close()
    return leisureitems


def processshopitemsdbs(user,cardname,cardno):
    shopitems = []
    dbsitems_file = open("file/dbsitems.txt", "r")
    for a in dbsitems_file:
        avaliableuobpts_file = open("file/avaliabledbspts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == user and usert[1] == cardname:
                if usert[2] == cardno:
                    point.append(int(usert[3]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Shop"):
            if (points >= int(individual_items[3])):
                e = dbsitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                e.set_maxquantity(maxquantity)
                shopitems.append(e)
    dbsitems_file.close()
    return shopitems

def processredeemedpointsdbs(user, cardname, cardno):
    redeemedpoint = 0
    my_file = Path("file/redeemdbspts.txt")
    checkout_file = Path("file/dbscheckout.txt")
    pt=[]
    if my_file.exists():
        if checkout_file.exists():
            redeemuobpts_file = open("file/redeemdbspts.txt", "a")
            dbscheckout_file = open("file/dbscheckout.txt","r")
            for points in dbscheckout_file:
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
            redeemuobpts_file = open("file/redeemdbspts.txt", "w")
            redeemuobpts_file.write(beginningdata)
            redeemuobpts_file.close()
    else:
        beginningdata = user + ','+ cardname + ',' + str(cardno) + ',' + str(0) + '\n'
        redeemuobpts_file = open("file/redeemdbspts.txt", "w")
        redeemuobpts_file.write(beginningdata)
        redeemuobpts_file.close()
    return redeemedpoint

def processcurrentpointsdbs(user,cardname,cardno):
    #uob_allpoints =[]
    uob_currentpts = 0
    avaliableuobpts_file = open("file/avaliabledbspts.txt", "r")
    for j in avaliableuobpts_file:
        transaction = j.split(",")
        if transaction[0] == user and transaction[1] == cardname:
            if transaction[2] == cardno:
                uob_currentpts = transaction[3]
     #           uob_allpoints.append(int(transaction[2]))
    #uob_currentpts = uob_allpoints[-1]
    avaliableuobpts_file.close()
    return uob_currentpts


def processpreferreddbs(user,cardname, cardno):
    dbspreferredList=[]
    qtyanditemdictionary = processget_quantitydbs(user,cardname,cardno)  # returns a dictionary; {user:[[item1,qty1] , [] , [] ]
    if qtyanditemdictionary == {'user': []}:
        dbspreferredList.append("no redemption made")
        print(dbspreferredList)
        return  dbspreferredList

    qtyanditem = qtyanditemdictionary[user]

    avaliabledbspts_file = open("file/avaliabledbspts.txt", "r")
    point = []
    for currentpoints in avaliabledbspts_file:
        currentpoints = currentpoints.strip()
        usert = currentpoints.split(",")
        if usert[0] == user and usert[1] == cardname:
            if usert[2] == cardno:
                point.append(int(usert[3]))
    avaliabledbspts_file.close()
    points = point[-1]

    alldbsitems = open("file/dbsitems.txt", "r")
    for individual in alldbsitems:
        individual= individual.strip()
        individual=individual.split(",")
        b = individual[7]
        for i in qtyanditem:
            itemname=i[0]
            qty = i[1]
            if str(itemname) == str(b):
                if (points >= int(individual[3])):
                    preferreditems = dbsitems(individual[1], individual[2], individual[3], individual[4],
                                            individual[5],individual[6], individual[7])
                    preferreditems.set_count(int(qty))
                    currentcount = preferreditems.get_count()
                    maxquantity = points // int(individual[3])
                    preferreditems.set_maxquantity(maxquantity)
                    dbspreferredList.append(preferreditems)
    avaliabledbspts_file.close()
    return dbspreferredList

def processget_quantitydbs(user, cardname,cardno): #based on the quantity of your redemptionhistory
    dictionary={}
    dictvalue = []
    allredemption_file = open("file/allredemption.txt", "r")
    for redeemed in allredemption_file:
        listed = redeemed.strip()
        lists = listed.split(",")
        if lists[0] == user and lists[2]== cardname:
            if lists[3] == cardno:
                bank = lists[2].split(" ")
                if bank[0] == "DBS":
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
def cartdictdbs(user, cardname,cardno, fullname, itempoint, currentpoint, redeempoint,quantity):
    totalitempt = int(itempoint) * int(quantity)
    pointsleft = int(currentpoint) - int(totalitempt)
    redeempoint = int(redeempoint) + int(totalitempt)
#current point left after redemption
    avaliablepointsdata = user + ',' + cardname + ',' + cardno + ',' + str(pointsleft) + '\n'
    avaliabledbspts_file = open("file/avaliabledbspts.txt", "a")
    avaliabledbspts_file.write(avaliablepointsdata)
    avaliabledbspts_file.close()
    #redemption point after remdeem
    redeempointsdata = user + ',' + cardname + ',' + cardno + ',' + str(redeempoint) + '\n'
    redeemdbspts_file = open("file/redeemdbspts.txt", "a")
    redeemdbspts_file.write(redeempointsdata)
    redeemdbspts_file.close()

    processingadd =open("file/processingadddbs.txt", "a")
    add = user + ',' + cardname + ',' + str(cardno) + ',' + fullname + ',' + itempoint + ',' + quantity + ',' + str(totalitempt) + '\n'
    processingadd.write(add)
    processingadd.close()

    reading = open("file/processingadddbs.txt", "r")
    redeemdbspts_file = open("file/dbscheckout.txt", "w")
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
        redeemdbspts_file.write("".join(row) + "")
    redeemdbspts_file.close()




def checkoutdbs(user,cardname,cardno):
    dbscheckout = []
    count=0
    redeem_file = Path("file/dbscheckout.txt")  # check if u got add to cart a not, if exist
    if redeem_file.exists():
        print(dbscheckout)
        print("adding")
        redeemdbspts_file = open("file/dbscheckout.txt", "r")

        for items in redeemdbspts_file:
            items = items.strip()
            items = items.split(",")
            if items[0] == user:
                if items[1] == cardname:
                    if items[2] == cardno:
                        uobitems_file = open("file/dbsitems.txt", "r")
                        for a in uobitems_file:
                            a = a.strip()
                            a = a.split(",")
                            if a[7] == items[3]:
                                item = checkoutdbsitems(a[1], a[2], a[3],a[4], a[5], a[6], a[7], items[5], items[6],str(count))

                                dbscheckout.append(item)
                                count+=1
        return dbscheckout




    else:
        dbscheckout = []
        return dbscheckout


def addtoredemptionhistorydbs(user, cardname, cardno):
    checkouts = open("file/dbscheckout.txt", "r")
    addtoredemption = open("file/allredemption.txt", "a")
    for a in checkouts: # add in all redemption history
        redemptiondate = datetime.datetime.today().strftime('%d/%m/%Y')
        a = a.strip()
        a = a.split(",")
        if a[0] == user and a[1] == cardname:
            print(a)
            if a[2] == cardno:
                bank = a[1].split(" ")
                if bank[0] =="DBS":
                    points =  str(a[6]) + " DBS Points"
                    addtoredemption.write(user + ',' + redemptiondate + ',' + cardname + ',' + str(cardno) + ',' + a[3] + ',' + str(a[5]) + ',' + points + '\n')
    addtoredemption.close()
    checkouts.close()

    cleardbsredeempt = open("file/redeemdbspts.txt", "w")
    enddata = user + ',' + cardname + ',' + str(cardno) + ',' + str(0) + '\n'
    cleardbsredeempt.write(enddata)
    cleardbsredeempt.close()

    clearedit = open("file/processingadddbs.txt", "w")
    clearedit.write("")
    clearedit.close()

    clearcheckout = open("file/dbscheckout.txt", "w")
    clearcheckout.write("")
    clearcheckout.close()


def removeitemdbs(user,cardname,cardno,position):
    itemlist = []
    checkout_file = open("file/dbscheckout.txt", "r")
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
    avaliablepoint_file = open("file/avaliabledbspts.txt","r")
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
    editcurrentpoint = open("file/avaliabledbspts.txt","a")
    currentpt = int(currentpoint) + int(pts)
    currentptdata = user + ',' + cardname + ',' + cardno + ',' + str(currentpt) + '\n'
    editcurrentpoint.write(currentptdata)
    editcurrentpoint.close()

    redeempts=[]
    redeempoint_file = open("file/redeemdbspts.txt", "r")
    for i in redeempoint_file:
        i = i.strip()
        i = i.split(",")
        if i[0] == user:
            if i[1] == cardname:
                if i[2] == cardno:
                    redeempts.append(points[3])
    redeempoint_file.close()
    redeempoint = redeempts[-1]

    editredeempoint = open("file/redeemdbspts.txt", "a")
    redeempt = int(redeempoint) - int(pts)
    print(redeempoint)
    redeemptdata = user + ',' + cardname + ',' + cardno + ',' + str(redeempt) + '\n'
    editredeempoint.write(currentptdata)
    editredeempoint.close()

    removeitem = itemlist.pop(int(position))

    reading = open("file/processingadddbs.txt", "r")

    data = []
    for items in reading:
        i =[]
        items = items.split(",")
        item = items[0] + ',' + items[1] + ',' + str(items[2]) + ',' + items[3] + ',' + str(
            items[4]) + ',' + str(items[5]) + ',' + str(items[6]) + '\n'

        i.append(item)
        data.append(item)
    reading.close()

    checkout_file = open("file/dbscheckout.txt", "w")
    for item in itemlist:
        checkout_file.write(",".join(item) + '\n')
    checkout_file.close()

    removing_file = open("file/processingadddbs.txt", "w")
    for ritem in itemlist:
        removing_file.write(",".join(ritem) + '\n')
    removing_file.close()
