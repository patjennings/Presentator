# Thomas Guesnon 2019
# Ce script permet de transformer un fichier markdown en présentation html, qui change de page au clic

import mistune # parser markdown
import os
print("Presentator lancé !")
print("Ce script va transformer votre fichier markdown .md en présentation html")
md_file="presentation.md"
presentation_title=input("Entrez un titre pour cette présentation : ")
presentation_file="index.html"

path=os.getcwd()

f = open(md_file, "r")
l = f.readlines()
s = []
part = "";
for line in l:
    if line != "\n":
        part += line
parts = part.split("\n---\n")
f.close()

nf = open(presentation_file, "w") # création du fichier html de sortie

# Lecture du fichier de style
style = open("parts/style.css", "r")
output_style=style.read()
style.close()

# Lecture du fichier de script
script = open("parts/script.js", "r")
output_script=script.read()
script.close()

html_output = "<html>"

html_output+="<head>\n<title>"+presentation_title+"</title>\n<meta charset=\"utf-8\" />\n<style type=\"text/css\" media=\"screen\">"
html_output+=output_style
html_output+="</style>\n</head>"

html_output+="<body>"

section_number=1
for section in parts:
    so="<section id=\"p-"+str(section_number)+"\" class=\"color-primary\">"
    so+="<div>"
    so+=mistune.markdown(section)
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

nf.write(html_output);
nf.close()
