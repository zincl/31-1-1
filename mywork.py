from flask import Flask, render_template, request, session, redirect,url_for,flash
from wtforms import Form, StringField, validators, IntegerField, SelectField
import tkinter.messagebox
import Processing
import uobitems
app = Flask(__name__)
import Processdbs

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/alldecredemption')
def alldecredemption():
    alldecredemptionList = []
    alldecredemptionList = Processing.processsalldecredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('alldecredemption.html', alldecredemption=alldecredemptionList)

@app.route('/uobdecredemption')
def uobdecredemption():
    uobdecredemptionList = []
    uobdecredemptionList = Processing.processuobdecredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('uobdecredemption.html', uobdecredemptions=uobdecredemptionList)


@app.route('/ocbcdecredemption')
def ocbcdecredemption():
    ocbcdecredemptionList = []
    ocbcdecredemptionList = Processing.processocbcdecredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('ocbcdecredemption.html', ocbcdecredemptions=ocbcdecredemptionList)

@app.route('/dbsdecredemption')
def dbsdecredemption():
    dbsdecredemptionList = []
    dbsdecredemptionList = Processing.processdbsdecredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('dbsdecredemption.html', dbsdecredemptions=dbsdecredemptionList)


@app.route('/alljanredemption')
def alljanredemption():
    alljanredemptionList = []
    alljanredemptionList = Processing.processsalljanredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('alljanredemption.html', alljanredemption=alljanredemptionList)


@app.route('/uobjanredemption')
def uobjanredemption():
    uobjanredemptionList = []
    uobjanredemptionList = Processing.processuobjanredemption(session['user'], session["cardno"])
    return render_template('uobjanredemption.html', uobjanredemptions=uobjanredemptionList)


@app.route('/ocbcjanredemption')
def ocbcjanredemption():
    ocbcjanredemptionList = []
    ocbcjanredemptionList = Processing.processocbcjanredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('ocbcjanredemption.html', ocbcjanredemptions=ocbcjanredemptionList)


@app.route('/dbsjanredemption')
def dbsjanredemption():
    dbsjanredemptionList = []
    dbsjanredemptionList = Processing.processdbsjanredemption(session['user'], session["cardno"])
    return render_template('dbsjanredemption.html', dbsjanredemptions=dbsjanredemptionList)

@app.route('/allfebredemption')
def allfebredemption():
    allfebredemptionList = []
    allfebredemptionList = Processing.processsallfebredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('allfebredemption.html', allfebredemption=allfebredemptionList)


@app.route('/uobfebredemption')
def uobfebredemption():
    uobfebredemptionList = []
    uobfebredemptionList = Processing.processuobfebredemption(session['user'], session["cardno"])
    return render_template('uobfebredemption.html', uobfebredemptions=uobfebredemptionList)


@app.route('/ocbcfebredemption')
def ocbcfebredemption():
    ocbcfebredemptionList = []
    ocbcfebredemptionList = Processing.processocbcfebredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('ocbcfebredemption.html', ocbcfebredemptions=ocbcfebredemptionList)


@app.route('/dbsfebredemption')
def dbsfebredemption():
    dbsfebredemptionList = []
    dbsfebredemptionList = Processing.processdbsfebredemption(session['user'], session["cardno"])
    return render_template('dbsfebredemption.html', dbsfebredemptions=dbsfebredemptionList)

@app.route('/allredemption')
def allredemption():
    allredemptionList = []
    allredemptionList = Processing.processallredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('allredemption.html', allredemptions=allredemptionList)

@app.route('/alluobredemption')
def alluobredemption():
    alluobredemptionList = []
    alluobredemptionList = Processing.processalluobredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('alluobredemption.html', alluobredemptions=alluobredemptionList)


@app.route('/allocbcredemption')
def allocbcredemption():
    allocbcredemptionList = []
    allocbcredemptionList = Processing.processallocbcredemption(session['user'], session["cardname"],session["cardno"])
    return render_template('allocbcredemption.html', allocbcredemptions=allocbcredemptionList)


@app.route('/alldbsredemption')
def alldbsredemption():
    alldbsredemptionList = []
    alldbsredemptionList = Processing.processalldbsredemption(session['user'],session["cardname"],session["cardno"])
    return render_template('alldbsredemption.html', alldbsredemptions=alldbsredemptionList)


#UOB CATALOGUE
@app.route('/catalogueuob',methods=['GET', 'POST'])
def catalogueuob():
    session['user']="Rubbish"
    session["cardname"] = "UOB Platinum Card"
    session["cardno"]= "9888-6121-0824-1112"
    if request.method == 'POST':
        session['cart'] = True
        fullname = request.form["fullname"]
        itempoint = request.form["point"]
        currentpoint = request.form["currentpoint"]
        redeempoint = request.form["redeempoint"]
        quantity = request.form["quantity"]
        print(quantity )

        if quantity == "0":
            flash("Enter a valid quantity!", 'danger')
        else:
            Processing.cartdict(session['user'],session["cardname"],session["cardno"],fullname, itempoint,currentpoint,redeempoint,quantity )
            print("You have successfully redeemed {} {}".format(quantity, fullname))
     #  listqty=Processing.list_qty(session['user'],session["cardno"])
    uob_redeempts = Processing.processredeemedpoints(session['user'],session["cardname"],session["cardno"])
    uob_currentpts = Processing.processcurrentpoints(session['user'],session["cardname"],session["cardno"])
    uob_preferreditems = Processing.processpreferreduob(session['user'],session["cardname"],session["cardno"])
    uob_allitems = Processing.processallitems(session['user'],session["cardname"],session["cardno"])
    uob_retialitems = Processing.processretailitems(session['user'],session["cardname"],session["cardno"])
    uob_diningitems = Processing.processdiningitems(session['user'],session["cardname"],session["cardno"])
    uob_leisureitems = Processing.processleisureitems(session['user'],session["cardname"],session["cardno"])
    #user = session["user"], cardno = session["cardno"],

    return render_template('catalogueuob.html',uobcurrentpts=uob_currentpts, uobredeempts=uob_redeempts, uobpreferreditems = uob_preferreditems, uoballitems = uob_allitems,uobretialitems=uob_retialitems, uobdiningitems=uob_diningitems, uobleisureitems=uob_leisureitems)

