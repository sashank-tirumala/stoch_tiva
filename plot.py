import matplotlib.pyplot as plt 
import pandas as pd
plt.figure()
df = pd.read_csv('data.txt')
plt.plot(df['leg1_x'], df['leg1_y'])
plt.plot(df['leg2_x'], df['leg2_y'], 'r')
plt.legend()
plt.show()