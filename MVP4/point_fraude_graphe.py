import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from MVP4.points import *


import csv
# 文件头，一般就是数据名
fileHeader = [u"critère", u"valeur", u"total"]
# 假设我们要写入的是以下两行数据

line1 = ["similarité avec d'autres", point_simil_code,100]
line2 = ["similarité des noms de fonctions", point_simil_func, 100]
line3 = ["similarité des noms de variables", point_simil_vari, 100]
line4 = ["similarité des noms de tests", point_simil_test, 100]

point_final = point_simil_code + point_simil_func + point_simil_vari + point_simil_test
line5 = ["final", point_final/4, 100]




# 写入数据
csvFile = open("point_fraude.csv", "w")
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
writer.writerow(line1)
writer.writerow(line2)
writer.writerow(line3)
writer.writerow(line4)
writer.writerow(line5)




csvFile.close()



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Load the example car crash dataset
#crashes = sns.load_dataset("point1").sort_values("total", ascending=False)
# Load the data
crashes = pd.read_csv("/Users/apple/PycharmProjects/Doctolib/MVP4/point_fraude.csv")

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="critère", data=crashes, label="fraude", color="r")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="valeur", y="critère", data=crashes, label="authentique", color="g")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 100), ylabel="", xlabel="note du candidat")
sns.despine(left=True, bottom=True)

plt.show()