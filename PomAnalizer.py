from MvnApiConnector import MvnApiConnector
from PomParser import PomParser

apiConnector = MvnApiConnector()
pomParser = PomParser()
pomParser.fromFile("example-pom.xml")
pomParser.getArtifacts()

# resp = apiConnector.searchArtifact("log")

# print(resp)
