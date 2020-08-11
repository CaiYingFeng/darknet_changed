
#用于生成image.txt,最终版，colmap可用
#输入：激光内插后位姿
#darknet使用过的imagelist，crate_imagelist.py产生
#***************************************************************#
# images.txt和database里面image顺序不一样时，改变images.txt使用 #
#**************************************************************#

import sqlite3
import os
from pathlib import Path
import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import os
str='front_left'
f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/'+str+'.txt')#时间戳位姿
f_dof=list(f)
f.close

f=open('/media/autolab/disk_3T/caiyingfeng/darknet/'+str+'.txt')#图片名
im_name=list(f)
im_name.sort()
f.close

i_path=Path('/media/autolab/disk_3T/caiyingfeng/map/model',f'images.txt')#要保存的model的images.txt
conn = sqlite3.connect("/media/autolab/disk_3T/caiyingfeng/map/"+str+".db")#db文件地址
cursor = conn.cursor()
sql = """select * from images"""

cursor.execute(sql)
result = cursor.fetchall()#result[i][1]表示id=i的图片的name
# print(len(result))
# print(len(im_name))

for i in range(0,len(result)):       
    
    for j in range(0,len(im_name)):
        
        str_name=im_name[j].split('/',-1)
        name=str_name[-1]
        name=name.strip("\n")

        
        if name==result[i][1]:

            
            str_dof=f_dof[j].split(' ',-1)
            with open(i_path, 'a') as f:

                qw = float(str_dof[7])        
                qx = float(str_dof[4])
                qy = float(str_dof[5])
                qz = float(str_dof[6])
        
                tx = float(str_dof[1])
                ty = float(str_dof[2])
                tz = float(str_dof[3])
                #print(qw)
        #         r = Quaternion(qw, qx, qy, qz)
        #         rotation = r.rotation_matrix
                r = R.from_quat([qx,qy,qz,qw])
                rotation = r.as_matrix()
        
                translation = np.asarray([tx,ty,tz])
                xyz = -np.dot(np.linalg.inv(rotation),translation)
                xyz = np.reshape(xyz,(1,3))
        #         print(xyz)
        #         print(xyz[0][1])
        
                r = R.from_matrix(np.linalg.inv(rotation))
                r2=r.as_quat()
        

                k=i+1
                line=k.__str__()+' '
                line+=r2[3].__str__()+' '                                 
                line+=r2[0].__str__()+' '
                line+=r2[1].__str__()+' '
                line+=r2[2].__str__()+' '
        
                line+=xyz[0][0].__str__()+' '   
                line+=xyz[0][1].__str__()+' '
                line+=xyz[0][2].__str__()+' '
                line+="1"+' '
                line+=name.__str__()+' '
                
                
        
                f.write(line+'\n'+'\n')
    

conn.close()