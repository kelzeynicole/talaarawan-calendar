"""             TALAARAWAN: 
            Calendar Application
                                        """
import os
import csv
import sys
import time
import emoji
import calendar as cl
import datetime as dt
from datetime import date
from datetime import datetime
from termcolor import colored


os.system('mode con: cols=100')
width = os.get_terminal_size().columns

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

dash = "="*width

def readdata():
    try:
        with open("data.csv", mode='r') as file:
            csvFile = csv.reader(file)
            rec = [i for i in csvFile if i!=[]]
    except:
        rec = list()
    return rec

def writedata(data):
    with open("data.csv",'w') as file:
        fwrite = csv.writer(file)
        fwrite.writerows(data)
        file.close()

def app():
    os.system('cls')
    print("\n\n")
    today = date.today()
    now = datetime.now()
    p1 = " Today is "
    dt = today.strftime("%B %d, %Y")
    dt_ = now.strftime("%I:%M %p")
    today = p1 + str(dt) + "." + "\t\t\t\t\t\t\t\t   " + str(dt_)
    print(color.GREEN + today + color.END)
    print("\n")
    print(color.BOLD + 'TALAARAWAN: Calendar Application'.center(width) + color.END)
    print(dash.center(width))
    
def check_date(start,date,end):
    f = '%m/%d/%Y'
    d1 =(dt.datetime.strptime(start,f).year , dt.datetime.strptime(start,f).month)
    d2 =(dt.datetime.strptime(end,f).year , dt.datetime.strptime(end,f).month)

    if d1<=date<=d2: return True
    else: return False

def getinfo():
    title = input("\t\tTitle (required field): ")
    while (len(title) == 0):
        print("\t\t\t\t" + color.RED + "Invalid. This is a required field." + color.END)
        title = input("\t\tTitle (required field): ")
    start = input("\t\tStart date (required field, format: 'MM/DD/YYYY'): ")
    while (start == str):
    	print("\t\t\t\t" + color.RED + "Invalid date! Please try again.".center(89) + color.END)
    	start = input("\t\tStart date (required field, format: 'MM/DD/YYYY'): ")
    while (len(str(start)) == 0):
    	print("\t\t\t\t" + color.RED + "Invalid. This is a required field." + color.END)
    	start = input("\t\tStart date (required field, format: 'MM/DD/YYYY'): ")
    end = input("\t\tEnd date (optional field, format: 'MM/DD/YYYY'): ")
    location = input("\t\tLocation (optional field): ")
    notes = input("\t\tNotes (optional field): ")
    return [title, start, end, location, notes]
    
def create():
    app()
    print(color.CYAN + "CREATE EVENT".center(width) + color.END)
    print(dash.center(width))
    print('\n\n')

    info = getinfo()
    
    if info[2]=='':
        d1 = dt.datetime.strptime(info[1],'%m/%d/%Y')
        d2 = dt.datetime.strptime(info[1],'%m/%d/%Y')
    else:
        d1 = dt.datetime.strptime(info[1],'%m/%d/%Y')
        d2 = dt.datetime.strptime(info[2],'%m/%d/%Y')
    if d1<=d2:
        try: count = len(readdata())+1
        except: count = 1
        info.insert(0,count)
        with open("data.csv",'a') as file:
            fwrite = csv.writer(file)
            fwrite.writerow(info)
            file.close()
        print(color.GREEN + "\n"+"Event successfully created.".center(width) + color.END)
        time.sleep(2)
        events()
    else:
        print(color.RED + "\n"+"Invalid Dates! Please try again.".center(width) + color.END)
        time.sleep(1.5)
        create()

