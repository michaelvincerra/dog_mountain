### MAIN FORMULA ###

from urllib.request import urlopen
import json
import urllib3
import certifi
from pprint import pprint


http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

req = http.request('GET', "https://download.clearlinux.org/releases/current/assets/bundles/bundles.json",  timeout=5.0)
json_data = json.loads(req.data.decode('utf-8'))

def title_check():
    title_ok = ["Titles OK"]
    
    for b in json_data["bundles"]:    
        if b["title"]: 
            title_ok 
        elif any(b["title"])==False:
            pprint(b["title"], indent=4) 
            
def desc_check():
    desc_ok = ["Descriptions OK"]
    
    for d in json_data["bundles"]:
        if d["description"]:
            desc_ok
        elif any(d["description"])==False:
            pprint(d["title"], indent=4) 
        
def tag_check():
    tag_ok = ["Tags OK"]
    
    for t in json_data["bundles"]:
        if t["tags"]:
            tag_ok 
        elif any(t["tags"])==False:
            pprint(t["title"],indent=4) 
                        
def metadata_check():
    """ 
    Return collated results of above formulas
    """
    x = title_check()
    y = desc_check()
    z = tag_check()
  
    for i in x,y,z: 
        return i

metadata_check()
