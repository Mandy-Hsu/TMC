# this is testing google results
try:
    from googlesearch import search
    #print("Success!")
except ImportError:
    print("Module Google not found")

#The function is the following:
#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)

keywords = ["grant application", "giving back", "community service"]
rootFile = "/Users/mandyhsu/Desktop/"

compList = open(rootFile+"companyList.txt","r")

resultURL = open(rootFile+"urlList.txt","w")
entry = compList.readline()

#print("reached the end of instantiating new files\n\n")


while entry:

    print("\n\n\nread from companyList\n\n\n")

    param = entry.split()

    location = False
    if  len(param) > 1:
        location = True 

    query = param[0]
    resultURL.write("\n\nResults for "+query)
    for key in keywords:
        query += " "+key

        print("\n\nThis is the query: "+query+"\n\n")

        for j in search(query, tld="co.in", num=3, stop=1, pause=2):
            resultURL.write("\n"+j)

        query = param[0]

    entry = compList.readline()

compList.close()
resultURL.close()

