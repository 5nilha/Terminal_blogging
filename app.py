from database import Database
from models.blog import Blog
from menu import Menu

Database.initialize() #initializes the database

menu = Menu()
menu.run_menu()
