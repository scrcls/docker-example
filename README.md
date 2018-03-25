# 命令

## 启动 
`docker-compose up`

## 重启服务
docker-compose restart web/db

## 重新编译service
docker-compose build --force-rm --no-cache web/db

## 创建django应用
docker-compose run web python manager.py startapp app

## 命令行连接mysql
docker-compose run db mysql -hdb -uroot -prootpassword
