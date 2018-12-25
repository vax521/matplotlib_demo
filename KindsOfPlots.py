import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

x = np.linspace(-3,3,200)
y1 = 2*x + 1
y2 = x**2
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2)
plt.xlim(-1,2)
plt.ylim(-2,3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

new_ticks = np.linspace(-1,2,5)

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--', label='linear line')
plt.plot(x,y2, label='square line')
plt.xlim(-1,2)
plt.ylim(-2,3)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$great$'])
# 获取当前坐标轴信息
ax = plt.gca()
ax.spines['left'].set_color('red')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_color('blue')
ax.spines['bottom'].set_position(('data',0))
plt.legend(loc='upper right')
plt.show()

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
# 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
plt.show()

# 散点图
n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value

plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.xlim(-1.5,1.5)
plt.xticks()
plt.ylim(-1.5,1.5)
plt.yticks()
plt.show()

# 柱状图
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X,Y1)
plt.bar(X,-Y2)
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x,y in zip(X, Y2):
    plt.text(x+0.4,-y-0.05, '%.2f'%y, ha='center',va='bottom')
plt.show()

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 1250
x = np.linspace(-10,10,n)
y = np.linspace(-10,10,n)
X,Y = np.meshgrid(x,y)
plt.contour(X,Y,f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
plt.show()

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=0.92)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
plt.show()

