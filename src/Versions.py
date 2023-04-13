
import requests
class Versions:
    minecraft_versions =[
        "latest","snapshot",
        "1.19.4","1.19.3","1.19.2","1.19.1","1.19",
        "1.18.2","1.18.1","1.18",
            "1.17.1","1.17",
            "1.16.5","1.16.4","1.16.3","1.16.2","1.16.1","1.16",
            "1.15.2","1.15.1","1.15",
            "1.14.4","1.14.3","1.14.2","1.14.1","1.14",
            "1.13.2","1.13.1","1.13",
            "1.12.2","1.12.1","1.12",
            "1.11.2","1.11.1","1.11",
            "1.10.2","1.10.1","1.10",
            "1.9.4","1.9.3","1.9.2","1.9.1","1.9",
            "1.8.9","1.8.8","1.8.7","1.8.6","1.8.5","1.8.4","1.8.3","1.8.2","1.8.1","1.8",
            "1.7.10","1.7.9","1.7.8","1.7.7","1.7.6","1.7.5","1.7.4","1.7.2",
            "1.6.4","1.6.2","1.6.1",
            "1.5.2","1.5.1","1.5",
            "1.4.7","1.4.6","1.4.5","1.4.4","1.4.3","1.4.2",
            "1.3.2","1.3.1",
            "1.2.5","1.2.4","1.2.3","1.2.2","1.2.1",
            "1.1",
            "1.0.1","1.0",
            ]
    java_versions = [
        "latest", "java8", "java8-jdk", "java8-multiarch", "java8-open9", "java8-graalvm-ce", "java11", "java11-jdk",
        "java11-jdk", "java11-openj9", "java17", "java17-jdk", "java17-openj9", "java17-graalvm-ce", "java17-alpine",
        "java19"
    ]

def checkForgeVersion(minecraft_version,forge_version):
    try:
        r = requests.head(f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar")
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def checkFabricVersion(minecraft_version, fabric_version):

