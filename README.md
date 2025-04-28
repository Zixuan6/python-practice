# python-machine-learning-practice
## Table of Contents
- [糖尿病回归预测](##糖尿病回归预测)
## 糖尿病回归预测
## 1. 因为我们需要用到scikit-learn

a. 打开terminal

b. 进入你想放环境的文件夹，比如 Documents：
```bash
cd ~/Documents
```
c. 创建一个新的虚拟环境，比如叫sklearn-ev：
```bash
python3 -m venv sklearn-env
```
d. 激活虚拟环境
```bash
source sklearn-env/bin/activate
```
e. 激活后，Terminal 前面应该出现 (sklearn-env)，就表示你在这个环境里了。

f. 然后在环境里安装 scikit-learn：
```bash
pip install scikit-learn
```
## 2. 做回归预测的步骤

a. 导入数据集，命名数据集X为training data， Y为target data

b. 将数据集拆分为训练集和测试集，用**train_test_split**

c. 创建一个多元线性回归算法对象 **lr = LinearRegression()**

d. 用训练集训练模型求参数， **lr.fit(X_train, Y_train)**

e. 预测一下X_test的Y值，可以X_train, X_test都算一下

f. 打印mean squared error的值，也就是loss function









