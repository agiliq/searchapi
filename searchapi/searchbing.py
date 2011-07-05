import urllib2
import urllib
try:
    import json
except ImportError:
    import simplejson as json
import logging

class BingException(Exception):
    pass

class Bing(object):
    def __init__(self, app_id, loglevel=logging.INFO):
#	self.app_id = '8414497A6BDB88F4484A90E88834E6729BA57A23'
        self.log_filename = 'log.log'
        self.start_point = 'http://api.bing.net/json.aspx?AppId='
	self.end_point = self.start_point + self.app_id + "&Version=2.2&Market=en-US&Query="
        logging.basicConfig(level=loglevel,
                          format='%(asctime)s %(name)-6s %(levelname)-8s %(message)s',
                          filename=self.log_filename)
        
        
    def talk_to_bing(self, query, sources, extra_args={}):
        query = urllib.quote_plus(query)
        logging.info('Query:%s'%query)
        logging.info('Sources:%s'%sources)
        logging.info('Other Args:%s'%extra_args)
        payload={}
        #payload['Appid'] = self.app_id
        payload['query'] = query
        payload['sources'] = sources
        payload.update(extra_args)
        query_string = urllib.urlencode(payload)
        final_url = self.end_point + query_string + "&Web.Count=&JsonType=raw" 
        logging.info('final_url:%s'%final_url)
        response = urllib.urlopen(final_url)
        data = json.load(response)
        if 'Errors' in data['SearchResponse']:
            logging.info('Error')
            logging.info('data:%s'%data)
            data = data['SearchResponse']
            errors_list = [el['Message'] for el in data['Errors']]
            error_text = ','.join(errors_list)
            raise BingException(error_text)
        logging.info('data:%s'%data)
        return data
    
    def do_web_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=web', extra_args=extra_args)
    
    def do_image_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=image', extra_args=extra_args)
    
    def do_news_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=news', extra_args=extra_args)
    
    def do_spell_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=spell', extra_args=extra_args)
    
    def do_related_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=relatedsearch', extra_args=extra_args)
    
    def do_phonebook_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=Phonebook', extra_args=extra_args)
    
    def do_answers_search(self, query, extra_args={}):
        return self.talk_to_bing(query, sources='&Sources=InstantAnswer', extra_args=extra_args)
