from urllib.request import urlopen
from links import LinkFinder
from general import *
class spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    
    def __init__(self, project_name,base_url,domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queue_file = spider.project_name + '/queue.txt'
        spider.crawled_file = spider.project_name + '/crawled'
        self.boot()
        self.crawl_page('Spider Man',spider.base_url)
        
    @staticmethod
    def boot(self):
        Create_ProjectDirectory(spider.project_name)
        Create_DataFiles(spider.project_name,spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_id,page_url):
        if page_url not in spider.crawled:
            print(thread_id, 'crawling ' +page_url)
            print('Queue ' +str(len(spider.queue)) + ' | crawled')
            spider.add_links_to_queue(spider.gather_link(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_files()
            
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_byte = response.read()
                html_string = html_byte.decode("utf-8")
            finder = LinkFinder(spider.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Error : can not crawl page')
            return set()
        return finder.page_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domain_name not in url:
                continue #preventing whole internet crawling :)
            spider.queue.add(url)
            
    @staticmethod
    def update_files():
        set_convert_to_file(spider.queue, spider.queue_file)
        set_convert_to_file(spider.crawled,spider.crawled_file)
            
        
    