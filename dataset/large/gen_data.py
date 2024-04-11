import os

if 1:
    #os.system(f"wget https://drive.google.com/file/d/1_uvttPWADzgGUMTkgmnnreUPDfKWoLCj")

    # this downloads twitter dataset (1.8M edges) from gdrive
    os.system("wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1_uvttPWADzgGUMTkgmnnreUPDfKWoLCj' -O edge.csv")
    os.system("wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1tzbqUe4llYmgjvtQdplv6LPKVfe1ClYS' -O vertex.csv")

    exit(0)
    
# grab some data from facebook https://snap.stanford.edu/data/ego-Facebook.html
dataset_name = "twitter_combined"
os.system(f"wget https://snap.stanford.edu/data/{dataset_name}.txt.gz")
os.system("gunzip *.txt.gz")

file = open(f"{dataset_name}.txt", "r")

os.system("rm -rf {dataset_name}.txt.gz")

vertices = []
edges = []
ctr = 0
for line in file:
    ctr += 1
    print(ctr)
    v = [int(x) for x in line.strip("\n").split(" ")]
    edges.append(v)
    if (v[0] not in vertices):
        vertices.append(v[0])
    if (v[1] not in vertices):
        vertices.append(v[1])

edge_file = open("edge.csv", "w")
#Person.id|Person.id
#38|956
edge_file.write("Person.id|Person.id\n")
for e in edges:
    edge_file.write(str(e[0])+"|"+str(e[1])+"\n")

vertex_file = open("vertex.csv", "w")
#id|firstName|lastName|gender|birthday|creationDate|locationIP|browserUsed
#38|Wilson|Alves|female|1983-02-07|2010-06-17T07:35:23Z|200.0.86.15|Firefox

vertex_file.write("id|firstName|lastName|gender|birthday|creationDate|locationIP|browserUsed\n")

for v in vertices:
    vertex_file.write(str(v) + "|junk|junk|junk|junk|junk|junk|junk\n")