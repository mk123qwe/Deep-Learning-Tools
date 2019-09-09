import cv2
import os
rootdir = 'D:\\...\\images'                                 #set your dir
list = os.listdir(rootdir)                                  #List all directories and files under folders
list.sort()                                                 #sort
l = len(list)
for i in range(0,l):
    # path = os.path.join(rootdir,list[i])
#   print(path)
    n = 'D:\\...\\images1\\'+"{}.png".format(path[-9:-4])   #Modify by filename
    print(n)    
    # img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