def update():
    app()
    print(color.CYAN + "UPDATE EVENT".center(width) + color.END)
    print(dash.center(width))
    print('\n\n')

    x = input("\t\tEnter event number: ")

    rec = readdata()
    tmp = []
    for i in rec:
        if i[3]=='':
            if check_date(i[2],(year,month),i[2]): tmp.append(i)
        else:
            if check_date(i[2],(year,month),i[3]): tmp.append(i)

    flag = 0
    for i in tmp:
        if i[0]==x: flag=1

    if flag:
        info = getinfo()
        try:
            if info[2]=='':
                d1 = dt.datetime.strptime(info[1],'%m/%d/%Y')
                d2 = dt.datetime.strptime(info[1],'%m/%d/%Y')
            else:
                d1 = dt.datetime.strptime(info[1],'%m/%d/%Y')
                d2 = dt.datetime.strptime(info[2],'%m/%d/%Y')
            if d1<=d2:
                modified = [i for i in rec if i[0]!=x]
                info.insert(0,x)
                modified.insert(int(x)-1,info)
                writedata(modified)
                print(color.GREEN + "\n" + "Event successfully updated.".center(width) + color.END)
                time.sleep(1)
                events()
            else:
                print(color.RED + "\n" + "Earlier end date than start date! Please try again.".center(width) + color.END)
                time.sleep(1)
                update()
        except:
            print(e)
            print(color.RED + "\n" + "Invalid Dates! Please try again.".center(width) + color.END)
            time.sleep(1)
            update()
    else:
        print(color.RED + "\n" + "Invalid Event ID! Please try again.".center(width) + color.END)
        time.sleep(1)
        events()

def delete():
    app()
    print(color.CYAN + "DELETE EVENT".center(width) + color.END)
    print(dash.center(width))
    print('\n\n')

    x = input(" \t\tEnter event ID: ")

    rec = readdata()
    tmp = []
    for i in rec:
        if i[3]=='':
            if check_date(i[2],(year,month),i[2]): tmp.append(i)
        else:
            if check_date(i[2],(year,month),i[3]): tmp.append(i)

    flag = 0
    for i in tmp:
        if i[0]==x: flag=1

    if flag:
        modified = [i for i in rec if i[0]!=x]
        writedata(modified)
        print(color.GREEN + "\n" + "Event successfully deleted.".center(width) + color.END)
        time.sleep(1)
        events()
    else:    
        print(color.RED + "\n" + "Invalid Event ID. Please try again.".center(width) + color.END)
        time.sleep(1)
        events()

def events():
    app()
    print(color.CYAN + "EVENTS".center(width) + color.END)
    print(dash.center(width))
    print('\n\n')

    rec = readdata()
    tmp = []
    for i in rec:
        if i[3] =='':
            if check_date(i[2],(year,month),i[2]): tmp.append(i)
        else:
            if check_date(i[2],(year,month),i[3]): tmp.append(i)
            
    if tmp == []:
        print(color.BOLD + "No events to display.".center(width) + color. END + "\n\n")

        print('{0:<24}'.format("a. Create Event").center(width))
        print('{0:<24}'.format("b. Go back to month view").center(width))
        a = input('{0:>45}'.format("Enter: "))
        a = a.lower()
        if a == "a": create()
        elif a == "b": calendar()
        else:
            print(color.RED + "\n" + "Invalid Input! Please try again.".center(width) + color.END)
            time.sleep(1)
            events()
    else: 
        for i in tmp:
            print("\t\t\tID:",i[0],"\n\t\t\tTitle:",i[1],"\n\t\t\tStart date:",i[2],"\n\t\t\tEnd date:",i[3],"\n\t\t\tLocation:",i[4],"\n\t\t\tNotes:",i[5])
            print(("-"*15).center(width))

        print('\n\n')
        print('{0:<24}'.format("a. Create Event").center(width))
        print('{0:<24}'.format("b. Update Event").center(width))
        print('{0:<24}'.format("c. Delete Event").center(width))
        print('{0:<24}'.format("d. Go back to month view").center(width))
        a = input('{0:>45}'.format("Enter: "))
        a = a.lower()
        if a == "a": create()
        elif a == "b": update()
        elif a == "c": delete()
        elif a == "d": 
        	calendar() 
        	menu()
        	if a == "e":
        		sys.exit("\n" + color.GREEN + "Thank you for using Talaarawan: Calendar Application!".center(width) + color.END)
        else:
            print(color.RED + "\n" + "Invalid Input! Please try again.".center(width) + color.END)
            time.sleep(1)
            events()

