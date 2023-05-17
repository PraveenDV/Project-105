import os
import cv2

path='Images/'

Images=[]

for files in os.listdir(path):
    name, extension=os.path.splitext(files)

    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
       file_name=path + files
       #print(file_name)
       Images.append(file_name)

count=len(Images)
frame=cv2.imread(Images[0])
print(frame)
height, width, channels=frame.shape
size=(width, height)

print(size)
out=cv2.VideoWriter('Project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1, -1):
    cv2.imread(Images[i])
    out.write(frame)
out.release()
print('done')
       