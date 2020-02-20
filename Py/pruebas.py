import pandas as pd
import numpy as np
import plotly.express as px
x = np.linspace(-5,5,100)
y = []
for i in range(len(x)):
    y.append(1/(1+np.e**(-x[i])))

px.scatter(x,y)
px.show()