
from opcua import Client
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred)
client = Client("opc.tcp://192.168.100.100:4840")
db=firestore.client()

table1,table2,table3=[],[],[]

def get_variable(name):
    result=client.get_node(name).get_value()
    print(f"Variable is {result}")
    return result  

def print_series(data,index):
    serie=pd.Series(data,index)
    print(serie,"\n")

def print_dataframe(data,index,column):
    df=pd.DataFrame(data,index,column)
    print(df)
    print("\n\n")
    return df

def make_excel_table(df,var):
    name="excel"+str(var)+".csv"
    df.to_csv(name)

def del_data(range1,table):
    for x in range(range1):
        del table[0:range1]


try:
    client.connect()
    print("It is connected")

    adress_axis= ["LeavePos[0]","LeavePos[1]","LeavePos[2]","LeavePos[3]","LeavePos[4]","LeavePos[6]","LeavePos[7]","LeavePos[8]","LeavePos[9]","LeavePos[10]"]
    adress_user= ["1_UsableCurrent","2_UsableCurrent","3_UsableCurrent","4_UsableCurrent","5_UsableCurrent","6_UsableCurrent","7_UsableCurrent","8_UsableCurrent","9_UsableCurrent"]
    adress_hmi = ["FeederEntryCounter","FeederPushCounter","GripperLeaveCount","MachineRunType","MachineStatus","Product_counter","PusherRows"]

    while True:
        try:
            print("\nAXIS \n") 
            for x in adress_axis:
                restore_axis="ns=2;s=Application.RestoreAxisPosition.Grp_aiOffsetGripperX_"+str(x)
                val_axis=get_variable(restore_axis)
                table1.append(val_axis)
                time.sleep(0.1)
            
            print("\nUSER \n")
            for y in adress_user:
                user="ns=2;s=Application.GVL_User.G_diDriver"+str(y)
                val_user=get_variable(user)
                table2.append(val_user)
                time.sleep(0.1)

            print("\nHMI \n")
            for z in adress_hmi:
                hmi="ns=2;s=Application.GVL_Hmi.HMI_i"+str(z)
                val_hmi=get_variable(hmi)
                table3.append(val_hmi)
                time.sleep(0.1)
        
            real=client.get_node("ns=2;s=Application.GVL_Hmi.Hmi_uiBoxUsrCounter").get_value()

            print(table1,"\n",table2,"\n",table3)    

            print_series(table1,adress_axis)
            print_series(table2,adress_user)
            print_series(table3,adress_hmi)
            print(real)

        
            df=print_dataframe(table1,adress_axis,['numbers'])
            df1=print_dataframe(table2,adress_user,['numbers'])
            df2=print_dataframe(table3,adress_hmi,['numbers'])

            make_excel_table(df,1)
            make_excel_table(df1,2)
            make_excel_table(df2,3)

            hmi_dic = dict(zip(adress_hmi, table3))
            user_dic = dict(zip(adress_user, table2))
            axis_dic = dict(zip(adress_axis, table1))
            real_dic={
                "counter":real
            } 

            print("COMING ...")

            db.collection('hmi').document().set(hmi_dic)   
            db.collection('user').document().set(user_dic)
            db.collection('axis').document().set(axis_dic)
            db.collection('real').document().set(real_dic)

            if len(table1)>0 and len(table2)>0 and len(table3)>0:    
                del_data(len(table1),table1)
                del_data(len(table2),table2)
                del_data(len(table3),table3)

            print("DELETING...")
            time.sleep(4)

            del_axis=db.collection('axis').get()
            for doc in del_axis:
                key=doc.id
                db.collection('axis').document(key).delete()

            del_hmi=db.collection('hmi').get()
            for doc in del_hmi:
                key=doc.id
                db.collection('hmi').document(key).delete()

            del_user=db.collection('user').get()
            for doc in del_user:
                key=doc.id
                db.collection('user').document(key).delete()
        
            del_real=db.collection('real').get()
            for doc in del_real:
                key=doc.id
                db.collection('real').document(key).delete()
        
        except:
            cred = credentials.Certificate("serviceAccountkey.json")
            firebase_admin.initialize_app(cred)
            client = Client("opc.tcp://192.168.100.100:4840")
            continue       

    
except:
    print("It is Not connected!!!")
    client.disconnect()