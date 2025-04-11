# %%
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5,6,7,234,634,6,2])
plt.ylabel('y label')
plt.xlabel("x label")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
print(x)
plt.plot(x**2)

# %%
x = np.arange(10)
plt.plot(x**2)
plt.axis([0,100,0,100]) # x축을 0~100, y축을 0~100

# %%
x = np.arange(-20,20)
y1 = 2*x
y2 = (1/3) * x ** 2+5
y3 = -x ** 2 -5
plt.plot(x,y1,'g--',x,y2,'r^-',x,y3,'b*:') # 색 지정 선 모양지정
plt.axis([-30,30,-30,30])

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,np.pi * 2,100)
fig = plt.figure()
print(plt.style.available) # 적용가능 스타일 확인
# plt.style.use('seaborn-v0_8-whitegrid') # 스타일 적용
plt.title("sin_cos-curve")
plt.plot(x,np.sin(x),'r-',label='sin curve')
plt.plot(x,np.cos(x),'b:',label = 'cosin curve')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend(loc="best") # 위치 지정 가능

fig.savefig('sin_cos_fig.png')
from IPython.display import Image
Image('sin_cos_fig.png')

# %% [markdown]
# # 마크다운 입니다
# ## ㅁ
# ### 3
# #### 3
# *   1
# *   1
# *   1

# %%
# plot은 매개변수로 x,y축을 받는데 하나의 배열의 형태로 넣으면 이걸 y축의 나열로 잡고 x축은 자동으로 잡아춤
plt.plot([2,3,4],[4,9,16],c='red')
plt.axis([0,20,0,20]) #(x시작점,x끝점,y시작점,y끝점)을 위미
plt.show()

# %%
# Scatter()
x=np.arange(0,10,1)
plt.axis([0,10,0,100])
plt.scatter(x,x**2,c='red',s=10)
plt.text(3,50,'y=x^2 graph')
plt.annotate('annotate',xy=(2,4),xytext=(5,20),arrowprops={"color":"green"})
plt.show()

# %%
x=np.arange(0,10,1)
plt.axis([0,10,0,100])
plt.plot(x,x**2,c="b",lw=5,ls="--",marker="o",ms=15,mec="g",mew=5,mfc="r")
plt.text(3,50,'y=x^2 graph')
plt.annotate('annotate',xy=(2,4),xytext=(5,20),arrowprops={"color":"green"})
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

# 한글 깨짐 해결
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

triXAxis = np.linspace(-4,4,100) # 범위 지정 (시작,끝,100개로 나눔)
sinYAxis = np.sin(triXAxis)
cosYAxis = np.cos(triXAxis)
plt.plot(triXAxis,sinYAxis)
plt.plot(triXAxis,cosYAxis)
plt.xticks([-4,-2,0,2,4])
plt.yticks([1,0,-1])
plt.title("Trigonometric Functions")
plt.show()

# %%
# 서브플롯(행의갯수,열의갯수,위치)
plt.subplot(211).set(xticks=[-4,-2,0,2,4],yticks=[-1,0,1])
triXAxis = np.linspace(-4,4,100)
sinYAxis = np.sin(triXAxis)
cosYAxis =  np.cos(triXAxis)
plt.plot(triXAxis,sinYAxis)
plt.plot(triXAxis,cosYAxis)
plt.title("Trigonometric Functions")

plt.subplot(212).set(xlim=[0,8],ylim=[0,3])
logXAxis = np.linspace(1,10,100)
logYAxis = np.log(logXAxis)
plt.plot(logXAxis,logYAxis)
plt.title("Log Functions")
plt.legend()
plt.show()

# %%
#matplotlib는 두가지 방식의 api제공 (pyplotapi,객체 지향 api)
x = np.linspace(0,1,50)
y1 = np.cos(4%np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

plt.plot(x,y1,'r-*',lw=1)
plt.plot(x,y2,'b--',lw=1)

# %%
x = np.linspace(0,1,50)
y1 = np.cos(4%np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

fig = plt.figure()
ax = fig.subplots()
ax.plot(x,y1,'r-*',lw=1)
ax.plot(x,y2,'b--',lw=1)

# %%
fig ,ax=plt.subplots(2,2)

X =  np.random.randn(100)
Y = np.random.randn(100)
ax[0,0].scatter(X,Y)
X =  np.arange(10)
Y = np.random.uniform(1,10,10)
ax[0,1].bar(X,Y)
X =  np.linspace(0,10,100)
Y=np.cos(X)
ax[1,0].plot(X,Y)
Z= np.random.uniform(0,1,(5,5))
ax[1,1].imshow(Z)
# pyplot은 subplot 에서 넘버링 1,2
# 객체지향은 subplot에서 넘버링 0,2

# %%
fig,axes = plt.subplots(3,4)
axes[1,2].plot([1,2,3,4]) # subplots으로 반환한 axes는 배열처럼 접근가능
axes[2][1].bar([1,2,3,4],[1,2,3,4])
plt.tight_layout() # subplot간 margin(여백으로 이해)이 겹치지 않게하는 함수
plt.show()

# %%
fig,ax = plt.subplots(1,2)
fig.suptitle('figure title')
ax[0].set_title('ax[0] title')
ax[1].set_title('ax[1] title')
plt.tight_layout()
plt.show()

# %%
ax221 = plt.subplot(2,2,1)
ax222 = plt.subplot(2,2,2)
ax212 = plt.subplot(2,1,2)

ax221.scatter([1,2,3],[3,2,1])
ax212.plot([1,2,3,4,5])
plt.tight_layout()
plt.show()

# %%
N = 30
X = np.random.rand(N)
Y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
plt.scatter(X,Y,s=area,c = colors, alpha=0.5)

# %%
x = np.arange(3)
years = ['2010','2011','2012']
domestic = [6801,7695,8010]
foreign = [777,1046,1681]

plt.bar(x,domestic)
plt.bar(x,foreign)
plt.xticks(x,years)
plt.show()

# %%
y= np.arange(3)
years = ['2010','2011','2012']
x = [1,3,5]
x2=[2,4,6]
domestic = [6801,7695,8010]
foreign = [777,1046,1681]
width=0.3
plt.barh(x,domestic,width)
plt.barh(x2,foreign,width)
plt.yticks(x,years)
plt.show()

# %%
data = [5,4,6,11]
clist = ['cyan','gray','orange','red']
explode = [.06,.07,.09,.09]
plt.pie(data,autopct = '%.2f%%',colors=clist,labels=clist,explode=explode)

# %%
data = np.random.random((10,10))
plt.imshow(data,cmap="cool")
plt.colorbar()

# %%
# 히스토그램
heights = np.random.normal(165 ,7,(300))
plt.hist(heights, bins=60)
plt.xlabel("heights")
plt.ylabel("frequency")
plt.show()

# %%
f1 = np.random.normal(loc=0,scale=1,size=100000)
f2 = np.random.normal(loc=3,scale=50,size=100000)

plt.hist(f1,bins=200,color='red',alpha=.7,
         label = 'loc=0,scale=1')
plt.hist(f2,bins=200,color='blue',alpha=.5,
         label = 'loc=3,scale=.5')

# %%
# 상자 수염 그리기
np.random.seed(85)
data1 = np.random.normal(100,10,200) # 평균이 100이고 분산이 10
data2 = np.random.normal(100,40,200)
data3 = np.random.normal(80,40,200)
data4 = np.random.normal(80,60,200)
plt.boxplot([data1,data2,data3,data4])

# %%



