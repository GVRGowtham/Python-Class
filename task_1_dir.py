#import os
#lst=[]
#for root, dirs, files in os.walk("./Tasks/Task 1"):
#	lst.append(dirs)
#print lst
import os
import json

def main():
	dir_list = next(os.walk('./Tasks/Task 1'))[1]
	#return (dir_list)
	lst=dir_list.split()
	return lst
	
	
	
	
if __name__ == "__main__":
    x=main()
	f=open('sam.txt','w+')
	f.write('Python executed')
	f.close()
    return json.dumps(x)