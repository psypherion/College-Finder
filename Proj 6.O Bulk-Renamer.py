import os # Importing library

# Creating a function 
def rename():
   i=1 
   path="E:\\Blog\\" # Path of the fle 
   """
   for path please provide your designated file path and 
   in place of single slashes '\' use double slashes '\\'
   """
   for old_file_name in os.listdir(path):
       new_file_name=f"pic {i}.jpg"  # Creating new file names for old files having 'jpg' extension
       source=path+old_file_name # Old filenames from where the naming should be happened
       destination=path+new_file_name # destination of the new file
       os.rename(source,destination) # Renaming the files of extension 'jpg'
       i += 1 
       
if __name__=="__main__": 
   rename()
