import os
#new folder will be a new project
#directory will be name of our website
def Create_ProjectDirectory(directory):
    if not os.path.exists(directory):
        print('Creating Directory '+directory)
        os.makedirs(directory)

def Create_DataFiles(project_name , base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/cc.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')
        
        
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


#delete content of file
def delete_file_content(path):
    open(path, 'w').close()
    

#prevent data loss using sets
#Read a file and convert each line to set itmes
def file_to_set(filename):
 #  open('Digikala/crawled.txt', 'w').close()
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#set items to lines in file
def set_to_file(links,file):
    with open(file,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

        
            

