# Apply the linear regression on age and weight

#import the mathamatical module from 
from scipy import stats #it is called stats module 
import matplotlib.pyplot as plt
def calculate(x):
    return slope*x+intercept

x=[1,2,3,4,5]
y=[20,50,40,30,50]

#calculate the slope and intercept
slope,intercept,r,p,sd=stats.linregress(x,y)
#apply the algorythm
model=list(map(calculate,x))
plt.plot(x,y)

#calculate the result for given value of x
nx=[0,10]
#Predict the value
ny=list(map(calculate,nx))
print(ny)
plt.plot(nx,ny,color="red")
plt.show()
