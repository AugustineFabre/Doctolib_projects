def nombre_requetes_SQL(code):
    index=0
    for ligne in code.split('\n'):
        if "scope " in ligne:
            index +=1
    return index
