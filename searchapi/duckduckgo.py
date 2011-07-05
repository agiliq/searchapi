import urllib
try:
    import json
except ImportError:
    import simplejson as json
class Duck(object):
	def __init__(self):
		self.end_point='http://api.duckduckgo.com/?q='
	
	def duckduckgo(self,query):
		query_string = urllib.quote_plus(query)
		final_url = self.end_point + query_string + '&format=json&pretty=1'
		response = urllib.urlopen(final_url)
		data = json.load(response)
		return data
		
