
import firebase_admin
from opcua import Client
from PyQt5.uic import loadUi
from basic2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread,pyqtSignal
from firebase_admin import credentials,firestore


cred=credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
client=Client("opc.tcp://192.168.100.100:4840")

class MainWindow(QMainWindow):
    
    old_axis,oldAxis=[],[]
    old_hmi,oldHmi=[],[]
    old_user,oldUser=[],[]
    old_real,oldReal=[],[]

    listAxis,valueAxis=[],[]
    listHmi,valueHmi=[],[]
    listUser,valueUser=[],[]
    listReal,valueReal=[],[]

    real,axis,hmi,user={},{},{},{}
    
    insertAxis=False
    insertHmi=False
    insertUser=False
    insertReal=False
    
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("basic2.ui",self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        

        self.loaddata()
        self.thread=ThreadClass(parent=None)
        self.thread.start()
        
        self.thread.signal_axis.connect(self.refAxis)
        self.thread.signal_hmi.connect(self.refHmi)
        self.thread.signal_user.connect(self.refUser)        
        self.thread.signal_real.connect(self.refReal)
        
     
    def refAxis(self,listAxis,valueAxis):
        
        if not self.insertAxis:
            print("aa")
            self.for_axis(self.listAxis,self.valueAxis)  
            self.insertAxis = True
        
        if self.insertAxis:
            print("aa")
            for i in  range(0,len(listAxis)):
                self.ui.listWidget_axis.item(i).setText(str(listAxis[i])) 
            for i in  range(0,len(listAxis)):
                self.ui.listWidget_avalue.item(i).setText(str(valueAxis[i]))         


    def refHmi(self,listHmi,valueHmi):
        
        if not self.insertHmi:
            self.for_hmi(self.listHmi,self.valueHmi) 
            self.insertHmi = True
        
        if self.insertHmi: 
            for i in  range(0,len(listHmi)):
                self.ui.listWidget_hmi.item(i).setText(str(listHmi[i])) 
            for i in  range(0,len(valueHmi)):
                self.ui.listWidget_hvalue.item(i).setText(str(valueHmi[i])) 


    def refUser(self,listUser,valueUser):
        
        if not self.insertUser:
                self.for_user(self.listUser,self.valueUser)
                self.insertUser = True
        
        if self.insertUser: 
            for i in  range(0,len(listUser)):
                self.ui.listWidget_user.item(i).setText(str(listUser[i])) 
            for i in  range(0,len(valueUser)):
                self.ui.listWidget_uvalue.item(i).setText(str(valueUser[i])) 


    def refReal(self,listReal,valueReal):
        
        if not self.insertReal:
                self.for_real(self.listReal,self.valueReal) 
                self.insertReal = True
        
        if self.insertReal: 
            for i in  range(0,len(listReal)):
                self.ui.listWidget_1.item(i).setText(str(listReal[i])) 
            for i in  range(0,len(listReal)):
                self.ui.listWidget_2.item(i).setText(str(valueReal[i])) 


    def for_real(self,listReal,valueReal):
        
        for x,label in enumerate(listReal):
            self.ui.listWidget_1.insertItem(x,str(label))
       
        for x,label in enumerate(valueReal):
            self.ui.listWidget_2.insertItem(x,str(label))


    def for_axis(self,listAxis,valueAxis):
        
        for x,label in enumerate(listAxis):
            self.ui.listWidget_axis.insertItem(x,str(label))
        
        for x,label in enumerate(valueAxis):
            self.ui.listWidget_avalue.insertItem(x,str(label))


    def for_hmi(self,valueHmi,listHmi):
        
        for x,label in enumerate(valueHmi):
            self.ui.listWidget_hmi.insertItem(x,str(label))
        
        for x,label in enumerate(listHmi):
            self.ui.listWidget_hvalue.insertItem(x,str(label))


    def for_user(self,valueUser,listUser):
        
        for x,label in enumerate(listUser):
            self.ui.listWidget_user.insertItem(x,str(label))
        
        for x,label in enumerate(valueUser):
            self.ui.listWidget_uvalue.insertItem(x,str(label))


    def Reallist(self,doc):
        for x in doc: self.real=x.to_dict()
            
        self.valueReal=list(self.real.values())
        self.listReal=list(self.real.keys())
        
        if self.valueReal==[]:
            self.listReal=self.oldReal
            self.valueReal=self.old_real
             


    def Axislist(self,docs):
        
        for x in docs: self.axis=x.to_dict()
            
        self.valueAxis=list(self.axis.values())
        self.listAxis=list(self.axis.keys())
            
        if self.valueAxis==[]:
            self.listAxis=self.oldAxis
            self.valueAxis=self.old_axis
       
 
    def Hmilist(self,document):    
        
        for x in document: self.hmi=x.to_dict()
        
        self.valueHmi=list(self.hmi.values())
        self.listHmi=list(self.hmi.keys())
        
        if self.valueHmi==[]:
            self.listHmi=self.oldHmi
            self.valueHmi=self.old_hmi
 
    

    def Userlist(self,documents):
        
        for x in documents: self.user=x.to_dict()
            
        self.valueUser=list(self.user.values())
        self.listUser=list(self.user.keys())
        
        if self.valueUser==[]:
            self.listUser=self.oldUser
            self.valueUser=self.old_user
    

    def loaddata(self):

        doc=db.collection('real').get()
        self.Reallist(doc)
        
        docs=db.collection('axis').get()
        self.Axislist(docs)
        
        document=db.collection('hmi').get()
        self.Hmilist(document)
        
        documents=db.collection('user').get()
        self.Userlist(documents)
        
        self.old_hmi=self.valueHmi if self.valueHmi!=[] else None
        self.oldHmi=self.listHmi   if self.valueHmi!=[] else None   
            
        self.old_axis=self.valueAxis if self.valueAxis!=[] else None
        self.oldAxis=self.listAxis   if self.valueAxis!=[] else None
            
        self.old_user=self.valueUser if self.valueUser!=[]  else None
        self.oldUser=self.listUser   if self.valueUser!=[]  else None
            
        if len(self.real) > 0: self.old_real=self.real.values()
            
        self.l1.setText(str(sum(self.valueHmi)))
        self.l2.setText(str(sum(self.valueUser)))
        self.l3.setText(str(sum(self.valueAxis))) 

class ThreadClass(QThread):    
    
    signal_real=pyqtSignal(list,list)
    signal_axis=pyqtSignal(list,list)
    signal_hmi=pyqtSignal(list,list)
    signal_user=pyqtSignal(list,list)
    
    old_real,old_hmi={},{}
    old_axis,old_user={},{} 

    def __init__(self,parent=None):
        super(ThreadClass,self).__init__(parent)


    def run(self):
        db=firestore.client()

        while True:
            doc=db.collection('real').get()
            for x in doc: real=x.to_dict() 
           
            real_value=list(real.values()) 
            real_key=list(real.keys()) 
           
            if real!=self.old_real: 
                self.old_real=real
                self.signal_real.emit(real_key,real_value)
            

            docs=db.collection('axis').get()
            for x in docs: axis=x.to_dict()
            
            axis_value=list(axis.values()) 
            axis_key=list(axis.keys()) 
            
            if axis!=self.old_axis:  
                self.old_axis=axis
                self.signal_axis.emit(axis_key,axis_value)
            

            document=db.collection('hmi').get()
            for x in document: hmi=x.to_dict()
           
            hmi_value=list(hmi.values()) 
            hmi_key=list(hmi.keys()) 
            
            if hmi!=self.old_hmi:
                self.old_hmi=hmi 
                self.signal_hmi.emit(hmi_key,hmi_value)


            documents=db.collection('user').get()
            for x in documents: user=x.to_dict()
            
            user_value=list(user.values()) 
            user_key=list(user.keys()) 
            
            if user!=self.old_user:
                self.old_user=user
                self.signal_user.emit(user_key,user_value)

            
            