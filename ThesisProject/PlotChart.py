import numpy as np
import matplotlib.pyplot as plt
import Utility

couArray = Utility.TestUtility.getDBCountryList()
couXList = list(couArray.keys())
couXList = list(map(int, couXList))
couYList = list(couArray.values())
couYList = list(map(float, couYList))
yItem = []
for i in couYList:
    yItem.append(int(i))

plt.title("GDP per person employed")
plt.xlabel("Year",fontsize=14, color='blue')
plt.ylabel("USD",fontsize=14, color='blue')
plt.grid(True)



x = couXList
y =  yItem
devCouList = Utility.TestUtility.getDevCountryList()
yCouItem = []
for i in range(0,devCouList.__len__()):
    couStrName = "".join(devCouList[i])
    yCouItem.append(Utility.TestUtility.getCountryByNameList(couStrName))

plt.plot(x, y)
for item in yCouItem:
    plt.plot(x, item)

label = devCouList
plt.legend(label, loc = 0, ncol = 2)
plt.show()
