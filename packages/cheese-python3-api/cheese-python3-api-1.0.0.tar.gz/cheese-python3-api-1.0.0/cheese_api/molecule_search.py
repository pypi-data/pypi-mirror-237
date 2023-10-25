import requests
from typing import List

class MoleculeSearcher():
    def __init__(self,
                 api_key:str = "",
                 search_type:str = "morgan",
                 search_quality:str = "fast",
                 n_neighbors:int = 10,
                 compute_descriptors:bool = True,
                 compute_properties:bool = True,
                 filter_molecules:bool = True,
                 response_format:str = "json"):

        # Search type
        self.search_type = search_type

        # Search quality
        self.search_quality = search_quality

        # Number of neighbors
        self.n_neighbors = n_neighbors

        # Paste your API key here
        self.api_key = api_key

        # Compute descriptors
        self.compute_descriptors = compute_descriptors
        
        # Compute properties
        self.compute_properties = compute_properties

        # Filter molecules : 'No solvants' filter
        self.filter_molecules = filter_molecules

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


    def search_single(self,query:str,
                      search_type:str = None,
                      n_neighbors:int = None
                      ):
        if search_type is None:
            search_type=self.search_type

        if n_neighbors is None:
            n_neighbors=self.n_neighbors

        # Perform the request
        resp=requests.get("https://api.cheese.themama.ai/molsearch",
                    {"search_input":query,
                    "search_type":search_type,
                    "n_neighbors":n_neighbors,
                    "search_quality":self.search_quality,
                    "descriptors":self.compute_descriptors,
                    "properties":self.compute_properties,
                    "filter_molecules":self.filter_molecules}
                    ,headers={'Authorization': f"Bearer {self.api_key}"
                    },
                    verify=False)
        
        return self.parse_response(resp,response_format="json")
    

    def search_list(self,
                    query:List[str],
                    search_type:str = None,
                    n_neighbors:int = None,
                    response_format:str = None
                      ):
        if search_type is None:
            search_type=self.search_type

        if n_neighbors is None:
            n_neighbors=self.n_neighbors
        
        if response_format is None:
            self.response_format = response_format
            
        # Perform the request
        resp=requests.get("https://api.cheese.themama.ai/molsearch_array",
                    {"search_input":query,
                    "search_type":search_type,
                    "n_neighbors":n_neighbors,
                    "search_quality":self.search_quality,
                    "descriptors":self.compute_descriptors,
                    "properties":self.compute_properties,
                    "filter_molecules":self.filter_molecules}
                    ,headers={'Authorization': f"Bearer {self.api_key}",
                              'Accept': f"application/{response_format}"
                    },
                    verify=False)

        return self.parse_response(resp,response_format)

    

    def search_file(self,filename:str,                    
                    search_type:str = None,
                    n_neighbors:int = None,
                    response_format:str = None):
        file=open(filename,"rb")

        if search_type is None:
            search_type=self.search_type

        if n_neighbors is None:
            n_neighbors=self.n_neighbors
        
        if response_format is None:
            self.response_format = response_format

        resp=requests.post("http://api.cheese.themama.ai/molsearch_file",
                                files={"search_input":file},
                                data={"search_type":self.search_type,
                                "n_neighbors":n_neighbors,
                                "search_quality":self.search_quality,
                                "descriptors":self.compute_descriptors,
                                "properties":self.compute_properties,
                                "filter_molecules":self.filter_molecules},
                                
                                headers={'Authorization': f"Bearer {self.api_key}",
                                            'Accept': f"application/{response_format}"
                                            },
                                verify=False)
        
        return self.parse_response(resp,response_format)