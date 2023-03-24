#!/usr/bin/python

import os

def VanillaServer():
    
    def setup():
        pass
    
    # returns a string containing the docker argument "-v {path/to/dir}" or empty if not defined by user
    def path():
        while true:
            dir_path = input("Enter path to where docker will save the container data. Leave empty to use the allocated anonymous volume. This means that when you delete the container, the data will also be deleted!")
            if(os.path.isdir(dir_path)):
                return dir_path
            else:
                print(f"{dir_path} is not a vaild path to a directory!")
    # returns a string containing all ports required by the docker container in format "-p {port}:port} ... -p {port}{port}"
    def ports():
        ports = f""
        while True:
            try:
                main_port = int(input("On which port should the minecraft server run?"))
            except ValueError():
                print("Please enter a number in the range 1024:65535")
            if (main_port <= 65535 and main_port >= 1024):
                break;
            else:
                print("Please enter a number in the range 1024:66525")
    
        while True:
            secondary_ports = input("Enter any other ports required by the server. Leave empty if none are required. Separate the ports with a space and you can reserve a range of ports using the format from:to")
            



    # returns a string containing the docker flag setting the minecraft Version
    def minecraftVersion():
        pass



