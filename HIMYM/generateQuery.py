import pandas as pd

df = pd.read_csv("himym.csv")

df


df.iloc[0]['Name']


query = "g.addV('person')"
for idx in range(len(df)):
    for elem in list(df.columns):
        val = df.iloc[idx][elem]
        if type(val)==str and ";" in val:
            splitted = df.iloc[idx][elem].split(";")
            for spt in splitted:
                query+=".property('"+elem+"','"+spt+"')"
        elif type (val)==str:
            query+=".property('"+elem + "','" + str(val) + "')"
        else:
            query+=".property('"+elem + "'," + str(val) + ")"

    print(query)
    query = "g.addV('person')"

g.addV('person').property('Name','Penny').property('age',4).property('Location','New York').property('Occupation','Student').property('id','penny')
g.addV('person').property('Name','Luke').property('age',2).property('Location','New York').property('Occupation','Student').property('id','luke')
g.addV('person').property('Name','Marvin').property('age',7).property('Location','New York').property('Location','Rome').property('Occupation','Student').property('id','marvin')
g.addV('person').property('Name','Daisy').property('age',5).property('Location','New York').property('Location','Rome').property('Occupation','Student').property('id','daisy')


relations = pd.read_csv("himym_relations.csv")

relations

#g.addE('knows').from(marko).to(peter)
addE = "g.addE('"+rel+"').from("++").to("+")"
addE = "g.addE('"
relations.iloc[0]

for idx in range(len(relations)):
    addE+=relations.iloc[idx]['relation']+"').from("+relations.iloc[idx]['man']+").to("+relations.iloc[idx]['woman']+")"
    print(addE)
    addE = "g.addE('"

g.V().hasLabel('person').has('id', 'ted').addE('married').to(g.V().hasLabel('person').has('id', 'tracy'))
g.V().hasLabel('person').has('id', 'ted').addE('loved').to(g.V().hasLabel('person').has('id', 'robin'))
g.V().hasLabel('person').has('id', 'ted').addE('loved').to(g.V().hasLabel('person').has('id', 'victoria'))
g.V().hasLabel('person').has('id', 'barney').addE('married').to(g.V().hasLabel('person').has('id', 'robin'))
g.V().hasLabel('person').has('id', 'marshall').addE('married').to(g.V().hasLabel('person').has('id', 'lily'))
g.V().hasLabel('person').has('id', 'ted').addE('roomate').to(g.V().hasLabel('person').has('id', 'marshall'))
g.V().hasLabel('person').has('id', 'ted').addE('roomate').to(g.V().hasLabel('person').has('id', 'lily'))
g.V().hasLabel('person').has('id', 'ted').addE('parent').to(g.V().hasLabel('person').has('id', 'luke'))
g.V().hasLabel('person').has('id', 'ted').addE('parent').to(g.V().hasLabel('person').has('id', 'penny'))
g.V().hasLabel('person').has('id', 'tracy').addE('parent').to(g.V().hasLabel('person').has('id', 'luke'))
g.V().hasLabel('person').has('id', 'tracy').addE('parent').to(g.V().hasLabel('person').has('id', 'penny'))
g.V().hasLabel('person').has('id', 'marshall').addE('parent').to(g.V().hasLabel('person').has('id', 'marvin'))
g.V().hasLabel('person').has('id', 'marshall').addE('parent').to(g.V().hasLabel('person').has('id', 'daisy'))
g.V().hasLabel('person').has('id', 'lily').addE('parent').to(g.V().hasLabel('person').has('id', 'marvin'))
g.V().hasLabel('person').has('id', 'lily').addE('parent').to(g.V().hasLabel('person').has('id', 'daisy'))


#Chi è stato in Connecticut
g.V().hasLabel('person').has('Location', 'Connecticut')
#Chi ha piu di 35 anni
g.V().hasLabel('person').has('age', gt(35))
# I figli dei conquilini di ted
g.V().hasLabel('person').has('id', 'ted').outE('roomate').inV().outE('parent').inV()


ted = g.V().has('Name','Ted Mosby').next()
barney = g.V().has('Name','Barney Stinson').next()
robin = g.V().has('Name','Robin Scherbatsky').next()
lily = g.V().has('Name','Lily Aldrin').next()
marshall = g.V().has('Name','Marshall Eriksen').next()
victoria = g.V().has('Name','Victoria').next()
tracy = g.V().has('Name','Tracy McConnell').next()




#
