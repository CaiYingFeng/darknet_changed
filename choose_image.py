#用于从一个文件夹中提取部分图片


# # ******************************
# # 提取colmap建图用图片
# # ******************************
# import cv2
# import os

# def read_directory(start_path,end_path):

#     image_name_list=os.listdir(start_path)
      
#     image_name_list.sort()

#     for i in range(0,len(image_name_list)):
#         if i%50==0:
#             continue

#             #print(image_name_list[i])
#         img = cv2.imread(start_path + "/" + image_name_list[i])
#         cv2.imwrite(end_path + "/" + image_name_list[i], img)


# #这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
# read_directory("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center","/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/fc")
# read_directory("/media/autolab/disk_3T/caiyingfeng/mask/front_center","/media/autolab/disk_3T/caiyingfeng/mask/fc")



# ************************
# 分割建图用图片和查询图片
# 将文件夹下的不同类别的文件夹中的部分图片转移到另一个文件夹下的相同类别的文件夹下，并删除原文件夹中的相应图片（类似于剪切）
# ************************
import cv2
import os
def transferPictures(dbpath,querypath):
    if(os.path.exists(dbpath) and os.path.exists(querypath)):

        image_name_list=os.listdir(dbpath)
      
        image_name_list.sort()

        for i in range(0,len(image_name_list)):
            if i%50==0:
                img = cv2.imread(dbpath + "/" + image_name_list[i])
                cv2.imwrite(querypath + "/" + image_name_list[i], img)
                os.remove(dbpath + "/" + image_name_list[i])
    else:
        print("路径不存在")

                #print(image_name_list[i])
        

                             
                        
#transferPictures("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_right","/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query_fr")
transferPictures("/media/autolab/disk_3T/caiyingfeng/mask/front_left","/media/autolab/disk_3T/caiyingfeng/mask/query_fl")




# # # ******************************
# # # 提取查询用图片，同时生成查询图片位姿真值
# # # ******************************
# import cv2
# import os

# def read_directory(start_path,end_path):


#     image_name_list=os.listdir(start_path)
      
#     image_name_list.sort()

#     for i in range(0,len(image_name_list),50):
#         #print(image_name_list[i])
#         img = cv2.imread(start_path + "/" + image_name_list[i])
#         cv2.imwrite(end_path + "/" + image_name_list[i], img)

# def ground_truth(time_path,name_path):
#     f=open(time_path)
#     f_dof=list(f)
#     f.close
#     f=open(name_path)
#     im_name=list(f)
#     im_name.sort()
#     f.close()
#     i_path='/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth.txt'
#     for i in range(0,len(f_dof),50):
#         str_dof=f_dof[i].split(' ',-1)
#         str_name=im_name[i].split('/',-1)
#         name=str_name[-1]
#         name=name.strip("\n")

#         with open(i_path, 'a') as f:   
#                 line=name.strip(".jpg")+' '    
#                 line+=str_dof[1]+' '
#                 line+=str_dof[2]+' '
#                 line+=str_dof[3]+' '
#                 line+=str_dof[4]+' '
#                 line+=str_dof[5]+' '
#                 line+=str_dof[6]+' '
#                 line+=str_dof[7].strip("\n")+' ' 
                
#                 #print(line) 
                
                
        
#                 f.write(line+'\n')




# #这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
# #read_directory("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center","/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query")
# ground_truth('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/front_center.txt','/media/autolab/disk_3T/caiyingfeng/darknet/front_center.txt')#时间戳位姿,darknet用list


