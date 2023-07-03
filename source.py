#USING DATETIME MODULE
from datetime import *

#USING TKINTER GUI TOOLKIT 
from tkinter import *

#TAKING TODAY'S DATE AS INPUT USING DATETIME MODULE
datetoday=int(datetime.now().strftime("%Y%m%d"))  
y=datetoday//10000
m=(datetoday-(y*10000))//100
d=datetoday-(y*10000)-(m*100)
try:
   adate = date(y, m, d)
except ValueError:
    print("CAUTION!In the yyyymmdd format month must be between 1 to 12 and date between 1 to 31 which should be applicable for the month")
    datetoday=int(datetime.now().strftime("%Y%m%d"))
    y=datetoday//10000
    m=(datetoday-(y*10000))//100
    d=datetoday-(y*10000)-(m*100)
    adate = date(y, m, d)
def date30(datetoday,adate):   #CALCULATES THE DATE OF 1 MONTH BACK
    days = timedelta(30)
    date30 = adate - days
    return date30
def dateyear(datetoday,adate): #CALCULATES THE DATE OF 1 YEAR BACK
    days = timedelta(365)
    date365 = adate - days
    return date365
def date1(datetoday,adate):    #CALCULATES THE DATE OF 1 DAY BACK
    days = timedelta(1)
    date1 = adate - days
    return date1


def today_dict_maker(datetoday):
    #THE ORIGINAL DICTIONARY OF CURRENCIES
    Dict={
            "INR": 1,          #Indian Rupee
            "USD": 74.428894,  #American dollar
            "EUR": 87.225160,  #Euro
            "SGD" :54.75000,   #Singapore Dollar
            "JPY":0.67232,     #Japanese Yen
            "CNY":11.47860,    #Chinese Yuan
            "KRW":0.06437,     #South Korean Won
            "ZAR":5.00780,     #South African Rand
            "SFR":81.285545,   #Swiss Franc 
            "CAD":58.918134,   #Canadian Dollar
            "RM":17.547088,    #Malaysian Ringgit
            "AUD":53.947659,   #Australian Dollar
            "GBP":102.169863,  #British Pound
            "BRL":14.116915    #Brazilian Real
                      }

    key=list(Dict.keys())
    value=list(Dict.values())
    l1=[0]*14
    j=0
    #TAKING INPUT OF CURRENCIES FOR DAILY UPDATION OF DICTIONARY OF CURRENCIES FROM THE DEVELOPER
    def indexl (m):
       print("value of",key[m],"today in INR:")
       l1[m]=float(input())   #INPUT CURRENCIES IS FIRST TAKEN IN THE FORM OF A LIST
    for  i in range(0,14):
       try:
         indexl(i)
       except ValueError:
          print("Invalid Input")
          indexl(i)
    
    dic1= {}          #INPUT CURRENCIES VALUES IS BEING TRANSFERRED TO A DICTIONARY
    for key in key:
        dic1[key]=l1[j]
        j+=1
    
    with open("file"+ str(datetoday)+ ".txt", 'w') as f: #INPUT CURRENCIES OF DICTIONARY STORED IN A FILE WITH TODAY'S DATE
       for key, value in dic1.items():      
          f.write('%s %s\n' % (key, value))


yourname=input("What is your name?")# TO DIFFERENTIATE USER AND DEVELOPER(WHO UPDATES CURRENCIES)
if (yourname == "developer"):
    today_dict_maker(datetoday)#IF YOU ARE DEVELOPER , YOU CAN UPDATE DAILY CURRENCIES NOW
                               #IF YOU ARE A USER IT TAKES YOU TO INTERFACE TO USE THE APPLICATION


def dict_extract_file(datetoday): #USED TO EXTRACT DATA FROM STORED FILES
   
   updcf = {}       
   a_file = open("file"+ str(datetoday) + ".txt")
   for line in a_file:
            key, value = line.split()
            updcf[key] = value
   
   value1=list(updcf.values())
   for i in range(0, len(value1)):
       value1[i] = float(value1[i])    
   s=0
   for x in updcf.keys():
        updcf.update({x:value1[s]})
        s+=1
   
   return updcf

try:
    updc=dict_extract_file(datetoday) #TODAY'S DICTIONARY OF DATA IS EXTRACTED FROM FILES 
except FileNotFoundError:
    try:
        updc=dict_extract_file(date1(datetoday,adate))
    except:
        updc=dict_extract_file(20210101)

