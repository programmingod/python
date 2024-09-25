import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Salaries.csv")
m = 0
b = 0
L = 0.0001
iter = 100

def gradient(m_new, b_new, points, L):
    m_grad = 0
    b_grad = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].remote_ratio
        y = points.iloc[i].salary_in_usd
        m_grad += -(2/n)*x*(y-(m_new*x+b_new))
        b_grad += -(2/n)*(y-(m_new*x+b_new))
    m = m_new - m_grad*L
    b = b_new - b_grad*L

    return m, b


for w in range(iter):
    m,b = gradient(m,b,data,L)


print(m,b)

plt.scatter(data.remote_ratio, data.salary_in_usd, color="black")
plt.plot(list(range(0,100)), [m*x+b for x in range(0,100)], color="red")
plt.show()