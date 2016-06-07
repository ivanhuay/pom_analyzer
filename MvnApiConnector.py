#!/usr/bin/python3
import requests

class MvnApiConnector:
    def __init__(self):
        self.url = "http://search.maven.org/solrsearch/select"
    def searchArtifact(self,query):
        return self.requestResult("?q="+query+"&rows=20&wt=json")

    def searchVersions(self,groupId,artifactId):

        return self.requestResult('?q=g:"'+groupId+'"+AND+a:"'+artifactId+'"&core=gav&rows=20&wt=json')

    def requestResult(self,queryParams):
        resp = requests.get(self.url+queryParams)
        if( resp.status_code == 200):
            return resp.json()
        else:
            return '{"error":"Error in request: '+self.url+queryParams+'.","status_code":"'+resp.status_code+'"}'
