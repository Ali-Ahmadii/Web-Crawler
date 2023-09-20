import threading
from queue import Queue
from spider import spider
from domain import *
from general import *

PROJECT_NAME = 'crawler'
HOMEPAGE = 'https://www.digikala.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
