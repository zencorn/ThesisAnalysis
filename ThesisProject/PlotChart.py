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

plt.title('AustraliaNew')

x = couXList
y =  yItem
y2 = Utility.TestUtility.getCountryByNameList('Belgium')
# # plt.plot(,couYList[0:5])
# plt.scatter(x, y)



plt.plot(x, y)
plt.plot(x, y2)
# plt.axis('tight')
plt.show()
