import pandas as pd
from sklearn.model_selection import train_test_split #This package divide the into traning and testing data 
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics

#Assigne coloum name to data set. 
coloum_name=['outlook','temprature','humidity','windy','result']



data=pd.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\MLalgorythm\\Decission tree\\actual_input.xlsx',header=None,names=coloum_name)
#print(data)

#Divide the data into features and result
feature_coloum=['outlook','temprature','humidity','windy']
x=data[feature_coloum]
#print(x)

y=data.result
#print(y)

#Divide the data into traning data and testing data
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=1)
print(type(x_test))

#Creat a decission tree model
model=DecisionTreeClassifier()
#provide traning to your model
traning_result=model.fit(x_train,y_train)
tree.plot_tree(traning_result)

#Calculate the accuracy of the model
predected_value=model.predict(x_test)


#Calcualte Accuracy
accuracy=metrics.accuracy_score(y_test,predected_value)
#print(accuracy)


#Give the random input from user to machine learning algorythm
outlook=1
temprature=2
humidity=3
windy=4

#Convert it into a data frame
a_list=[outlook,temprature,humidity,windy]
new_a_list=pd.DataFrame(a_list)
#print(new_a_list)

#Transpose the matrix
new_a=new_a_list.T #T property is called transpose the property 
#print(new_a)

predected_value=model.predict(new_a)
print(predected_value)