@app.route('/cartuob',methods=['GET', 'POST'])
def cartuob():
    uobcheckoutList=[]
    checkoutpoints  = Processing.processredeemedpoints(session['user'],session["cardname"],session["cardno"])
    uobcheckoutList = Processing.checkout(session['user'],session["cardname"],session["cardno"])

    if request.method == 'POST' and 'remove' in request.form:
        position = request.form["remove"]

        print(position)
        Processing.removeitem(session['user'], session["cardname"],session["cardno"],position)
        return redirect(url_for('cartuob'))
    return render_template('cartuob.html', uobcheckout=uobcheckoutList, uobcheckoutpts=checkoutpoints)

@app.route('/addtoredemption')
def addtoredemption():
    print("hello")
    Processing.addtoredemptionhistory(session['user'], session["cardname"], session["cardno"])
    session.clear()
    session['user'] = "Rubbish"
    session["cardname"] = "UOB Platinum Card"
    session["cardno"] = "9888-6121-0824-1112"
    return redirect(url_for('allredemption'))
    # change to max reward page


#DBS CATALOGUE
@app.route('/cataloguedbs',methods=['GET', 'POST'])
def cataloguedbs():
    session['user']="Rubbish"
    session["cardname"] = "DBS Black Card"
    session["cardno"]= "7381-3191-7122-0333"
    if request.method == 'POST':
        session['cart'] = True
        fullname = request.form["dbsfullname"]
        itempoint = request.form["dbspoint"]
        currentpoint = request.form["dbscurrentpoint"]
        redeempoint = request.form["dbsredeempoint"]
        quantity = request.form["dbsquantity"]
        print(quantity )

        if quantity == "0":
            flash("Enter a valid quantity!", 'danger')
        else:
            Processdbs.cartdictdbs(session['user'],session["cardname"],session["cardno"],fullname, itempoint,currentpoint,redeempoint,quantity )
            print("You have successfully redeemed {} {}".format(quantity, fullname))
     #  listqty=Processing.list_qty(session['user'],session["cardno"])
    dbs_redeempts = Processdbs.processredeemedpointsdbs(session['user'],session["cardname"],session["cardno"])
    dbs_currentpts = Processdbs.processcurrentpointsdbs(session['user'],session["cardname"],session["cardno"])
    dbs_preferreditems = Processdbs.processpreferreddbs(session['user'],session["cardname"],session["cardno"])
    dbs_allitems = Processdbs.processallitemsdbs(session['user'],session["cardname"],session["cardno"])

    dbs_dineitems = Processdbs.processdineitemsdbs(session['user'],session["cardname"],session["cardno"])
    dbs_leisureitems = Processdbs.processleisureitemsdbs(session['user'],session["cardname"],session["cardno"])
    dbs_shopitems = Processdbs.processshopitemsdbs(session['user'],session["cardname"],session["cardno"])
    #user = session["user"], cardno = session["cardno"],


    return render_template('cataloguedbs.html',dbscurrentpts=dbs_currentpts, dbsredeempts=dbs_redeempts, dbspreferreditems = dbs_preferreditems, dbsallitems = dbs_allitems, dbsdineitems=dbs_dineitems, dbsleisureitems=dbs_leisureitems,dbsshopitems=dbs_shopitems)

@app.route('/cartdbs',methods=['GET', 'POST'])
def cartdbs():
    dbscheckoutList=[]
    checkoutpoints  = Processdbs.processredeemedpointsdbs(session['user'],session["cardname"],session["cardno"])
    dbscheckoutList = Processdbs.checkoutdbs(session['user'],session["cardname"],session["cardno"])

    if request.method == 'POST' and 'remove' in request.form:
        position = request.form["remove"]

        print(position)
        Processdbs.removeitemdbs(session['user'], session["cardname"],session["cardno"],position)
        return redirect(url_for('cartdbs'))
    return render_template('cartdbs.html', dbscheckout=dbscheckoutList, dbscheckoutpts=checkoutpoints)

@app.route('/addtoredemptiondbs')
def addtoredemptiondbs():
    print("hello")
    Processdbs.addtoredemptionhistorydbs(session['user'], session["cardname"], session["cardno"])
    session.clear()
    session['user'] = "Rubbish"
    session["cardname"] = "DBS Black Card"
    session["cardno"] = "7381-3191-7122-0333"
    return redirect(url_for('allredemption'))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
