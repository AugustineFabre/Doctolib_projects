import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from MVP4.points import *


import csv
# 文件头，一般就是数据名
fileHeader = [u"critère", u"valeur"]
# 假设我们要写入的是以下两行数据
line1 = ["variables bien nommées", point_nom_var]
line2 = ["fonctions bien nommées", point_nom_fonc]
line3 = ["bons cases in code", point_bon_case]
line4 = ["bons cases in test", point_bon_case_test]
line5 = ["noms diff des variables", point_dif_vari]
line6 = ["noms diff des fonctions", point_dif_func]
line7 = ["noms diff des tests", point_dif_test]
line8 = ["duplication de code", point_dupli_code]
line9 = ["duplication de test", point_dupli_test]
line10 = ["longeur de fonction", point_trop_long]

'''
line11 = ["similarité avec d'autres", point_simil_code]
line12 = ["similarité des noms de fonctions", point_simil_func]
line13 = ["similarité des noms de variables", point_simil_vari]
line14 = ["similarité des noms de tests", point_simil_test]
'''

line11 = ["similarité avec d'autres",100]
line12 = ["similarité des noms de fonctions",100]
line13 = ["similarité des noms de variables",100]
line14 = ["similarité des noms de tests", 100]
line15 = ["commentaires pour les longues fonctions", point_avoir_comment]


#point_final = point_nom_var + point_nom_fonc + point_bon_case + point_bon_case_test + point_dif_vari + point_dif_func + point_dif_test + point_trop_long + point_simil_code + point_simil_func + point_simil_vari + point_simil_test + point_avoir_comment
point_final = point_nom_var + point_nom_fonc + point_bon_case + point_bon_case_test + point_dif_vari + point_dif_func + point_dif_test + point_trop_long + 100 + 100 + 100 + 100 + point_avoir_comment
line16 = ["final", point_final/15]




# 写入数据
csvFile = open("point.csv", "w")
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
writer.writerow(line1)
writer.writerow(line2)
writer.writerow(line3)
writer.writerow(line4)
writer.writerow(line5)
writer.writerow(line6)
writer.writerow(line7)
writer.writerow(line8)
writer.writerow(line9)
writer.writerow(line10)
writer.writerow(line11)
writer.writerow(line12)
writer.writerow(line13)
writer.writerow(line14)
writer.writerow(line15)
writer.writerow(line16)



csvFile.close()




sns.set(style="whitegrid")

# Load the example Titanic dataset
#datatweet = sns.load_dataset("instance")

# Load the data
datatweet = pd.read_csv("/Users/apple/PycharmProjects/Doctolib/MVP4/point.csv")

# Draw a nested barplot to show degree for opinion and candidates
g = sns.catplot(x="critère", y="valeur", data=datatweet,height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("nombre")

plt.show()