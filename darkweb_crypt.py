import webhoseio
from collections import Counter
webhoseio.config(token="7f568fb7-7400-47c9-9213-7b074c590dc0")
query_params = {
"q": "EternalBlue OR WannaCrypt OR ShadowBroker OR EquationAPT OR Lazarus OR LazarusGroup OR Lazarus-Group OR Erebus OR Ransomware OR GoldenEye OR CryptoLocker OR Locky OR Petya OR zCrypt OR PowerWare OR HydraCrypt OR Cerber OR CryptoWall OR CVE",
"ts": "1479589849479"}
output = webhoseio.query("productFilter", query_params)
print(output)
print(output["darkposts"][0]["text"]) # Print the text of the first post
print(output["darkposts"][0]["title"]) # Print the title of the first post

fname="site_darkweb.txt"    
# Get the next batch of posts

output = webhoseio.get_next()

site_freq=Counter()

i=0    
# Print the site of the first post
while output:
    site_freq.update(output['darkposts'][i]['source']['site'])
    i=i+1

with open(fname,"r") as f:
    for k,v in  c.most_common():
        f.write( "{},{}\n".format(k,v))
