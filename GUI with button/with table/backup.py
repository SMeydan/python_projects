import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred=credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

while True:
    class MainWindow(QMainWindow):
        
        def __init__(self,old_axis=None,old_axis_k=None,old_hmi=None,old_hmi_k=None,old_user=None,old_user_k=None,old_real=None,old_real_k=None,axis_list=None,axis_value_list=None,hmi_list=None,hmi_value_list=None,user_list=None,user_value_list=None,real_list=None,real_value_list=None,real=None,user=None,hmi=None,axis=None):
            super(MainWindow,self).__init__()
            loadUi("basic.ui",self)

            self.setcols(115,0)
            self.setcols(110,1)
            
            self.old_axis,self.old_axis_k=[],[]
            self.old_hmi,self.old_hmi_k=[],[]
            self.old_user,self.old_user_k=[],[]
            self.old_real,self.old_real_k=[],[]

            self.axis_list,self.axis_value_list=[],[]
            self.hmi_list,self.hmi_value_list=[],[]
            self.user_list,self.user_value_list=[],[]
            self.real_list,self.real_value_list=[],[]
            
            self.real,self.axis,self.hmi,self.user={},{},{},{}
            
            self.pushButton_2.clicked.connect(self.deletedata)
            self.loaddata()

        def deletedata(self):

            self.rowCount(0,0)
            self.rowCount(0,1)
            self.loaddata() 


        def setcols(self,width,num):
            if num==0:
                for x in range(0,5):
                    self.tableWidget.setColumnWidth(x,width)
            else:
                for x in range(0,1):        
                    self.tableWidget_2.setColumnWidth(x,width)

       
        def rowCount(self,num,x):
            if x==0:
                self.tableWidget.setRowCount(num)
            else:
                self.tableWidget_2.setRowCount(num)

        
        def setItem(self,num,key,value):
             for x in range(len(key)):
                    self.tableWidget.setItem(x,num,QtWidgets.QTableWidgetItem(str(key[x])))
                    self.tableWidget.setItem(x,num+1,QtWidgets.QTableWidgetItem(str(value[x])))                  
       
        def loaddata(self):

            self.rowCount(10,0)
            self.rowCount(1,1)

            doc=db.collection('real').get()
            for x in doc:
                self.real=x.to_dict()
                self.real_value_list=list(self.real.values())
                if self.real_value_list==[]:
                    self.real_list=self.old_real_k
                    self.real_value_list=self.old_real
                else:
                    self.real_list=list(self.real.keys())
                    self.real_value_list=list(self.real.values())
                break
            if self.real_value_list!=[]:
                self.tableWidget_2.setItem(0,1,QtWidgets.QTableWidgetItem(str(self.real["counter"])))
                self.tableWidget_2.setItem(0,0,QtWidgets.QTableWidgetItem("counter")) 
             
            docs=db.collection('axis').get()
            for x in docs:
                self.axis=x.to_dict()
                self.axis_value_list=list(self.axis.values())
                if self.axis_value_list==[]:
                    self.axis_list=self.old_axis_k
                    self.axis_value_list=self.old_axis
                else:
                    self.axis_list=list(self.axis.keys())
                    self.axis_value_list=list(self.axis.values())
                break
            if self.axis_value_list!=[]:
                self.setItem(2,self.axis_list,self.axis_value_list)
             
            dox=db.collection('hmi').get()
            for x in dox:
                self.hmi=x.to_dict()
                self.hmi_value_list=list(self.hmi.values())
                if self.hmi_value_list==[]:
                    self.hmi_list=self.old_hmi_k
                    self.hmi_value_list=self.old_hmi
                else:
                    self.hmi_list=list(self.hmi.keys())
                    self.hmi_value_list=list(self.hmi.values())
                break
            if self.hmi_value_list!=[]:
                self.setItem(0,self.hmi_list,self.hmi_value_list)
            
            doxs=db.collection('user').get()
            for x in doxs:
                self.user=x.to_dict()
                self.user_value_list=list(self.user.values())
                if self.user_value_list==[]:
                    self.user_list=self.old_user_k
                    self.user_value_list=self.old_user
                else:
                    self.user_list=list(self.user.keys())
                    self.user_value_list=list(self.user.values())
                break
            if self.user_value_list!=[]:
                self.setItem(4,self.user_list,self.user_value_list)
            
            self.l1.setText(str(sum(self.hmi_value_list)))
            self.l2.setText(str(sum(self.user_value_list)))
            self.l3.setText(str(sum(self.axis_value_list))) 
            
            if self.hmi_value_list!=[]:
                self.old_hmi=self.hmi_value_list 
                self.old_hmi_k=self.hmi_list    
            
            if self.axis_value_list!=[]:
                self.old_axis=self.axis_value_list
                self.old_axis_k=self.axis_list
            
            if self.user_value_list!=[]:
                self.old_user=self.user_value_list
                self.old_user_k=self.user_list
            
            if len(self.real) > 0:
                self.old_real=self.real.values()
               
            print(self.old_user)
            print(self.old_real) 



    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(890)
    widget.setFixedWidth(950)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")    
