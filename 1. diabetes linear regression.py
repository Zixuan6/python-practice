from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#加载糖尿病数据集
diabetes = datasets.load_diabetes()
X = diabetes.data
Y = diabetes.target

#将数据集拆分为训练集和测试集; test size = 0.2意味着20%是测试集;这样我们就会返回四个数据集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#创建一个多元线性回归算法对象
lr = LinearRegression()

#使用训练集训练模型,这个用来求参数
lr.fit(X_train, Y_train)

#使用测试集进行预测,Y是接收的
Y_pred_train = lr.predict(X_train)
Y_pred = lr.predict(X_test)

#使用评估指标评估：打印模型的均方差
print("测试集均方误差：%.2f" % mean_squared_error(Y_test, Y_pred))
#看看训练集的均方误差
print("训练集均方误差：%.2f" % mean_squared_error(Y_train, Y_pred_train))