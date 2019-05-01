# movie 项目
#### github: 
    http:   https://github.com/eganchau/movie 
    ssh:    git@github.com:eganchau/movie.git
    user: 240449548@qq.com

#### 代码管理 git:
> 配置好后可使用vscode进行git提交同步；
    
    git init                        # 初始化
    git add .                       # 添加文件
    git commit -m "msg"             # 提交； -m: message
    git push -u origin master       # 同步

#### python 虚拟环境：pipenv:
    # python3
    pip3 install pipenv             # 安装pipenv
    pipenv shell                    # 激活env
    pipenv install packageName      # 安装库
    pipenv install pylint --dev     # --dev: 开发环境包
    pipenv graph                    # 查看已安装库
    pipenv lock -r --dev > requirements.txt    # 生成requirements.txt
    pipenv install -r requirements.txt         # 根据requirements.txt 安装库
    pipenv uninstall packageName    # 删除库

#### doc 项目开发文档
    环境、初始化建库表
    后台模板、前台模板
    后台管理