class MyWindow:  #CREATING AND FUNCTIONING TO WINDOW
    def __init__(self, win):
        #WRITING THE FRAMEWORK FOR THE WINDOW
        self.lbl1=Label(win, text='From currency:')
        self.lbl2=Label(win, text='To currency:')
        self.lbl3=Label(win, text='Amount:')
        self.lbl4=Label(win, text='Converted Amount:')
        self.lbl5=Label(win, text='INR-Indian Rupee')
        self.lbl6=Label(win, text='USD-American dollar')
        self.lbl7=Label(win, text='EUR-Euro')
        self.lbl8=Label(win, text='SGD-Singapore Dollar')
        self.lbl9=Label(win, text='JPY-Japanese Yen')
        self.lbl10=Label(win, text='CNY-Chinese Yuan')
        self.lbl11=Label(win, text='KRW-South Korean Won') 
        self.lbl12=Label(win, text='ZAR-South African Rand') 
        self.lbl21=Label(win, text='SFR-Swiss Franc') 
        self.lbl22=Label(win, text='CAD-Canadian Dollar') 
        self.lbl23=Label(win, text='RM-Malaysian Ringgit') 
        self.lbl24=Label(win, text='AUD-Australian Dollar') 
        self.lbl25=Label(win, text='GBP-British Pound') 
        self.lbl26=Label(win, text='BRL-Brazilian Real') 


        self.lbl13=Label(win, text='EXCHANGE RATE FROM') 
        self.lbl14_1=Label(win, text='TO') 
        self.lbl14_2=Label(win, text='IS')
        self.lbl16=Label(win, text=' % INCREASE IN PRICE OF CURRENCY')
        self.lbl15=Label(win, text=' CURRENCY CONVERTER')
        
        self.lbl17=Label(win, text='Select Currency')
        self.lbl18=Label(win, text='% increase by day')
        self.lbl19=Label(win, text='% increase by month')
        self.lbl20=Label(win, text='% increase by year')

        self.t1=Entry(bd=5)
        self.t2=Entry(bd=5)
        self.t3=Entry(bd=5)
        self.t4=Entry(bd=5)
        self.t13=Entry(bd=1)
        self.t14_1=Entry(bd=1)
        self.t14_2=Entry(bd=1)
        self.t17=Entry(bd=5)
        self.t18=Entry(bd=5)
        self.t19=Entry(bd=5)
        self.t20=Entry(bd=5)

        self.btn1 = Button(win, text='Convert')
        self.btn2 = Button(win, text='Calculate')
        
              
        #POSITIONS
        self.lbl15.place(x=50, y=24)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=250, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=250, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=250, y=150)
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=250, y=250)
        self.lbl13.place(x=100, y=300)
        self.t13.place(x=240, y=300)
        self.lbl14_1.place(x=100, y=330)
        self.t14_1.place(x=130, y=330)
        self.lbl14_2.place(x=260, y=330)
        self.t14_2.place(x=290, y=330)

        self.lbl16.place(x=570, y=24)
        self.lbl17.place(x=590, y=70)
        self.t17.place(x=680, y=70)
        self.lbl18.place(x=590, y=150)
        self.t18.place(x=710, y=150)
        self.lbl19.place(x=590, y=200)
        self.t19.place(x=710, y=200)
        self.lbl20.place(x=590, y=250)
        self.t20.place(x=710, y=250)



        self.lbl5.place(x=440, y=50)
        self.lbl6.place(x=440, y=70)
        self.lbl7.place(x=440, y=90)
        self.lbl8.place(x=440, y=110)
        self.lbl9.place(x=440, y=130)
        self.lbl10.place(x=440, y=150)
        self.lbl11.place(x=440, y=170)
        self.lbl12.place(x=440, y=190)
        self.lbl21.place(x=440, y=210)
        self.lbl22.place(x=440, y=230)
        self.lbl23.place(x=440, y=250)
        self.lbl24.place(x=440, y=270)
        self.lbl25.place(x=440, y=290)
        self.lbl26.place(x=440, y=310)

        self.b1=Button(win, text='Convert', command=self.convert)#COVERT BUTTON
        self.b1.place(x=250, y=200) #CONVERT BUTTON POSITION
        
        self.b2=Button(win, text='Calculate', command=self.calpc)#CALCULATE BUTTON
        self.b2.place(x=620, y=100)#CALCULATE BUTTON POSITION

        
    def convert(self):#CONVERTS CURRENCIES
        self.t4.delete(0, 'end')

        self.t13.delete(0, 'end')
        self.t14_1.delete(0, 'end')
        self.t14_2.delete(0, 'end')

        fromcurr=(self.t1.get())
        tocurr=(self.t2.get())
        ipamount=int(self.t3.get())
        for x in updc.keys():
              if x==fromcurr:
                 val1=updc[x]
        for x in updc.keys():
              if x==tocurr:
                  val2=updc[x]
        opamount=((ipamount*val1)/val2)
        self.t4.insert(END, str(opamount))
        
        exchangerate=((float)((val2/val1)))
        print(exchangerate)
        self.t13.insert(END,fromcurr)
        self.t14_1.insert(END,tocurr)
        self.t14_2.insert(END,exchangerate)
    
    def calpc(self):#CALCULATES RATE OF INCREASE IN CURRENCY FOR A PERIOD OF TIME
        self.t18.delete(0, 'end')
        self.t19.delete(0, 'end')
        self.t20.delete(0, 'end')
        scurr=(self.t17.get())
        dt=updc
        try:
         dyt=dict_extract_file(date1(datetoday,adate))
        except FileNotFoundError:
         dyt=dict_extract_file((20210101))
        try:  
         dlm=dict_extract_file(date30(datetoday,adate))
        except FileNotFoundError:
         dlm=dict_extract_file(20210102)
        try:
         dly=dict_extract_file(dateyear(datetoday,adate))
        except FileNotFoundError:
         dly=dict_extract_file(20210103)
        for x in dt.keys():
              if x==scurr:
                 v1=dt[x]
        for x in dyt.keys():
              if x==scurr:
                 v2=dyt[x]
        for x in dlm.keys():
              if x==scurr:
                 v3=dlm[x]
        for x in dly.keys():
              if x==scurr:
                 v4=dly[x]
        pibd=((float)((v1-v2)/v1)*100)
        pibm=((float)((v1-v3)/v1)*100)
        piby=((float)((v1-v4)/v1)*100)
        if(scurr=="INR"):
            pibd=str("NO VALUE CHANGE")
            pibm=str("INR-BASE CURRENCY")
            piby=str("NO VALUE CHANGE")
        self.t18.insert(END,pibd)
        self.t19.insert(END,pibm)
        self.t20.insert(END,piby)
        
  
      
   
window=Tk()
mywin=MyWindow(window)
window.title('CURRENCY CONVERTER')
window.geometry("900x380")
window.mainloop()

