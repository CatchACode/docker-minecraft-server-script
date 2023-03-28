#!/usr/bin/python3
import Versions
import os

class VanillaServer():
    
    def setup():
        pathToDir = VanillaServer.path()
        ports = VanillaServer.ports()
        minecraft_version = VanillaServer.minecraftVersion()
        java_version = VanillaServer.javaVersion()
        name = VanillaServer.nameContainer()
        eula = VanillaServer.eula()

        print(f"docker run -d {pathToDir} {ports} {minecraft_version} {eula} {name} itzg/minecraft-server:{java_version}")
        #exec (f"docker run -d {pathToDir} {ports} {minecraft_version} {eula} {name} itzg/minecraft-server:{java_version}")

    # returns a string containing the docker argument "-v {path/to/dir}" or empty if not defined by user
    def path():
        while True:
            dir_path = input("Enter path to where docker will save the container data. Leave empty to use the allocated anonymous volume. This means that when you delete the container, the data will also be deleted!\n")
            if(len(dir_path) == 0):
                return f""
            if(os.path.isdir(dir_path)):
                return dir_path
            else:
                print(f"{dir_path} is not a vaild path to a directory!\n")
    # returns a string containing all ports required by the docker container in format "-p {port}:port} ... -p {port}{port}"
    def ports():
        ports = f""
        while True:
            try:
                main_port = input("On which port should the minecraft server run? Leave empty to use the default port of 25565\n")
                if (len(main_port) == 0):
                    main_port = 25565
                    break;
                elif (main_port.isdigit()):
                    main_port = int(main_port)
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a number in the range 1024:65535\n")
            if (main_port <= 65535 and main_port >= 1024):
                break;
            else:
                print("Please enter a number in the range 1024:66525\n")
        ports += f"-p {main_port}:{main_port}"
        while True:
            try: 
                secondary_ports = input("Enter any other ports required by the server. Leave empty if none are required. Separate the ports with a space and you can reserve a range of ports using the format from:to\n")
                if (len(secondary_ports) == 0): break
                secondary_ports = secondary_ports.split(" ") 
                for port in secondary_ports:
                    if (f":" in port):
                        start = port[:port.find(":")]
                        end   = port[port.find(":")]
                        if (not start.isdigit()) and (not end.isdigit()): raise ValueError
                        ports += f" -p {port}"
                    else:
                        if not port.isdigit(): raise ValueError
                        ports += f" -p {port}:{port}"
                break
            except ValueError:
                print("Invaild input! Please only ports as a numbers and ranges in the format <from:to>, both separated by a space!\n")
        return ports

    # returns a string containing the docker flag setting the minecraft Version
    def minecraftVersion():
        while True:
            try:
                version = input("Enter which minecraft version the server will be! Format x.xx.x or x.xx or latest for the latest version or snapshot for the latest snapshot. Type v to list all available versions or leave empty to use the latest version\n")
                if (version == "v"):
                    print(Versions.minecraft_versions)
                elif (len(version) == 0): return f"-e VERSION=latest"
                elif (Versions.Versions.isValidMinecraftVersion(version.lower())):
                    return f"-e VERSION={version}"
                else: raise ValueError
            except ValueError:
                print(f"{version} is not a vaild version!\n")

    # returns a string containing the docker arg setting the java version <... itzg/minecraft-server:{version}>
    def javaVersion():
        while True:
            try:
                version = input("Enter which java version the container should use. Leave empty to use the lates version. Type v to to list all available version\n")
                if (version == "v"):
                    print(Versions.Versions.java_versions)
                elif (len(version) == 0): return f"{version}"
                elif (Versions.Versions.isVaildJavaVersion(version)):
                    return f"{version}"
            except ValueError:
                print(f"{version} is not a vaild java version! Type v to list all available versions\n")

    def nameContainer():
        name = input("Name your docker container. Leave empty for docker to assign a random name!\n")
        if (len(name) == 0): return ""
        else: return f"--name {name}"

    def eula():
        accept = input("Do you accept the minecraft EULA? If you do not accept the EULA your server will not start!\n")
        
        match accept.lower():
            case "y" | "yes" | "accept":
                return f"-e EULA=TRUE"
            case _:
                print("EULA not ACCEPTED!\n")
                return f"-e EULA=FALSE"
        
        
