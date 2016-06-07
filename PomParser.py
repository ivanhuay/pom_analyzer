import xml.etree.ElementTree as ET


class PomParser:
    def fromFile(self,file):
        tree = ET.parse(file)
        self.root = tree.getroot()
    def fromString(self,string):
        self.root = ET.fromstring(string)
    def getArtifacts(self):
        for dependency in self.root.findall("./dependencies/dependency"):
            artifactId = dependency.find("artifactId").text;
            groupId = dependency.find("groupId").text;
            print(groupId)
            print(artifactId)
