import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.figure()
plt.plot(x,y,label="Square Numbers")
plt.title('Simple Plot')
plt.xlabel('Value')
plt.ylabel('Value')
#显示图列
plt.legend()
#显示图形
plt.show()