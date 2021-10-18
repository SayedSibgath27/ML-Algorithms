import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


data=pd.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\MLalgorythm\\Decission tree\\second_input.xlsx')
print(data)

outlook=data['outlook']
outlook=list(outlook)
#print(outlook)


#Convert the string to interger 
pobj=preprocessing.LabelEncoder()#It convert string to interger 
actual_outlook=pobj.fit_transform(outlook)
print(actual_outlook)

temperature=data['temperature']
temperature=list(temperature)
#print(temperature)

actual_temperature=pobj.fit_transform(temperature)
print(actual_temperature)

humidity=data['humidity']
humidity=list(humidity)
#print(humidity)


actual_humidity=pobj.fit_transform(humidity)
print(actual_humidity)


windy=data['windy']
windy=list(windy)
#print(windy)

actual_windy=pobj.fit_transform(windy)
print(actual_windy)


play=data['play']
play=list(play)
#print(play)


actual_play=pobj.fit_transform(play)
print(actual_play)


#Combine all the feature into single feature
allfeature=list(zip(actual_outlook,actual_temperature,actual_humidity,actual_windy))

print(allfeature)
result=list(actual_play)
print(result)

#Apply the MLAlgorythm
model=KNeighborsClassifier(n_neighbors=3)
#Train the model 
traning_data=model.fit(allfeature,actual_play)
print(traning_data)


#Predict the value
predicted_value=model.predict([[1,2,3,4]])
print(predicted_value)

