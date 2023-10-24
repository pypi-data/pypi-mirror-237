class posos:
    def smeshnoy(task=''):
        #1
        sklad = {
            'в группе учатся. дисперсию центральный момент':'В группе Ω учатся 27 студентов, Ω={1,2,...,27}. Пусть X(i) – 100-балльная оценка студента i∈Ω.\n\
            Из группы Ω случайным образом 7 раз выбирается студент ω∈Ω.\n\
Повторный выбор допускается. Пусть ωj – студент, полученный после выбора j=1,...,7, X(ωj) – его оценка. Среднюю оценку на случайной выборке\n\
обозначим X¯¯¯¯=17∑X(ωj). Оценки в группе даны: 100, 86, 51, 100, 95, 100, 12, 61, 0, 0, 12, 86, 0, 52, 62, 76, 91, 91, 62, 91, 65, 91, 9, 83, 67, 58, 56.\n\
Требуется найти: 1) дисперсию Var(X¯¯¯¯); 2) центральный момент μ3(X¯¯¯¯).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
grades = [100, 86, 51, 100, 95, 100, 12, 61, 0, 0, 12, 86, 0, 52, 62, 76, 91, 91, 62, 91, 65, 91, 9, 83, 67, 58, 56]\n\
k = 7\n\
\n\
grades = np.array(grades)\n\
n = len(grades)\n\
\n\
var = grades.var() / k\n\
var #дисперсия\n\
\n\
mu3 = np.sum((grades - grades.mean()) ** 3) / n / k ** 2\n\
mu3 #центр.момент\n\
\n\
moment(grades, 3) / k ** 2 # тоже ценетр. момент'
            ,
            'в группе учатся. математическое ожидание дисперсию':'В группе Ω учатся 27 студентов, Ω={1,2,...,27}. Пусть X(i) – 100-балльная оценка студента i∈Ω.\n\
            Из группы Ω случайным образом 6\n\
раз выбирается студент ω∈Ω. Повторный выбор не допускается. Пусть ωj – студент, полученный после выбора j=1,...,6 , X(ωj)– его оценка.\n\
Среднюю оценку на случайной выборке обозначим X¯¯¯¯=16∑X(ωj).\n\
Оценки в группе даны: 100, 78, 77, 51, 82, 100, 73, 53, 78, 55, 7, 0, 81, 15, 96, 12, 71, 70, 53, 0, 73, 100, 55, 100, 59, 89, 81.\n\
Требуется найти: 1) математическое ожидание E(X¯¯¯¯); 2) дисперсию Var(X¯¯¯¯).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
grades = [100, 78, 77, 51, 82, 100, 73, 53, 78, 55, 7, 0, 81, 15, 96, 12, 71, 70, 53, 0, 73, 100, 55, 100, 59, 89, 81]\n\
k = 6\n\
\n\
grades = np.array(grades)\n\
n = len(grades)\n\
\n\
E = grades.mean()\n\
E #матожидание\n\
\n\
Var = grades.var() / k * (n - k) / (n - 1)\n\
Var #дисперсия'
            ,
            'распределение баллов на. математическое ожидание стандартное отклонение':'Распределение баллов на экзамене до перепроверки задано таблицей. Оценка работы Число работ 2 7     3 48    48 5    10 5.\n\
Работы будут перепроверять 6 преподавателей, которые разделили все работы между собой поровну случайным образом.\n\
Пусть X¯¯¯¯ – средний балл (до перепроверки) работ, попавших к одному из преподавателей. Требуется найти:\n\
1) математическое ожидание E(X¯¯¯¯); 2) стандартное отклонение σ(X¯¯¯¯).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
vals = [2] * 7 + [3] * 48 + [4] * 8 + [5] * 105\n\
k = 6\n\
\n\
vals = np.array(vals)\n\
n = len(vals)\n\
k = n / k\n\
\n\
E = vals.mean()\n\
E # матожидание\n\
\n\
Var = vals.var() / k * (n - k) / (n - 1)\n\
std = np.sqrt(Var)\n\
std # стандарт. отклонение'
            ,
            'две игральные кости. математическое ожидание стандартное отклонение':'Две игральные кости, красная и синяя, подбрасываются до тех пор, пока не выпадет 19 различных (с учетом цвета) комбинаций очков.\n\
Пусть Ri – число очков на красной кости, а Bi – число очков на синей кости в комбинации с номером i. Случайные величины Xi\n\
задаются соотношениями: Xi=11Ri−9Bi,i=1,...,19. Среднее арифметическое этих величин обозначим X¯¯¯¯=119∑Xi.\n\
Требуется найти: 1) математическое ожидание E(X¯¯¯¯); 2) стандартное отклонение σ(X¯¯¯¯).\n\
import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
k = 19\n\
n = 36\n\
\n\
combs = [(r, b) for r in range(1, 7) for b in range(1, 7)]\n\
combs = np.array(combs)\n\
mean, var = combs.mean(axis=0), combs.var(axis=0)\n\
mean, var\n\
\n\
E = 11 * mean[0] - 9 * mean[1]\n\
E # матожидание\n\
\n\
Var = 121 * var[0] + 81 * var[1]\n\
Var = Var / k * (n - k) / (n - 1)\n\
std = np.sqrt(Var)\n\
std # cтандарт. отклонение\n\
\n\
E, std'
            ,
            'имеется пронумерованных монет. математическое ожидание дисперсию':'Имеется 11 пронумерованных монет. Монеты подбрасываются до тех пор, пока не выпадет 257 различных (с учетом номера монеты) комбинаций орел-решка.\n\
Пусть Xi – число орлов в комбинации с номером i; а X¯¯¯¯=1257∑Xi – среднее число орлов в полученных таким образом комбинациях.\n\
Требуется найти: 1) математическое ожидание E(X¯¯¯¯); 2) дисперсию Var(X¯¯¯¯).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
k = 257\n\
q = 11\n\
\n\
n = 2 ** q\n\
\n\
lst = np.array(list(product([0, 1], repeat=11)))\n\
lst\n\
\n\
E = lst.mean() * q\n\
E # матожидание\n\
\n\
Var = lst.var() * q\n\
Var = Var / k * (n - k) / (n - 1)\n\
Var # дисперсия'
            ,
            'эмпирическое распределение признаков. математическое ожидание дисперсию':'Эмпирическое распределение признаков X и Y на генеральной совокупности\n\
Ω={1,2,...,100} задано таблицей частот\n\
	Y=1	Y=2	Y=3\n\
X=100	11	32	11\n\
X=400	24	11	11\n\
Из Ω случайным образом без возвращения извлекаются 7 элементов. Пусть X¯¯¯¯ и Y¯¯¯¯ – средние значения признаков на\n\
выбранных элементах. Требуется найти: 1) математическое ожидание E(X¯¯¯¯); 2) дисперсию Var(Y¯¯¯¯); 3) коэффициент корреляции ρ(X¯¯¯¯,Y¯¯¯¯)\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
vals = [(100, 1)] * 11 + [(100, 2)] * 32 + [(100, 3)] * 11 +\n\
[(400, 1)] * 24 + [(400, 2)] * 11 + [(400, 3)] * 11\n\
k = 7\n\
\n\
vals = np.array(vals)\n\
n = len(vals)\n\
\n\
E = vals.mean(axis=0)[0]\n\
E # матожидание\n\
\n\
VarY = vals.var(axis=0)[1]\n\
VarY = VarY / k * (n - k) / (n - 1)\n\
VarY # дисперсия\n\
\n\
cov = ((vals[:, 0] * vals[:, 1]).mean() - vals[:, 0].mean() * vals[:, 1].mean()) / k * (n - k) / (n - 1)\n\
VarX = vals.var(axis=0)[0]\n\
VarX = VarX / k * (n - k) / (n - 1)\n\
\n\
ro = cov / (np.sqrt(VarX) * np.sqrt(VarY))\n\
ro # коэффицент корреляции'
            ,
            'эмпирическое распределение признаков. математическое ожидание стандартное отклонение':'Эмпирическое распределение признаков X и Y на генеральной совокупности\n\
            Ω={1,2,...,100} задано таблицей частот\n\
	Y=1	Y=2	Y=4\n\
X=100	21	17	12\n\
X=300	10	27	13\n\
Из Ω случайным образом без возвращения извлекаются 6 элементов. Пусть X¯¯¯¯ и Y¯¯¯¯ – средние значения признаков на выбранных элементах.\n\
Требуется найти: 1) математическое ожидание E(Y¯¯¯¯); 2) стандартное отклонение σ(X¯¯¯¯); 3) ковариацию Cov(X¯¯¯¯,Y¯¯¯¯).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
vals = [(100, 1)] * 21 + [(100, 2)] * 17 + [(100, 4)] * 12 +\n\
[(300, 1)] * 10 + [(300, 2)] * 27 + [(300, 4)] * 13\n\
k = 6\n\
\n\
vals = np.array(vals)\n\
n = len(vals)\n\
\n\
E = vals.mean(axis=0)[1]\n\
print(E)\n\
\n\
VarX = vals.var(axis=0)[0]\n\
VarX = VarX / k * (n - k) / (n - 1)\n\
print(np.sqrt(VarX))\n\
\n\
cov = ((vals[:, 0] * vals[:, 1]).mean() - vals[:, 0].mean() * vals[:, 1].mean()) / k * (n - k) / (n - 1)\n\
cov'
            ,
            'в группе учится. среднюю положительную оценку в группе медиану положительных оценок в группе':'В группе учится 29 студентов. Ими были получены\n\
следующие 100-балльные оценки: 90, 79, 53, 62, 66, 68, 75, 0, 82, 29, 0, 29, 68, 90, 0, 60, 44, 44, 70, 68, 70, 89, 0, 68, 0, 66, 0, 59, 70.\n\
            Найдите: 1) A – среднюю положительную оценку в группе; 2) M – медиану положительных оценок в группе;\n\
            3) H – среднее гармоническое и G – среднее геометрическое оценок, которые не менее M;\n\
            4) Q – медианную оценку в той части группы, в которой студенты набрали не менее M баллов;\n\
            5) N – количество студентов, оценки которых оказались между H и Q (включая границы).import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
marks = np.array([90, 79, 53, 62, 66, 68, 75, 0, 82, 29, 0, 29, 68, 90, 0, 60, 44, 44, 70, 68, 70, 89, 0, 68, 0, 66, 0, 59, 70])\n\
print(marks[marks>0].mean()) # A\n\
\n\
M = np.median(marks[marks!=0])\n\
print(M) # M\n\
\n\
H = scs.hmean(marks[marks>=M])\n\
print(H) # H\n\
\n\
G = scs.gmean(marks[marks>=M])\n\
print(G) # G\n\
\n\
Q = np.median(marks[marks>=M])\n\
print(Q) #Q\n\
\n\
print(len(marks[(marks >= min(H,Q)) & (marks <= max(H,Q))])) # N'
            ,
            'следующие чисел это. среднее арифметическое ПД эмпирическое стандартное отклонение ПД':'Следующие 28 чисел – это умноженные на 10000 и округленные до ближайшего целого дневные логарифмические доходности\n\
акции компании АВС: -9, 9, -138, -145, 186, 78, 34, -37, -19, -68, -82, 158, 96, -189, 24, 84, -99, 125, -39, 26, 62, -91, 239, -211, 2, 129, 2, -16.\n\
Будем называть их преобразованными доходностями (ПД). Финансовый аналитик Глеб предполагает, что преобразованные доходности (как и исходные)\n\
приближенно распределены по нормальному закону. Чтобы проверить свое предположение Глеб нашел нижнюю квартиль L и верхнюю квартиль H нормального распределения N(μ,σ2),\n\
для которого μ – это среднее арифметическое ПД, а σ – эмпирическое стандартное отклонение ПД. Затем Глеб подсчитал количество ПД, попавших в интервал от L до H\n\
(надеясь, что в этот интервал попадет половина ПД). Результат этого вычисления показался ему недостаточно убедительным. Чтобы окончательно развеять сомнения относительно\n\
нормальности ПД, Глеб построил на одном рисунке графики функций: F^(x) и F(x), где F^(x) – эмпирическая функция распределения ПД, а F(x) – функция распределения N(μ,σ2).\n\
В качестве меры совпадения двух графиков Глеб решил использовать расстояние d между функциями F^(x) и F(x), которое он вычислил, исходя из определения: d=sup|F^(x)−F(x)|.\n\
В ответе укажите результаты вычислений Глеба: 1) среднее арифметическое ПД; 2) эмпирическое стандартное отклонение ПД; 3) квартили L и H; 4) количество ПД,\n\
попавших в интервал от L до H; 5) расстояние между функциями F^(x) и F(x).\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
vals = np.array([-9, 9, -138, -145, 186, 78, 34, -37, -19, -68, -82, 158, 96, -189, 24, 84, -99, 125, -39, 26, 62, -91, 239,\n\
                -211, 2, 129, 2, -16])\n\
\n\
v_mean = vals.mean()\n\
v_std = vals.std()\n\
v_mean, v_std # среднее арифмитическое ПД ; эмипирическое стандартное отклонение ПД\n\
\n\
X = scs.norm(v_mean, v_std)\n\
L = X.ppf(0.25)\n\
H = X.ppf(0.75)\n\
L, H # Квартиль L; квартиль H\n\
\n\
len(vals[(vals >= L) & (vals <= H)]) # колличество ПД, плпавших в интервал от L до H\n\
\n\
xsort=sorted(vals)\n\
n=len(xsort)\n\
\n\
res_d = float("-inf")\n\
for i in range(len(xsort)):\n\
    maxx=max(abs((i+1)/n-X.cdf(xsort[i])),abs((i)/n-X.cdf(xsort[i])))\n\
    if maxx > res_d:\n\
        res_d = maxx\n\
        d_ind = i\n\
res_d, d_ind # res_d - орасстояние между функцифми распределений , d_ind - хз'
            ,
            'в группе учатся. ковариацию коэффициент корреляции':'В группе Ω учатся студенты: ω1,...,ω30. Пусть X и Y – 100-балльные экзаменационные оценки по математическому анализу и теории вероятностей. Оценки студента ωi\n\
обозначаются: xi=X(ωi) и yi=Y(ωi), i=1,...,30. Все оценки известны:\n\
x1=71,y1=71\n\
, x2=52,y2=58\n\
, x3=72,y3=81\n\
, x4=87,y4=92\n\
, x5=81,y5=81\n\
, x6=100,y6=94\n\
, x7=90,y7=96\n\
, x8=54,y8=46\n\
, x9=54,y9=60\n\
, x10=58,y10=62\n\
, x11=56,y11=49\n\
, x12=70,y12=60\n\
, x13=93,y13=86\n\
, x14=46,y14=48\n\
, x15=56,y15=61\n\
, x16=59,y16=52\n\
, x17=42,y17=40\n\
, x18=60,y18=60\n\
, x19=33,y19=37\n\
, x20=83,y20=92\n\
, x21=50,y21=57\n\
, x22=93,y22=93\n\
, x23=41,y23=42\n\
, x24=55,y24=64\n\
, x25=60,y25=59\n\
, x26=37,y26=30\n\
, x27=71,y27=71\n\
, x28=42,y28=44\n\
, x29=85,y29=82\n\
, x30=39,y30=39\n\
. Требуется найти следующие условные эмпирические характеристики: 1) ковариацию X и Y при условии, что одновременно X⩾50 и Y⩾50;\n\
2) коэффициент корреляции X и Y при том же условии.\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
import re\n\
\n\
s = "x1=71,y1=71\n\
 , x2=52,y2=58\n\
, x3=72,y3=81\n\
, x4=87,y4=92\n\
, x5=81,y5=81\n\
, x6=100,y6=94\n\
, x7=90,y7=96\n\
, x8=54,y8=46\n\
, x9=54,y9=60\n\
, x10=58,y10=62\n\
, x11=56,y11=49\n\
, x12=70,y12=60\n\
, x13=93,y13=86\n\
, x14=46,y14=48\n\
, x15=56,y15=61\n\
, x16=59,y16=52\n\
, x17=42,y17=40\n\
, x18=60,y18=60\n\
, x19=33,y19=37\n\
, x20=83,y20=92\n\
, x21=50,y21=57\n\
, x22=93,y22=93\n\
, x23=41,y23=42\n\
, x24=55,y24=64\n\
, x25=60,y25=59\n\
, x26=37,y26=30\n\
, x27=71,y27=71\n\
, x28=42,y28=44\n\
, x29=85,y29=82\n\
, x30=39,y30=39"\n\
match = re.findall(r"=(\d+)", s)\n\
x_all = list(map(int, match[::2]))\n\
y_all = list(map(int, match[1::2]))\n\
\n\
x = []\n\
y = []\n\
\n\
for x_t, y_t in zip(x_all, y_all):\n\
    if x_t >= 50 and y_t >= 50:\n\
        x.append(x_t)\n\
        y.append(y_t)\n\
\n\
x = np.array(x)\n\
y = np.array(y)\n\
\n\
cov = 0\n\
for x_t, y_t in zip(x, y):\n\
    cov += (x_t - x.mean()) * (y_t - y.mean())\n\
cov /= len(x)\n\
cov # ковариация \n\
\n\
cov/np.sqrt(x.var()*y.var()) # коэффицент корреляции'
            ,
            'поток состоит из. среднее значение эмпирическое стандартное отклонение':'Поток Ω состоит из k групп: Ω1,...,Ωk, k=3. На потоке учатся n=n1+...+nk студентов, где ni – число студентов в группе Ωi, i=1,...,k.\n\
Пусть X(ω) – 100-балльная оценка студента ω∈Ω. Далее используются следующие обозначения: x¯¯¯i – среднее значение, σi – (эмпирическое)\n\
стандартное отклонение признака X на группе Ωi. Дано:\n\
n1=24\n\
, n2=26\n\
, n3=30\n\
, x¯¯¯1=70\n\
, x¯¯¯2=76\n\
, x¯¯¯3=77\n\
, σ1=4\n\
, σ2=6\n\
, σ3=8.\n\
Требуется найти: 1) среднее значение Xна потоке Ω; 2) (эмпирическое) стандартное отклонение X на потоке Ω.\n\import numpy as np\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import scipy.stats as scs\n\
import mpmath as mp\n\
from fractions import Fraction\n\
from itertools import permutations, combinations, product\n\
from scipy.stats import *\n\
n1=24\n\
n2=26\n\
n3=30\n\
xm1=70\n\
xm2=76\n\
xm3=77\n\
si1=4\n\
si2=6\n\
si3=8\n\
\n\
M = (n1 * xm1 + n2 * xm2 + n3 * xm3)/(n1 + n2 + n3)\n\
print(M) # срднее значение \n\
\n\
var_all = (n1 * (xm1 - M)**2 + n2 * (xm2 - M)**2 + n3 * (xm3 - M)**2)/(n1 + n2 + n3)\n\
\n\
var_mean_all = (n1 * si1**2 + n2 * si2**2 + n3 * si3**2)/(n1 + n2 + n3)\n\
\n\
np.sqrt(var_all + var_mean_all) # стандартное отклонение'
            }
        print(sklad[task])



