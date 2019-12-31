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

plt.title("GDP per person employed")   # 设置标题
plt.xlabel("Year",fontsize=14, color='blue') # 横轴标题
plt.ylabel("USD",fontsize=14, color='blue')  # 纵轴标题，可以设置字体大小和字体颜色
plt.grid(True)


x = couXList
y =  yItem
y2 = Utility.TestUtility.getCountryByNameList('Belgium')

# plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, y2)
label = ["Australia", "Austria"]
plt.legend(label, loc = 0, ncol = 2)
plt.show()
