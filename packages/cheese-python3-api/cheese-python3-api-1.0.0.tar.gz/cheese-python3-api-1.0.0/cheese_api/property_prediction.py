import requests
from typing import List

class PropertyPredictor():
    def __init__(self,
                 api_key:str = "",
                 compute_descriptors:bool = True,
                 compute_properties:bool = True,
                 response_format:str = "json"):

        # Paste your API key here
        self.api_key = api_key

        # Compute descriptors
        self.compute_descriptors = compute_descriptors
        
        # Compute properties
        self.compute_properties = compute_properties

        # Response format 
        self.response_format = response_format


    # Parse response based on response format
    def parse_response(self,resp,response_format):
        if response_format=="json":
            return resp.json()

        else:
            return resp.content
    
    def download_csv(self,resp,
                     result_filename=None):
        # Download result file to local storage
        if result_filename is None:
            result_filename=resp.headers["content-disposition"].split()[-1].replace("filename=","")
            save_path="./"
            
        with open(save_path+result_filename,'wb') as new_file:
            new_file.write(resp.content)


    def predict_single(self,query:str):
        # Perform the request
        resp=requests.get("https://api.cheese.themama.ai/predict",
                        {"search_input":query,
                        "descriptors":self.compute_descriptors,
                        "properties":self.compute_properties,
                        },
                        headers={'Authorization': f"Bearer {self.api_key}"
                                 },
                    verify=False)
        
        return self.parse_response(resp,response_format="json")
    

    def predict_list(self,
                    query:List[str],
                    response_format:str = None
                      ):
        
        if response_format is None:
            self.response_format = response_format
            
        # Perform the request
        resp=requests.get("https://api.cheese.themama.ai/predict_array",
                    {"search_input":query,
                    "descriptors":self.compute_descriptors,
                    "properties":self.compute_properties}
                    ,headers={'Authorization': f"Bearer {self.api_key}",
                              'Accept': f"application/{response_format}"
                    },
                    verify=False)

        return self.parse_response(resp,response_format)

    

    def predict_file(self,filename:str,
                    response_format:str = None):
        file=open(filename,"rb")
        
        if response_format is None:
            self.response_format = response_format

        resp=requests.post("http://api.cheese.themama.ai/predict_file",
                                files={"search_input":file},
                                data={"descriptors":self.compute_descriptors,
                                        "properties":self.compute_properties},
                                
                                headers={'Authorization': f"Bearer {self.api_key}",
                                            'Accept': f"application/{response_format}"
                                            },
                                verify=False)
        
        
        return self.parse_response(resp,response_format)