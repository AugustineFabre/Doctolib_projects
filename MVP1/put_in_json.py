import json

from nombre_fonction import nombre_fonction
functionCount = nombre_fonction(candidate_rb)

from nombre_commentaire import *
commentCount = nombre_commentaire(candidate_rb)

from nombre_test import *
testCount = nombre_test(candidate_rb_test)

from nombre_variable import *
variableCount = nombre_variable(candidate_rb)

MVP1 = {"functionCount": functionCount, "commentCount": commentCount, "variableCount": variableCount, "testCount": testCount}
print(MVP1)

with open('../fichier_json/MVP1.json', 'w', encoding='utf-8') as f:
    json.dump(MVP1, f, indent=4)
