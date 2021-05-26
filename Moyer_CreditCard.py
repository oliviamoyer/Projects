# Olivia Moyer
# 001

# import
import datetime as dt

# define functions
def sumdigits(a):
    try:
        # sum of the first two digits of the cvv
        total=int(a[0])+int(a[1])
        return total
    except: 
        False

# returns true if credit card number is 16 and doesn't start w/ 0
def creditcardnum(b):
    try:
        if len(b)==16:
            if int(b[0])!=0:
                return True
        else:
            return False
    except: 
        return False

# returns true if the cvv length matches the credit card type
def check1(c,a):
    try:
        if c=="AmericanExpress" and len(a)==4:
            return True
        elif (c=="MasterCard" or c=="Visa" or c=="Discover") and len(a)==3:
            return True
        else: 
            return False 
    except: 
        False

# returns true if credit card num is valid and therefore the cvv sum matches the fifth digit
def check2(cnum,sum):
    try:
        if creditcardnum(cnum)==True: # need to make sure credit card number is valid
            five=int(cnum[4])
            if five==sum:
                return True
            else: 
                return False
        else: 
            return False
    except: 
        False

# returns true if card had not expired
def check3(strDate): 
    # got today's date
    today=dt.datetime.today()
    try:
        border=strDate.find('/')
        # convert input to date object
        month=int(strDate[0:border])
        year=int(strDate[border+1:])
        if month<12:
            month=month+1
        else: 
            month=month-11
            year=year+1
        ccdate=dt.datetime(year, month, 1)
        if today>=ccdate:
                return False
        else:
                return True
    except: 
        return False

# returns true if it passes the Luhn Test
def luhntest(cardnum):
    try:
        cardsum=0
        for x in range(0,16):
            num=int(cardnum[x])
            if x%2==0:
                num1=num*2
                if num1<10:
                    cardsum+=num1
                else: 
                    num2=str(num1)
                    add1=int(num2[0])
                    add2=int(num2[1])
                    num1=add1+add2
                    cardsum+=num1
            else: 
                cardsum+=num
        if cardsum%10==0: 
            return True
        else: 
            return False
    except:
        return False

 
# user input
card=input("Enter payment method from the following options: AmericanExpress, MasterCard, Visa, Discover: ",)
cnum=input("Enter credit card number:",)
cvv=input("Enter cvv:",)
date=input("Enter date mm/yyyy:",) 

# processing/testing
cvvsum=sumdigits(cvv)
if check1(card,cvv) and check2(cnum, cvvsum) and check3(date) and luhntest(cnum):
    print("Credit Card is valid")
else: 
    print("Credit Card is not valid")


    
