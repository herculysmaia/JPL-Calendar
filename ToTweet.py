arquivo = open("novo documento de texto.txt", "r")
string_list = []
e_link = True
text = ""
post = []

for linha in arquivo.readlines():
    if linha[0:4] == "<li>" and len(string_list) != 0:
        if len(text) > 250:
            raw_input("OOOPS!!")
        print text
        string_list.append(text)
        if string_list[1] == None:
            post.append("%s %s %s" % (string_list[0][-2:],string_list[3],string_list[2]))
        else:
            post.append("%s %s-%s %s %s" % (string_list[0][-2:],string_list[0],string_list[1],
                                            string_list[3],string_list[2]))
        string_list = []
        
    if e_link and linha[0:4] == "<a h":
        text += " "
    e_link = True
    if linha[0:4] == "<li>":
        string_list.append(linha[5:11])
        if linha[11] == "-":
            i=12
            text = ""
            while linha[i] != "-":
                text += linha[i]
                i+=1
            string_list.append(text[0:-1])
            i+=2
        else:
            i=14
            string_list.append(None)
        if linha[i-1:i+3] == "<img":
            while linha[i] != "]":
                i+=1
            i+=2
        if linha[i:i+2] == "<a":
            while linha[i] != "=":
                i+=1
            text = ""
            i+=1
            while linha[i] != ">":
                text += linha[i]
                i+=1
            i+=1
            string_list.append(text)
            text = ""
            while linha[i:i+4] != "</a>":
                text += linha[i]
                i+=1
            i+=4
    
        else:
            text_link = ""
            text = ""
            while linha[i] != "<":
                text += linha[i]
                i+=1
            i+=8
            while linha[i] != ">":
                text_link += linha[i]
                i+=1
            i+=1
            while linha[i:i+4] != "</a>":
                text += linha[i]
                i+=1
            i+=4
            if linha[i:i+2] != "\n":
                while linha[i:i+2] != "\n":
                    text += linha[i]
                    i+=1
        
            
            string_list.append(text_link)
        
        if linha[i:i+2] != "\n":
            while linha[i:i+2] != "\n":
                text += linha[i]
                i+=1
            
    i=0
    if linha[0:4] == "<a h":
        i+=1
        while linha[i] != ">":
            i+=1
        i+=1
        while linha[i:i+4] != "</a>":
            text += linha[i]
            i+=1
        i+=4
        e_link = False
        if linha[i:i+2] != "\n":
            while linha[i:i+2] != "\n":
                text += linha[i]
                i+=1
arquivo2 = open("json/json.json", "w" )
for line in post:
    arquivo2.write(line)
    arquivo2.write('\n')
arquivo2.close()
arquivo.close()
