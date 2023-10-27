class test:
    def task(zadacha=''):
        #1
        sklad = {
            '1':'1. (1 балл) Загрузите предложенный вам датасет с помощью функции sklearn.datasets.fetch_openml. \n\
Выведите текстовое описание загруженного датасета. бозначьте целевую переменную за y, \n\
а остальные данные за X.\n\
import numpy as np\n\
import matplotlib.pyplot as plt\n\
import pandas as pd\n\
from sklearn.linear_model import LinearRegression\n\
from sklearn.metrics import r2_score, mean_squared_error\n\
from sklearn.preprocessing import PolynomialFeatures\n\
from sklearn.datasets import fetch_Название_Библиотеки\n\
california = fetch_california_housing()\n\
california\n\
\n\
print(california["DESCR"])\n\
\n\
X = california.data\n\
X\n\
\n\
Y = california.target\n\
Y\n\
\n\
data = pd.DataFrame(california.data, columns = california.feature_names)\n\
data["Price"] = california.target\n\
data'
            ,
            '2':'2. (1 балл) Выведите основную статистическую информацию о данных. Сделайте количественное\n\
описание датасета: число строк (объектов),число столбцов (признаков), статистику по признакам.\n\
type(california)\n\
\n\
data.describe()\n\
\n\
X.shape, Y.shape'
            ,
            '3':'3. (1 балл) Выведите тип данных каждого признака и целевой переменной. Убедитесь,\n\
что в данных все признаки являются числовыми. В случае, если это не так, удалите нечисловые колонки.\n\
data.info()\n\
Все колонки float - числовые, ничего удалять и менять не надо.\n\
А так через data.drop(название столбца) удаляем ненужные столбцы'
            ,
            '4':'4. (1 балл) Убедитесь, что нет пропущенных значений в данных и у целевой переменной. В случае,\n\
если это не так, заполните пропуски медианными значениями\n\
data.isnull().sum()\n\
\n\
data["Price"].isnull().sum() # необязательно\n\
\n\
Убедились, что нет пустых\n\
Если что, то:\n\
data = data.fillna(data.median())\n\
data["Price"] = data["Price"].fillna(data["Price"].median())'
            ,
            '5':'5. (1 балл) Постройте гистограмму распределения целевой переменной. Сделайте вывод по графику.\n\
Предположите, какому виду распределения она принадлежит.\n\
plt.figure(figsize=(8, 6))\n\
plt.hist(data["Price"], bins=20, color="blue", alpha=0.7)\n\
plt.xlabel("Значения целевой переменной")\n\
plt.ylabel("Частота")\n\
plt.title("Гистограмма распределения целевой переменной")\n\
plt.show()\n\
\n\
На основе графика вы можете предположить вид распределения. Например:\n\
Если гистограмма напоминает колокол (является симметричной и унимодальной), то это может быть нормальное распределение.\n\
Если гистограмма смещена влево и имеет длинный хвост вправо, это может быть распределение, близкое к логнормальному.\n\
Если гистограмма имеет два явных "пика", это может быть двойное распределение.\n\
Если гистограмма неравномерна и имеет длинные хвосты, это может быть распределение, близкое к распределению Пуассона.\n\
Если гистограмма является равномерной, то это равномерное распределение.'
            ,
            '6':'6. (4 балл) Обучите модель линейной регрессии на рассматриваемых данных, написанную своими руками.\n\
Проиллюстрируйте работу модели графиком обучения и распределения целевой переменной. Выведите уравнение полученной гиперплоскости.\n\
class LinReg:\n\
    def init(self):\n\
        self.b1 = []\n\
        self.b0 = 0\n\
\n\
    def fit(self, x, y):\n\
        x = np.column_stack((np.ones(len(x)), x))\n\
        vals = np.linalg.inv(x.T @ x) @ (x.T @ y) # наклон прямой\n\
        self.b0 = vals[0] # свободный член\n\
        self.b1 = vals[1:]\n\
        giperploskost = str(self.b0)\n\
        for i, j in enumerate(self.b1):\n\
            giperploskost += " + " + str(j) + f" * X{i}"\n\
        return giperploskost\n\
\n\
\n\
    def predict(self, x):\n\
        ypred = []\n\
        for i in range(X.shape[0]):\n\
            tt = self.b0\n\
            for j in range(X.shape[1]):\n\
                tt += self.b1[j]*x[i][j]\n\
            ypred.append(tt)\n\
        return np.array(ypred)\n\
\n\
a=LinReg()\n\
a.fit(X,Y)\n\
ypred = a.predict(X)\n\
print("Ручное ур-е гиперплоскости:")\n\
a.fit(X,Y)\n\
\n\
plt.scatter(Y,ypred)\n\
plt.plot(Y,Y, c="r")'
        
            ,
            '7':'7. (2 балл) Обучите модель LinearRegression() линейной регрессии на рассматриваемых данных из библиотеки sklearn.\n\
Выведете уравнение полученной гиперплоскости. Убедитесь, что уравнения гиперплоскостей, полученных с помощью модели написанной своими\n\
руками и библиотечной, будут примерно одинаковыми.\n\
model = LinearRegression()\n\
model.fit(X, Y)\n\
print(model.coef_, model.intercept_)\n\
\n\
model.intercept_\n\
\n\
giperploskost = str(model.intercept_)\n\
for i, j in enumerate(model.coef_):\n\
    giperploskost += " + " + str(j) + f" * X{i}"\n\
print("Библиотечное ур-е гиперплоскости:")\n\
giperploskost\n\
\n\
a=LinReg()\n\
a.fit(X,Y)\n\
ypred = a.predict(X)\n\
print("Ручное ур-е гиперплоскости:")\n\
a.fit(X,Y)\n\
\n\
y_pred = model.predict(X)\n\
plt.scatter(Y, y_pred, c = "black")\n\
plt.plot(Y, Y, c="r")\n\
plt.xlabel("y - истинный")\n\
plt.ylabel("y - предсказанный")\n\
plt.show()'
            ,
            '8':'8. (1 балл) Оцените работу моделей, рассчитав для каждой из них метрики: коэффициент детерминации и ошибку MSE.\n\
Сделайте выводы по качеству работы моделей.\n\
a=LinReg()\n\
a.fit(X,Y)\n\
y_pred_hand = a.predict(X)\n\
r2_hand = r2_score(Y, y_pred_hand)\n\
mse_hand = mean_squared_error(Y, y_pred_hand)\n\
print(f"Метрики для модели, построенной руками:")\n\
print(f"Коэффициент детерминации (R-squared): {r2_hand}")\n\
print(f"Среднеквадратичная ошибка (MSE): {mse_hand}")\n\
\n\
y_pred_sklearn = model.predict(X)\n\
r2_sklearn = r2_score(Y, y_pred_sklearn)\n\
mse_sklearn = mean_squared_error(Y, y_pred_sklearn)\n\
print(f"Метрики для модели из sklearn:")\n\
print(f"Коэффициент детерминации (R-squared): {r2_sklearn}")\n\
print(f"Среднеквадратичная ошибка (MSE): {mse_sklearn}")'
            }
        print(sklad[zadacha])



