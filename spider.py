from urllib.request import urlopen
from links import LinkFinder
from domain import *
from general import *

class Spideee:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    
    def __init__(self, project_name,base_url,domain_name):
        Spideee.project_name = project_name
        Spideee.base_url = base_url
        Spideee.domain_name = domain_name
        Spideee.queue_file = Spideee.project_name + '/queue.txt'
        Spideee.crawled_file = Spideee.project_name + '/cc.txt'
        self.boot()
        self.crawl_page('Spideee Man',Spideee.base_url)
        
    @staticmethod
    def boot():
        Create_ProjectDirectory(Spideee.project_name)
        Create_DataFiles(Spideee.project_name,Spideee.base_url)
        Spideee.queue = file_to_set(Spideee.queue_file)
        Spideee.crawled = file_to_set(Spideee.crawled_file)
    
    @staticmethod
    def crawl_page(thread_id,page_url):
        if page_url not in Spideee.crawled:
            print(thread_id, 'crawling ' +page_url)
            print('Queue ' +str(len(Spideee.queue)) + ' | crawled')
            print('here in crawl_page')
            Spideee.add_links_to_queue(Spideee.gather_link(page_url))
            print('here after crawl_page link gathering dunction calling')
            Spideee.queue.remove(page_url)
            Spideee.crawled.add(page_url)
            Spideee.update_files()
            
    @staticmethod
    def gather_link(page_url):
        print('worked')
        print(page_url)
        html_string = ''
        try:
            response = urlopen(page_url)
            print(response)
            print(response.getheader('Content-Type'))
            if response.getheader('Content-Type') == 'text/html; charset=utf-8':
                html_byte = response.read()
                html_string = html_byte.decode('utf-8')
            ffff = LinkFinder(Spideee.base_url,page_url)
            ffff.feed(html_string)
        except Exception as e:
            print('Error:', e)
            return set()
        print(ffff.page_links())
        return ffff.page_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spideee.queue:
                continue
            if url in Spideee.crawled:
                continue
            if Spideee.domain_name not in url:
                continue #preventing whole internet crawling :)
            Spideee.queue.add(url)
            
    @staticmethod
    def update_files():
        set_to_file(Spideee.queue, Spideee.queue_file)
        set_to_file(Spideee.crawled,Spideee.crawled_file)
            
        
    