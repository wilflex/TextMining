
def load_data():
    
    try:
        
        links = "".join(c.replace('\\',"\\") for c in r"C:\Users\marsh\Desktop\Text mining\les_miserables_1.txt")
        href = "".join(c.replace('\\',"/")for c in links)

        i = 0
        with open(href,"r",encoding="utf-8") as f:
            text = f.readlines()
    
            #for c in text:
                #i += 1
                #print(i,c.strip("\n"))
        
        lines = []

        for word in text[20:13907]:
            lines.append(word.strip(""))
        lines = [line.title() for line in lines]
        result = ''.join(lines)
    
        return result
    
    except Exception as e:
        print(e.args)



def recherche_prenom():
        
    # chargement des données
    texto = load_data().split("\n")
    
    # construction de la souche cible
    cible = []
    i = 0
    for c in texto:
        if "Monsieur" in c or "M." in c or "Madame" in c or "Mademoiselle" in c or "Mme" in c:
            c = c.replace("M. ","*")
            c = c.replace("Monsieur ","*")
            c = c.replace("Madame ","*")
            cible.append(c)
            
    # identification des nom ou prenom
    nom = set() 
    for c in cible:
        c = c.replace("--"," ")
        for j in c.lower().split():
            if "*" in j:
                nom.add(j.strip(".").strip("?").strip("!").strip(";").strip("_").strip("«"))
                
    # nettoyage de nom et pretraitement       
    name = list(nom)
    nom = set() 
    for c in cible:
        c = c.replace("--"," ")
        for j in c.lower().split():
            if "*" in j:
                nom.add(j.strip("?").strip("!").strip(";").strip("_").strip("«").strip(",").strip("»").strip("."))
    name = list(nom)

    mot_vide = [c for c in list(nom) if len(c) <= 4]

    clean_name = []
    for j in mot_vide:
        if j in name:
            name.remove(j)

    for c in name:           
        if "'" in c or "veut" in c or "soupe" in c or "couche" in c:
            pass
        else:
            clean_name.append(c.strip("*"))    
    clean_name.remove('votre')
    clean_name.remove('aurait')
    clean_name.remove("attendra")

    clean_name = {c.capitalize() for c in clean_name}
    
    return clean_name


if __name__ == '__main__':
    assert type(load_data()) == type("e")
    assert  type(recherche_prenom()) == type({1})
    print(recherche_prenom())