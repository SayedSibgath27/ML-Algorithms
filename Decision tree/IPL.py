from tkinter import*
from tkinter import PhotoImage
from PIL import Image,ImageTk
from sklearn.model_selection import train_test_split #This package divide the into traning and testing data 
from sklearn.tree import DecisionTreeClassifier
from tkinter import ttk
from sklearn import tree
from sklearn import metrics
from tkinter import messagebox
import pandas as pd






def predict():
    t1_value=t1.get()
    t2_value=t2.get()
    t3_value=t3.get()
    option_value=option.get()
    score=int(e1.get())
    #Check that user has entered empty value or not 
    if(t1_value==""or t2_value==""or t3_value==""or option_value==""):
        messagebox.showwarning('Warning',"Choose aprox value")
    else:
        
    
    
        print(t1_value,t2_value,t3_value,option_value,score)
        coloum_name=['TeamA','TeamB','Toss 1','Firstinnings','Winner','Option']
        
        #Apply machine learning Algorythm
        data=pd.read_excel("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\MLalgorythm\\Decission tree\\database.xlsx",header=None,names=coloum_name)
        print(data)
        feature_coloumn=['TeamA','TeamB','Toss 1','Firstinnings','Option']
        x=data[feature_coloumn]
        y=data.Winner
        print(x,y)
        
        
        #Divde the data into two set
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
        model=DecisionTreeClassifier()
        traning_data=model.fit(x_train,y_train)
        tree.plot_tree(traning_data)
        
        predictedvalue=model.predict(x_test)
        accuracy=metrics.accuracy_score(y_test,predictedvalue)
        print(accuracy)
        
        #Predict the output for given input
        if(t1_value=="RCB"):
            t1_valuee=0
        if(t1_value=="CSK"):
            t1_valuee=1
        if(t1_value=="KIIP"):
            t1_valuee=2
        if(t1_value=="KKR"):
            t1_valuee=3
            
        if(t2_value=="RCB"):
            t2_valuee=0
        if(t2_value=="CSK"):
            t2_valuee=1
        if(t2_value=="KIIP"):
            t2_valuee=2
        if(t2_value=="KKR"):
            t2_valuee=3
            
        if(t3_value=="RCB"):
            t3_valuee=0
        if(t3_value=="CSK"):
            t3_valuee=1
        if(t3_value=="KIIP"):
            t3_valuee=2
        if(t3_value=="KKR"):
            t3_valuee=3
        
        if(option_value=="Batting"):
            option_valuee=1
        else:
            option_valuee=0
        a_list=[t1_valuee,t2_valuee,t3_valuee,option_valuee,score]
        new_a_list=pd.DataFrame(a_list)
        
        new_a=new_a_list.T
        result=model.predict(new_a)
        print(result)
        
        
        
        if (result==0):
            print(t1_valuee)
            if t1_valuee==0:
                print("RCB will win the match")
                result_label.configure(text="RCB will win the match")
        if (result==0):
            print(t1_valuee)
            if t1_valuee==2:
                print("CSK will win the match")
                result_label.configure(text="CSK will win the match")
        if (result==0):
            print(t1_valuee)
            if t1_valuee==3:
                print("KKR will win the match")
                result_label.configure(text="KKR will win the match")

                
                
        if (result==0):
            print(t2_valuee)
            if t2_valuee==0:
                print("RCB will win the match")
                result_label.configure(text="RCB will win the match")
        if (result==0):
            print(t2_valuee)
            if t2_valuee==2:
                print("CSK will win the match")
                result_label.configure(text="CSK will win the match")
        if (result==0):
            print(t2_valuee)
            if t2_valuee==3:
                print("KKR will win the match")
                result_label.configure(text="KKR will win the match")
        else:
            print(t2_valuee)
   
        
   
    
w=Tk()
w.geometry('1550x1550')
#image=PhotoImage(file="C:\\Users\\Sayed Sigbath\\Desktop\\Python\\MLalgorythm\\Decission tree\\Background.jpg")

image=Image.open("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\MLalgorythm\\Decission tree\\Background.jpg")
image.thumbnail((1550,1550),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
photo_label=Label(w,image=photo)
photo_label.place(x=0,y=0)

team1=['CSK','RCB','KIIP','KKR']
team2=['CSK','RCB','KIIP','KKR']

t1_label=Label(w,text="Choose Team1")
t1_label.place(x=400,y=100)

t1=StringVar()
c1=ttk.Combobox(w,textvariable=t1)
c1['value']=tuple(team1)
c1.current(1)
c1.place(x=500,y=100)

t2_label=Label(w,text="Choose Team2")
t2_label.place(x=400,y=140)

t2=StringVar()
c2=ttk.Combobox(w,textvariable=t2)
c2['value']=tuple(team2)
c2.current(1)
c2.place(x=500,y=140)

t3_label=Label(w,text="Toss Won")
t3_label.place(x=400,y=180)

t3=StringVar()
c3=ttk.Combobox(w,textvariable=t3)
c3['value']=tuple(team1)
c3.current(1)
c3.place(x=500,y=180)


option=StringVar()
r1=Radiobutton(w,text="Batting",variable=option,value="Batting")
r1.place(x=400,y=220)


r2=Radiobutton(w,text="Bowling",variable=option,value="Bowling")
r2.place(x=580,y=220)

t4_label=Label(w,text="First inning score")
t4_label.place(x=400,y=260)

e1=Entry(w)
e1.place(x=580,y=260)

button=Button(w,text="Predict",command=predict)
button.place(x=400,y=300)

result_label=Label(w,text="No data found")
result_label.place(x=400,y=350)


w.mainloop()