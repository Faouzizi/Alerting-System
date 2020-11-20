####################################################################
######### import packages
####################################################################
import os

####################################################################
######### import environnemental variables 
######### variables will be used to connect to email server...
####################################################################
mysql_user = os.getenv("mysql_user")
mysql_password = os.getenv("mysql_password")
mysql_host = os.getenv("mysql_host")
mysql_db = os.getenv("mysql_db")
smtp_password = os.getenv("smtp_password")
smtp_email = os.getenv("smtp_email")
recipient_list = list(os.getenv("recipient_list").split(','))
