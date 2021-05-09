
### 将项目文件复制容器

docker cp /Users/huaiyaowang/why/sidework/chatterbotictweb d15032ecef44:/www/

### 进入容器

docker exec -it d15032ecef44 /bin/bash

python manage.py runserver 0.0.0.0:3000

