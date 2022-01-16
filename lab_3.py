import numpy as np
import matplotlib.pyplot as plt 

def ermite(Ax,Ay,Bx,By,prA,prB): 
    xe=np.arange(Ax,Bx+0.01,0.01)
    h=Bx-Ax
    fxde=[]
    for xde in xe: 
        koef=(xde-Ax)/h
        h3=(1-3*(koef**2)+2*(koef**3))*Ay+(3*(koef**2)-2*(koef**3))*By+(koef-2*(koef**2)+(koef**3))*prA*h+(-(koef**2)+(koef**3))*prB*h
        fxde.append(h3)
#        возвращаем два списка с координатами точек по эрмиту
    return xe,fxde

 
def calc():
#        получаем коээф. k
    k = 10
#        получаем разбиения
    n = 3
#      
    xi=[]
#        равномерная сетка
   
    for i in range(0,n+1): 
        xi.append(-1+i*(2/n))
    fxi=[]
    prxi=[]

#        вычисляем значение функции и производной в точках разбиения
    for xd in xi: 

        fxi.append(1/(1+(5+k)*(xd**2)))
        prxi.append(-(2*(k+5)*xd)/((k+5)*(xd**2)+1)**2)
        # prxi.append((xd-10+k)/2)

#        попарно передаем точки, производные в точках и значения функции в метод вычисляющий многочлен эрмита
#        полученные два списка наносим на график
    for i in range(len(xi)-1):  
        x,y=ermite(xi[i],fxi[i],xi[i+1],fxi[i+1],prxi[i],prxi[i+1])
        plt.plot(x,y)
        plt.plot(xi[i],fxi[i],'o')
        plt.plot(xi[i+1],fxi[i+1],'o')

#        на отрезке [-1,1] находим абсциссы и ординаты для отображения иходного графика функции
    xfunc=np.arange(-1,1+0.01,0.01)
    yfunc=(1/(1+(5+k)*(xfunc**2)))
    plt.plot(xfunc,yfunc, color="gray",alpha=0.5,label='f(x)=1/(1+(5+k)*x^2)')
    plt.show()

calc()