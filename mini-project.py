
import random
class phonepay:
    b_name={}#"sbi":1199,"unionbank":7986
    amount={}#"sbi":2344,"unionbank":3543
    movie_name={"3":{"pt":300,"gt":200,"st":100},"kgf":{"pt":350,"gt":250,"st":150}}
    b_train={"dmm":1,"bnglr":2,"tpt":3}
    b_buses={"dmm":1,"bnglr":2,"tpt":3}
    b_flight={"bnglr":1,"hyd":2,"goa":3,"krl":2,"mob":3,"raj":4}
    history={}
    
    def disp(self):
        print(f"name:{self.name}\ncontact no:{self.phone}\nemail ID:{self.email}\nybl:{self.ybl}")
    def __init__(self,name,phone,email,ybl):
        self.name=name
        self.phone=phone
        self.email=email
        self.ybl=ybl
    @classmethod
    def sel(self):
        while True:
            self.phone=int(input(f"login with mobile number\n>>"))
            if len(str(self.phone))==10 and self.phone>0:
                phonepay.otp()                
                break  
            else:
                print(f"please enter 10 digit phone number")
        self.name=input("enter full name (or) press enter to skip:")
        self.email=input("enter email (or) press enter to skip:")
        self.ybl=str(self.phone)+"@ybl"
    @classmethod
    def otp(self):
        for r_no in range(3):
            r_no=random.randint(1000,9999)
            print(r_no)
            b_otp=int(input("enter opt:>"))
            if r_no==b_otp:
                break
            else:print("Entered wrong opt now sended new otp")
        else:print("you entered wrong otps so, not working now try later")          
    @classmethod
    def pin(self):
        global bank_name
        for set_pin1 in range(3):
            set_pin1=int(input("set pin:"))
            set_pin2=int(input("enter comform pin:"))
            if set_pin1==set_pin2:
                phonepay.b_name.update({bank_name:set_pin2})
                self.add_am=(input("enter yes /no:"))
                if self.add_am=="yes":

                    phonepay.amount.update({bank_name:int(input("enter bank bal amt:-"))})
                else:
                    phonepay.amount.update({bank_name:0})

                print("avl_banks in phonepay:-\n",phonepay.amount)
                break
            else:print('pin not match try again')
        else:print("you entered o many items wrong pin try later")
    @classmethod
    def ch_pin(self):
        global bank_name
        print("~~"*30)
        print(phonepay.b_name.keys())
        bank_name=input("enter bank name:>")
        if bank_name in phonepay.b_name:
            for self.p_pin in range(3):
                self.p_pin=int(input("enter pin:"))
                if self.p_pin==phonepay.b_name[bank_name]:

                    phonepay.pin()
                    break
                
    @classmethod
    def book_t(self):
        global t_cast1
        print(t_cast1,"\ncorform ticket enter:- yes \n else:-no")
        t_com=(input("yes or no:="))
        if t_com=='yes':
            e_amount=int(input("enter amt:-"))
            t_cast1=abs(t_cast1)
            if e_amount==t_cast1:
                if phonepay.b_name=={}:
                    print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
                    sa_op=input("enter above options no:")
                    if sa_op=="1":
                        phonepay.add_bank1()
                    elif sa_op=="2":
                        phonepay.add_bank2()
                phonepay.pay(e_amount)
            else:
                print("wrong amount is entered")
        else:
            print("thank to visit")
    @classmethod
    def pay(self,e_amount):
        global b_name
        global amount
        c=e_amount
        print(self.b_name.keys())
        d=input("enter bank name:")
        if d in self.b_name:
            for _ in range(3):
                e=int(input('enter pin:'))
                if e==self.b_name[d]:
                    if c<=self.amount[d]:
                        self.amount[d]-=c
                        if c!=0:
                            print('payment is done')
                            print(self.amount[d])
                            phonepay.history.update({d:c})
                            break
                        elif c==0:
                            print(self.amount[d])
                            break
                    else:
                        print("not safiient amt")
                        break
                else:
                    print("wrong pass try again")
            else:
                print("u  entered wrong pin so manyy time not working\ntry another")
    
    @classmethod
    def add_bank1(self):
                global bank_name
                bank_name=input("enter bank name:")
                bank_no1=int(input("enter bank no:>"))
                bank_no2=int(input("enter bank no:>"))
                if bank_no1==bank_no2:
                    iffc_no=input("enter ifsc code :>")
                    if iffc_no.isalnum():
                        cvv=input("enter cvv no:>")
                        if len(cvv)==3 and cvv[::-1]==iffc_no[:-4:-1]:
                            phonepay.otp()
                            phonepay.pin()
                        else:print("cvv is not matched")
                    else:print(iffc_no,"it's not ifsc code")
                else:print("bank no is not matched (or) bank sever down try it later")
    @classmethod
    def add_bank2(self):
                global bank_name
                bank_name=input("enter bank name:")
                bm_no=int(input("enter bank linkk phone no:>"))
                if len(str(bm_no))==10:
                    phonepay.otp()
                    phonepay.pin()
                else:print("this number is not linked in bank")

