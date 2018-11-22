from MVP1.open_ruby import openRb
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from MVP1.num_comments import nombre_commentaire
from MVP1.num_functions import nombre_fonction
from MVP1.num_tests import nombre_test
from MVP1.num_variables import nombre_variable
from MVP1.num_scopes import nombre_requetes_SQL

num_comments = nombre_commentaire(candidate_rb)
num_functions = nombre_fonction(candidate_rb)
num_variables = nombre_variable(candidate_rb)
num_tests = nombre_test(candidate_rb_test)
num_scopes = nombre_requetes_SQL(candidate_rb)

import csv
# 文件头，一般就是数据名
fileHeader = [u"critère", u"valeur"]
# 假设我们要写入的是以下两行数据
line1 = ["function", num_functions]
line2 = ["commentaire", num_comments]
line3 = ["variable", num_variables]
line4 = ["test", num_tests]
line5 = ["scope", num_scopes]

# 写入数据
csvFile = open("parametre_code.csv", "w")
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
writer.writerow(line1)
writer.writerow(line2)
writer.writerow(line3)
writer.writerow(line4)
writer.writerow(line5)

csvFile.close()




sns.set(style="whitegrid")

# Load the example Titanic dataset
#datatweet = sns.load_dataset("instance")

# Load the data
datatweet = pd.read_csv("/Users/apple/PycharmProjects/Doctolib/MVP4/parametre_code.csv")

# Draw a nested barplot to show degree for opinion and candidates
g = sns.catplot(x="critère", y="valeur", data=datatweet,height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("nombre")

plt.show()





from MVP2.contenu_fonc import Contenu_fonction
print(Contenu_fonction(candidate_rb))

from MVP2.contenu_test import Contenu_test
print(Contenu_test(candidate_rb_test))

