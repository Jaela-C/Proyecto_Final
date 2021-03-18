import couchdb
from textblob import TextBlob
#import re
#import emoji
import time
couch=couchdb.Server('http://admin:admin@127.0.0.1:5984')

#db=couch['combined-lasso-arauz']
nombredb='noticias'
db=couch[nombredb]

count=0
cambios=0
for docid in db.view('_all_docs', skip=1):
#for docid in db.view('_all_docs', descending=True):
    id=docid['id']
    idnumber=int(id)
    count=count+1
    print(str(count)+"-> "+str(id) )
    #if idnumber< 1346120101632864261:
    #	continue
    doc=db[id]
    texto=doc['text']
    time.sleep(0.01)
    if not'clasificado' in doc:
    #if not'clasificado' and count>385000 in doc:
    #if not'clasificado' and id>1326633672523608065 in doc:
        cambios=cambios+1
        try:
            time.sleep(0.3)
            texto_en=TextBlob(str(texto)).translate(to="en")
            doc['traduccion'] = "si"
        except:
            texto_en=TextBlob(str(texto))
            doc['traduccion'] = "no"
        
        polaridad=texto_en.polarity
        subjetividad=texto_en.subjectivity
        if polaridad<0:
            sentimiento="negativo"
        elif polaridad==0:
            sentimiento="neutral"
        else:
            sentimiento="positivo"
        print(nombredb)
        print("polaridad: "+str(polaridad))
        print("subjetividad: "+str(subjetividad))
        print("sentimiento: " +str(sentimiento))

        try:
            
            doc['polaridad'] = polaridad
            doc['subjetividad'] = subjetividad
            doc['sentimiento'] = sentimiento
            doc['nombredb'] = nombredb
            doc['clasificado'] = "si"
            #print(nombredb + str(polaridad)+str(subjetividad)+str(sentimiento))
            db.save(doc)
            print("texto clasificado")
            print(" ")
        except:
            print("no se pudo clasificar ")
            doc['clasificado'] = "no"
            doc['nombredb'] = nombredb
            db.save(doc)

        
    else:
        print ("listo")
        print()

print("cambios totales realizados: "+str(cambios))
    #emot=re.findall(r'[^\w\s,]', texto)
    #list_emoji = [emoji.emojize(x) for x in texto]

    
    #print(emot)
    #print(list_emoji)