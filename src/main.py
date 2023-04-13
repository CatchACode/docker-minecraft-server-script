#!/usr/bin/env python3
print("Running")
from simple_term_menu import TerminalMenu
from dataclasses import dataclass
from Versions import Versions
#class DockerCommand:

@dataclass
class DockerCommand:
    minecraft_version: "latest"
    java_version: "latest"
    ports: ["25565"]
    eula: False
    data_directory: ""



def main():
    docker_command = "docker run -d"
    main_menu_items = ["Server Type","Minecraft Version","Java Version","Ports","Data Directory","Start container"]
    main_menu_title = "Main Menu.\nPress Q or ESC to quit!\n"
    main_menu_status_bar = "docker run -d itzg/minecraft-server"
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title
    )


    while not main_menu_exit:

        main_sel = main_menu.show()
        if main_sel == main_menu_items.index("Server Type"):
            type, command = serverType()
            print(f"You selected {type} Server")

        elif main_sel == main_menu_items.index("Minecraft Version"):
            print(f"You selected {minecraftVersion()}")
        elif main_sel == main_menu_items.index("Ports"):
            ports()
        elif main_sel == None:
            main_menu_exit = True

def ports():
    print()
# returns a tuple of the server Type as string and a string containing the necessary docker flags ( Type, Flag )
def serverType():
    server_type_menu_items = [
        "Vanilla",
        "Forge",
        "Fabric",
        "Quilt",
        "Bukkit",
        "Spigot",
        "Paper",
        "Pufferfish",
        "Purpur",
        "Magma",
        "Mohist",
        "Catserver",
        "Loliserver",
        "Canyon",
        "SpongeVanilla",
        "Limbo",
        "Crucible"
    ]
    server_type_menu_title = "Server Type"
    server_type_menu = TerminalMenu(
        menu_entries=server_type_menu_items,
        title=server_type_menu_title
    )
    server_type_sel = server_type_menu.show()
    return server_type_menu_items[server_type_sel], f" -e VERSION={server_type_menu_items[server_type_sel]}"

def minecraftVersion():
    minecraft_version_menu_items = [
        "latest", "snapshot",
        "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19",
        "1.18.2", "1.18.1", "1.18",
        "1.17.1", "1.17",
        "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16",
        "1.15.2", "1.15.1", "1.15",
        "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14",
        "1.13.2", "1.13.1", "1.13",
        "1.12.2", "1.12.1", "1.12",
        "1.11.2", "1.11.1", "1.11",
        "1.10.2", "1.10.1", "1.10",
        "1.9.4", "1.9.3", "1.9.2", "1.9.1", "1.9",
        "1.8.9", "1.8.8", "1.8.7", "1.8.6", "1.8.5", "1.8.4", "1.8.3", "1.8.2", "1.8.1", "1.8",
        "1.7.10", "1.7.9", "1.7.8", "1.7.7", "1.7.6", "1.7.5", "1.7.4", "1.7.2",
        "1.6.4", "1.6.2", "1.6.1",
        "1.5.2", "1.5.1", "1.5",
        "1.4.7", "1.4.6", "1.4.5", "1.4.4", "1.4.3", "1.4.2",
        "1.3.2", "1.3.1",
        "1.2.5", "1.2.4", "1.2.3", "1.2.2", "1.2.1",
        "1.1",
        "1.0.1", "1.0"
    ]

    minecraft_version_menu_title = "Minecraft Version"
    minecraft_version_menu = TerminalMenu(
        menu_entries=minecraft_version_menu_items,
        title=minecraft_version_menu_title
    )
    minecraft_version_sel = minecraft_version_menu.show()
    return minecraft_version_menu_items[minecraft_version_sel]



if __name__ == "__main__":
    main()