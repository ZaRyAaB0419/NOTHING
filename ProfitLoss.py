actualcost=float(input("plz enter actual product price :"))
saleamount=float(input("plz enter sale amount :"))

if (saleamount > actualcost):
    amount=saleamount-actualcost
    print("total profit={0}".format(amount))

else:
    print("noprofit")    