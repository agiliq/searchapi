import urllib
try:
    import json
except ImportError:
    import simplejson as json
url = 'http://api.bing.net/json.aspx?AppId='
app_id = "8414497A6BDB88F4484A90E88834E6729BA57A23"
option = 'web'
query = 'aqiliq'
noOfItems = '5'
final_url = url+app_id+"&Version=2.2&Market=en-US&Query="+query+"&Sources="+option+"&Web.Count="+noOfItems+"&JsonType=raw"
response = urllib.urlopen(final_url)

data = json.loads(response.read())
for k, v in data.items():
     print k, " : ", v
#print final_url


#http://api.bing.net/json.aspx?AppId=8414497A6BDB88F4484A90E88834E6729BA57A23&Version=2.2&Market=en-US&Query=aqiliq&Sources=web&Web.Count=5&JsonType=raw