def calendar():
    app()
    print(color.CYAN + ((dt.datetime.strptime(str(month),"%m").strftime("%B")).upper() + " " + str(year)).center(width) + color.END)
    print(dash.center(width))
    print(color.YELLOW + '\n',"{0:^12}{1:^12}{2:^12}{3:^12}{4:^12}{5:^12}{6:^12}".format("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday").center(width) + color.END )
    days = [0 for i in range(cl.monthrange(year,month)[0]+1)] + [dt.date(year,month,i) for i in range(1,cl.monthrange(year,month)[1]+1)]

    rec = readdata()
    flag = 1
    for c,i in enumerate(days):
        if i!=0:
            for data in rec:
                if data[3]=='':
                    d1 = dt.datetime.strptime(data[2],'%m/%d/%Y').date()
                    d2 = dt.datetime.strptime(data[2],'%m/%d/%Y').date()
                else:
                    d1 = dt.datetime.strptime(data[2],'%m/%d/%Y').date()
                    d2 = dt.datetime.strptime(data[3],'%m/%d/%Y').date()
                if d1<=i<=d2:
                    flag = 0
                    break
            if flag: days[c] = str(i.day)
            else:
                days[c] = color.RED + "*" + str(i.day) + color.END
                flag = 1

    days = [days[i:i+7] for i in range(0,len(days),7)]
    
    for i in days:
        tmp=''
        for j in i:
            if j!=0: tmp+="{0:>12}".format(j)
            else: tmp+="{0:>12}".format(' ')
        print("\n   ",tmp)
    menu()

def menu():
    a = color.BLUE + 'a.' + color.END + " View Next Month"
    b = color.BLUE + 'b.' + color.END + " View Previous Month"
    c = color.BLUE + 'c.' + color.END + " Select Month and Year"
    d = color.BLUE + 'd.' + color.END + " View Events"
    e = color.BLUE + 'e.' + color.END + " Exit Calendar"

    print('\n')
    print("\t\t\t\t" + "      " + a)
    print("\t\t\t\t" + "      " + b)
    print("\t\t\t\t" + "      " + c)
    print("\t\t\t\t" + "      " + d)
    print("\t\t\t\t" + "      " + e)

    global year,month
    choice = input('{0:>45}'.format("   Enter: "))
    choice = choice.lower()

    if choice == "a":
        month += 1
        if month > 12: month,year = 1, year + 1
        calendar()
        
    elif choice == "b":
        month -= 1
        if month < 1: month,year = 12, year - 1
        calendar()
        
    elif choice =="c": 
        mm = input('{0:>45}'.format("Enter month: "))
        try: month = dt.datetime.strptime(mm,"%b").month
        except:
            try: month = dt.datetime.strptime(mm,"%B").month
            except:
                try: month = dt.datetime.strptime(mm,"%m").month
                except:
                    print(color.RED + "Invalid Input!".center(width) + color.END)
                    time.sleep(1)
                    calendar()

        yy = input('{0:>45}'.format("Enter year: "))
        try: year = dt.datetime.strptime(yy,"%Y").year  
        except:
            print(color.RED + "Invalid Input!".center(width) + color.END)
            time.sleep(1)
            calendar()
        calendar()
        
    elif choice =="d":
        events()

    elif choice =="e":
        sys.exit("\n" + color.GREEN + "Thank you for using Talaarawan: Calendar Application!".center(width) + color.END)
    
    else:
        print("\n" + color.RED + "Invalid Input! Please try again.".center(width) + color.END)
        time.sleep(1)
        calendar()

year, month = dt.date.today().year, dt.date.today().month
calendar()