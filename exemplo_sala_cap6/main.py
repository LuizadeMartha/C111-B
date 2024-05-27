import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #PLOT SIMPLES
# x = np.array([1,2,3,4])
#
# #Broadcasting
# y = x*2
# #PLOTS MULTIPLOS
# y2 = x**2
#
# plt.xlabel('Valores de X')
# plt.ylabel('Valores de Y')
# #PLOTAGEM
# plt.plot(x, y, 'o--g', x, y2, 'b:o',
#          linewidth=3, markersize=20)
# plt.show()
#
#
# #subplots
# x = np.array([1,2,3,4])
# #Broadcasting
# y = x*2
# y2 = x**2
#
# #plot 1
# plt.subplot(1, 2, 1)
# plt.title('Linear')
# plt.plot(x, y, 'x--r')
#
# #plot 2
# plt.subplot(1, 2, 2)
# plt.title('Exponencial')
# plt.plot(x, y2, 'o:g')
# plt.show()

#SCATTER PLOT
dataset =pd.read_csv('Paises.csv', delimiter=';')
dataset2 = dataset.nlargest(6, 'Area (sq. mi.)')
plt.scatter(x=dataset2['Country'],
            y=dataset2['Area (sq. mi.)'],
            s=dataset2['GDP ($ per capita)']/50)
plt.show()
#maior renda per capita EUA
#maior area : russia