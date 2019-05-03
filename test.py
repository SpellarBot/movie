import os
import ipdb



# UPLOAD_DIR = "app/static/uploads/"

# UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),  UPLOAD_DIR)



if not os.path.exists(UP_DIR):    # 创建“上传文件夹”
    print("create %s"% UP_DIR)
    os.makedirs(UP_DIR)    # 创建目录
    os.chmod(UP_DIR, 644)  # 授权 r=4, w=2, r=1  # os.chmod(UP_DIR, 'rw')                
        
