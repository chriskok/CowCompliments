# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    
    pathname = "./cow_annotations/"
    for filename in os.listdir(pathname): 
        dst = str(i) + '.' + filename.split(".")[-1]
        src = pathname + filename 
        dst = pathname + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        print(dst)
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 