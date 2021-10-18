from tkinter import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from scipy import stats  
import matplotlib.pyplot as plt

application=Tk()

def predict():
    def predictvalue(H_list,W_list):
        #Apply alogorythm
        def calculate(x):
            return slope*x+intercept
        x=H_list
        y=W_list
        
        #calculate the slope and intercept
        slope,intercept,r,p,sd=stats.linregress(x,y)        #apply the algorythm
        model=list(map(calculate,x))
        plt.plot(x,y)
        plt.plot(x,model,color='green')
        
        #Calculate the weight for given height
        nx=[0,int(height_value)]
        #Predict the value
        ny=list(map(calculate,nx))
        print(ny)
        plt.plot(nx,ny,color="red")
        plt.show()
        p_data=ny[-1]
        figure=plt.Figure(figsize=(6,5),dpi=100)
        ax=figure.add_subplot()
        bargraph=FigureCanvasTkAgg(figure,application)
        Graph=bargraph.get_tk_widget()
        Graph.place(x=700, y=160)
        df=pd.DataFrame({'height':H_list,'Weight':W_list})
        df.plot(x='height',y='Weight', color='red', legend=True,ax=ax)
        df=pd.DataFrame({'height1':H_list,'Weight1':model})
        df.plot(x='height1',y='Weight1', color='green', legend=True,ax=ax)
        df=pd.DataFrame({'height2':nx,'Weight2':ny})
        df.plot(x='height2',y='Weight2', color='blue', legend=True,ax=ax)
        
        if int(p_data)>int(weight_value):
            label=Label(application, text="Under Weighted", font=150)
            label.place(x=340,y=360)
        else:
            label=Label(application, text="Over Weighted", font=150)
            label.place(x=340,y=360)
        
        
    #Read the data from the server 
    data=pd.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\MLalgorythm\\Linear Regression\\Actualdataset.xlsx')
    #print(data)
    
    height=data['height']
    height_list=list(height)
    print(height_list)
    
    Mweight=data['Male_Weight']
    Mweight_list=list(Mweight)
    print(Mweight_list)
    
    
    Fweight=data['Female_Weight']
    Fweight_list=list(Fweight)
    print(Fweight_list)
    
    #Read a adata from the interface
    gender_value=gender.get()
    height_value=name1.get()
    weight_value=name2.get()
    print(gender_value)
    print(height_value)
    print(weight_value)
    
    if gender_value=="Male":
        predictvalue(height_list,Mweight_list)
    else:
        predictvalue(height_list,Fweight_list)
    
    
    
    
figure=plt.Figure(figsize=(6,5),dpi=100)
ax=figure.add_subplot()
bargraph=FigureCanvasTkAgg(figure,application)
Graph=bargraph.get_tk_widget()
Graph.place(x=700, y=160)


application.geometry('1550x1500')


l1=Label(application,text="Weight Prediction", font=500)
l1.place(x=700,y=60)

g1=Label(application,text="Choose your gender", font=300)
g1.place(x=300,y=115)

#Creat a radio button
gender=StringVar()
gender.set(FALSE)
r1=Radiobutton(application,text="Male",font=300, variable=gender,value="Male")
r1.place(x=320,y=150)

r2=Radiobutton(application,text="Female",font=300, variable=gender,value="Female")
r2.place(x=320,y=180)

H1=Label(application,text="Enter your height", font=300)
H1.place(x=300,y=240)

name1=Entry(application)
name1.place(x=320,y=280)


W1=Label(application,text="Enter your weight", font=300)
W1.place(x=500,y=240)

b1=Button(application,text="Predict",command=predict)
b1.place(x=340,y=320)

name2=Entry(application)
name2.place(x=520,y=280)


application.mainloop()