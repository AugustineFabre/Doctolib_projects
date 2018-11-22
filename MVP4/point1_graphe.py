from MVP4.points import *


import csv
# 文件头，一般就是数据名
fileHeader = [u"critère", u"valeur",u"total"]
# 假设我们要写入的是以下两行数据
line1 = ["variables bien nommées", point_nom_var,100]
line2 = ["fonctions bien nommées", point_nom_fonc,100]
line3 = ["bons cases in code", point_bon_case,100]
line4 = ["bons cases in test", point_bon_case_test,100]
line5 = ["noms diff des variables", point_dif_vari,100]
line6 = ["noms diff des fonctions", point_dif_func,100]
line7 = ["noms diff des tests", point_dif_test,100]
line8 = ["duplication de code", point_dupli_code,100]
line9 = ["duplication de test", point_dupli_test,100]
line10 = ["longeur de fonction", point_trop_long,100]

#point_final = point_nom_var + point_nom_fonc + point_bon_case + point_bon_case_test + point_dif_vari + point_dif_func + point_dif_test + point_trop_long + point_simil_code + point_simil_func + point_simil_vari + point_simil_test + point_avoir_comment
point_final = point_nom_var + point_nom_fonc + point_bon_case + point_bon_case_test + point_dif_vari + point_dif_func + point_dif_test + point_trop_long + 100 + 100 + 100 + 100 + point_avoir_comment
line11 = ["final", point_final/15,100]




# 写入数据
csvFile = open("point1.csv", "w")
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




csvFile.close()