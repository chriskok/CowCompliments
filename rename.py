# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    
    pathname = "./cow_images/"
    for filename in os.listdir(pathname): 
        splitname = filename.split(".")
        dst = 'cow' + splitname[0] + '.' + splitname[-1]
        src = pathname + filename 
        dst = pathname + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        print(dst)
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 