#!/bin/sh

# query="""CREATE DATABASE "$MYSQL_TEST_DATABASE"; GRANT ALL PRIVILEGES ON "$MYSQL_TEST_DATABASE".* TO '"$MYSQL_USER"'@'%'; FLUSH PRIVILEGES;"""
query="""GRANT ALL PRIVILEGES ON *.* TO '"$MYSQL_USER"'@'%'; FLUSH PRIVILEGES;"""
mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$query"