print(f"{"=-="*30}\nphonepay login page\n{"=-="*30}")
phonepay.sel() 
while True  :
    print(f"Phonepay\n{"=="*20}\n{"1.tranfer_money\n2.recharge\n3.booking_tickets\
                        \n4.check_bank_bal & add_bank\n5.history\n6.profile\n7.exit\n"}{"=="*20}")         
    a=input("enter the above opstion no:>")
    if a=="1":
        b=int(input("Enter phone no:"))
        if len(str(b))==10:
            e_amount=int(input("enter amount"))
            if phonepay.b_name=={}:
                print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
                sa_op=input("enter above options no:")
                if sa_op=="1":
                    phonepay.add_bank1()
                elif sa_op=="2":
                    phonepay.add_bank2()
            if e_amount>0:               
                phonepay.pay(e_amount)
    elif a=="2": 
        r_no=int(input("enter phone no:"))
        if len(str(r_no))==10:
            r_plans=[300,24,550,3500]
            if r_no%2==0:
                print(f"jio\n{"---"*30}\n1.28 day unlimited calls and 1.5gb/day data:                               {r_plans[0]}rs\
\n2.2gb data   :                                                          {r_plans[1]}rs\
\n3. 74 day unlimited calls and 1.5gb/day data:                           {r_plans[2]}rs\
\n4.1 year unlimited calls and 2gb/day data:                              {r_plans[3]}rs ")
                e_amount=int(input("enter amount"))
                if phonepay.b_name=={}:
                    print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
                    sa_op=input("enter above options no:")
                    if sa_op=="1":
                        phonepay.add_bank1()
                    elif sa_op=="2":
                        phonepay.add_bank2()

                if e_amount>0:
                    phonepay.pay(e_amount)
            else:
                print(f"airtel\n{"---"*30}\
                      \n1.28 day unlimited calls and 1.5gb/day data:                            {r_plans[0]}rs\
                      \n2.2gb data   :                                                         {r_plans[1]}rs\
                      \n3. 74 dayunlimited calls and 1.5gb/day data:                           {r_plans[2]}rs\
                      \n4.1 year unlimited calls and 2gb/day data:                             {r_plans[3]}rs ")
                e_amount=int(input("enter amount:"))
                if phonepay.b_name=={}:
                    print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
                    sa_op=input("enter above options no:")
                    if sa_op=="1":
                        phonepay.add_bank1()
                    elif sa_op=="2":
                        phonepay.add_bank2()

                if e_amount>0:
                    phonepay.pay(e_amount)
    elif a=='3':
        print(f"booking tickets\n{"*"*30}\n1.booking movie tickets\
              \n2.booking train tickats\n3.booking bus tickets\n4.booking flight tickets")
        book=input("enter bookin opstion:")
        if book=='1':
            movies=phonepay.movie_name
            print(movies.keys())
            m_name=input("enter movie name:")
            if m_name in movies:
                print(movies[m_name])
                s_s=input("enter requred seats op amount:-")
                if s_s in movies[m_name]:
                    e_amount=int(input("enter amount:"))
                    if int(e_amount)==movies[m_name][s_s]:
                        if phonepay.b_name=={}:
                            print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
                            sa_op=input("enter above options no:")
                            if sa_op=="1":
                                phonepay.add_bank1()
                            elif sa_op=="2":
                                phonepay.add_bank2()
                        phonepay.pay(e_amount)
                else:
                    print("not requered op")
            else:
                print("movie name i not in streming")
        elif book=="2": 
            trains=phonepay.b_train
            b_from=input("from:>")
            b_to=input("to::")
            if b_from in trains and b_to in trains:
                print(f"select the class\n{">"*30}\n1.frist class\n2.sencond class\n3.thrid class")
                e_class=input("enter class no:-")
                if e_class=="1":
                    t_cast1=(trains[b_from]-trains[b_to])*1000
                    phonepay.book_t()
                elif e_class=="2":
                    t_cast1=(trains[b_from]-trains[b_to])*500
                    phonepay.book_t()
                else:
                    t_cast1=(trains[b_from]-trains[b_to])*250
                    phonepay.book_t()
            else:
                print("trains not avalible")
        elif book=="3":
            trains=phonepay.b_buses
            b_from=input("from:>")
            b_to=input("to::")
            if b_from in trains and b_to in trains:
                print(f"select the class\n{">"*30}\n1.frist class\n2.sencond class\n3.thrid class")
                e_class=input("enter class no:-")
                if e_class=="1":
                    t_cast1=(trains[b_from]-trains[b_to])*750
                    phonepay.book_t()
                elif e_class=="2":
                    t_cast1=(trains[b_from]-trains[b_to])*300
                    phonepay.book_t()
                else:
                    t_cast1=(trains[b_from]-trains[b_to])*150
                    phonepay.book_t()
            else:
                print("bus not avalible")
        elif book=="4":
            trains=phonepay.b_flight
            b_from=input("from::>")
            b_to=input("to::")
            if b_from in trains and b_to in trains:
                print(f"select the class\n{">"*30}\n1.frist class\n2.econamic class")
                e_class=input("enter class no:-")
                if e_class=="1":
                    t_cast1=(trains[b_from]-trains[b_to])*2500
                    phonepay.book_t()
                elif e_class=="2":
                    t_cast1=(trains[b_from]-trains[b_to])*1500
                    phonepay.book_t()
    elif a=="4":
        print(f"{"<>"*25}\n1.chick_bank_bal\n2add_bank\n3.self transfer amt\n4.change pin\n{"*"*30}")
        op_cb=input("enter the op:-1 / 2 / 3/4\nenter:-")
        if op_cb=="1":
            e_amount=0
            phonepay.pay(e_amount)
        elif op_cb=="2":
            print(f"select bank adding options\n{"+"*30}\n1.bank_details\n2to mobile number")
            sa_op=input("enter above options no:")
            if sa_op=="1":
                phonepay.add_bank1()
            elif sa_op=="2":
                phonepay.add_bank2()
        elif op_cb=="3":
            se_bank=input("enter t_bank name:>")
            e_amount=int(input("enter amt:"))
            phonepay.pay(e_amount)           
            phonepay.amount[se_bank]+=e_amount
            print(phonepay.amount)
        elif op_cb=="4":
            phonepay.ch_pin()
    elif a=="5":
        print(phonepay.history)
    elif a=="6":
        print(f"<profile>\n{"^^"*30}")
        print(f"{phonepay.disp()}\navl banks:-{tuple(phonepay.amount.keys())}")
        print(f"{"--"*25}\n1.edit\n2.back")
        ed=input()
        if ed=="1":
            phonepay.sel()
        else:
            pass
    elif a=="7":
        break
    else:
        continue
    

            

