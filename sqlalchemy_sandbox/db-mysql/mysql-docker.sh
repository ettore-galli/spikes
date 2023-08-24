# Once:
# docker pull mysql

docker run --name mysql-sandbox -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=sandbox -p 3306:3306 -it -d mysql:latest 