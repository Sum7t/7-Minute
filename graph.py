import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("Book1.xlsx")
print(df.head(10))

Stocks = ((np.asarray(df['Stocks'])).reshape(5,2))
SD = ((np.asarray(df['SD'])).reshape(5,2))

print(Stocks)
print(SD)

result = df.pivot(index='Yrows',columns='Xcols',values='SD')
print(result)

labels = (np.asarray(["{0} \n {1:.2f}".format(symb,value)
                      for symb, value in zip(Stocks.flatten(),
                                               SD.flatten())])
         ).reshape(5,2)

fig, ax = plt.subplots(figsize=(13,7))

# Add title to the Heat map
title = "Standard Deviation"

# Set the font size and the distance of the title from the plot
plt.title(title,fontsize=18)
ttl = ax.title
ttl.set_position([0.5,1.05])

# Hide ticks for X & Y axis
ax.set_xticks([])
ax.set_yticks([])

# Remove the axes
ax.axis('off')

sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidths=0.30,ax=ax)

plt.show()