# Thomas Guesnon 2019
# Ce script permet de transformer un fichier markdown en présentation html, qui change de page au clic

import mistune # parser markdown
import os

print("Presentator lancé !")
print("Ce script va transformer votre fichier markdown .md en présentation html")

path=os.getcwd()
md_file="presentation.md"

presentation_title=input("Entrez un titre pour cette présentation : ")
presentation_file="index.html"

def set_attr(attr_str, attr_type):
    get_attr=attr_str.split(":")
    get_attr=get_attr[1]
    get_attr=get_attr.replace(" ", "")
    get_attr=get_attr.replace("\n", "")
    result = {attr_type:get_attr}
    return result

slide_colors=[]
slide_bg=[]

f = open(md_file, "r")
lines = f.readlines()
parts = [];
part = {"content": "", "color": "#FFFFFF", "background": "#333333"}

# Ici, je lis les sections séparées par ---
# Si je trouve une ligne "color:", je la traite avec set_attr() pour qu'elle me renvoie un objet
# avec lequel je remplacerai la key/value par défaut {"color" : "#FFFFFF"}
# Pareil avec une ligne "background:"

# Si une ligne du fichier n'est :
# - ni une couleur
# - ni un background
# - ni un saut de ligne
# - ni un séparateur
# j'append la clé content de part{} avec cette ligne

# Quand je trouve "---", indicateur d'une nouvelle section, je pousse le dict part{} dans la list parts[]. Je réinitialise le dict part{} avec les valeurs par défaut, et je recommence

for line in lines:
    print(line)
    check_color=line.find("color")
    check_bg=line.find("background")

    if line != "\n" and line.find("---")==-1 and check_color==-1 and check_bg==-1: # j'ai une ligne de contenu
        part.update(content = part["content"]+"\n"+line)
    if check_color>=0: # J'ai une couleur
        c=set_attr(line, "color")
        part.update(c)
    if check_bg>=0: # J'ai un background
        b=set_attr(line, "background")
        part.update(b)
    if line.find("---") != -1: # J'ai une nouvelle section
        parts.append(part)
        part = {"content": "", "color": "#FFFFFF", "background": "#333333"}        

f.close()

nf = open(presentation_file, "w") # création du fichier html de sortie

# Lecture du fichier de style
style = open("includes/style.css", "r")
output_style=style.read()
style.close()

# Lecture du fichier de script
script = open("includes/script.js", "r")
output_script=script.read()
script.close()

html_output = "<html>"

html_output+="<head>\n<title>"+presentation_title+"</title>\n<meta charset=\"utf-8\" />\n<style type=\"text/css\" media=\"screen\">"
html_output+=output_style
html_output+="</style>\n</head>"

html_output+="<body>"

section_number=1
for section in parts:
    so="<section id=\"p-"+str(section_number)+"\" style=\"background-color:"+section["background"]+"; color: "+section["color"]+";\">"
    so+="<div>"
    so+=mistune.markdown(section["content"])
    so+="</div>"
    so+="</section>"
    section_number+=1
    html_output+=so

html_output+="<script type=\"text/javascript\">"
html_output+=output_script
html_output+="</script>"
html_output+="</body>"
html_output+="</html>"

print("Fichier HTML créé ! ")
print("> "+path+"/"+presentation_file)

# print(html_output)

nf.write(html_output);
nf.close()
