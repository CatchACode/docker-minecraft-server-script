#!/usr/bin/python


class NewServer:
    
    def main():
        print(
f"""Choose which type of minecraft server you want to start!
1.  Vanilla
2.  Forge
3.  Fabric
4.  Quilt
5.  Bukkit/Spigot
6.  Paper
7.  Pufferfish
8.  Purpur
9.  Magma
10. Mohist
11. Catserver
12. Loliserver
13. Canyon
14. Spongevanilla
15. Limbo
16. Crucible
17. Feed the Beast Modpack
18. CurseForge Modpack
19. Packwiz Modpack""")
        type = input()

        match type.lower():
            case "1" | "Vanilla" | "vanilla":
                pass
            case "2" | "Forge" | "forge":
                pass
            case "3" | "Fabric" | "fabric":
                pass
            case "4" | "Quilt" | "quilt":
                pass
            case "5" | "Bukkit" | "bukkit" | "Spigot" | "spigot":
                pass
            case "6" | "Paper" | "paper":
                pass
            case "7" | "Pufferfish" | "pufferfish":
                pass
            case "8" | "Purpur" | "purpur":
                pass
            case "9" | "Magma" | "magma":
                pass
            case "10" | "Mohist" | "mohist":
                pass
            case "11" | "Catserver" | "catserver":
                pass
            case "12" | "Loliserver" | "loliserver":
                pass
            case "13" | "Canyon" | "canyon":
                pass
            case "14" | "Spongevanilla" | "spongevanilla":
                pass
            case "15" | "Limbo" | "limbo":
                pass
            case "16" | "Crucible" | "crucible":
                pass
            case "17" | "ftb" | "feed the beast" | "feed the beast modpack":
                pass
            case "18" | "curseforge" | "curseforge modpack":
                pass
            case "19" | "packwiz" | "packwiz modpack":
                pass





if __name__ == "__main__":
    NewServer.main()
