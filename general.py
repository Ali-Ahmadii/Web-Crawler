import os
#new folder will be a new project
#directory will be name of our website
def Create_ProjectDirectory(directory):
    if not os.path.exists(directory):
        print('Creating Directory '+directory)
        os.makedirs(directory)
Create_ProjectDirectory('digikala')
def Create_DataFiles(project_name , base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        create_text_file(queue,base_url)
    if not os.path.isfile(crawled):
        create_text_file(crawled,'')
        
def create_text_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()
    
Create_DataFiles('digikala','https://digikala.com/')    
    
#add data
def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')


#delete content of file
def delete_file_content(path):
    with open(path ,'w'):
        pass
    

#prevent data loss using sets
#Read a file and convert each line to set itmes
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#set items to lines in file
def set_convert_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        write_to_file(file,link)

        
            

