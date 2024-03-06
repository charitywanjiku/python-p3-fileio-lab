"""def write_file(file_name, file_content):
    file_name+=".txt"
    with open(file_name,"w")as file:
        file.write(file_content)
    

def append_file(file_name, append_content):
    file_name+=".txt"
    with open(file_name,"a")as file:
     file.write(append_content)
    

def read_file(file_name):
    file_name+=".txt"
    with open(file_name,"r")as file:
       return file.read()"""
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:  
     file.write(file_content)
    

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", encoding='utf-8', mode='a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8', mode='r') as file:
        return file.read()
       
    
