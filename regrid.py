import requests
import json
import time



def get_properties_detail():

    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://app.regrid.com/us/az",
    "X-CSRF-Token": "X0gqx/cEQxNdgrlB7P7d8JudBYQoN6SgLrFcbWrHOovhtt/3psWI22L6DBVZf7YHMwu58LyM3lNcQZYByDcQjQ==",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
    }

    cookies = {
        "_session_id": "b997a5acffc5f7d58d94188b4e22d900",
        "_ce.s": "v~866cdba5fb9195d7e4fa58ce807ac80d7ffe576d~lcw~1704929795484~lva~1704913143678~vpv~1~v11.cs~392098~v11.s~213e7880-aff3-11ee-91f3-3d4b19aee676~v11.sla~1704917200333~gtrk.la~lr8f6hln~v11.send~1704929797071~lcw~1704929797071",
        "_CEFT": "Q%3D%3D%3D",
        "_ga": "GA1.2.967596528.1704837850",
        "_gid": "GA1.2.1635511591.1704837850",
        "_ga_NGWML8455J": "GS1.1.1704929797.7.0.1704929797.0.0.0",
        "__cf_bm": "aKOOuJZ2S58IlEUyMn__MTzZ5MS_GO07Lbp1o8tUiGk-1704973565-1-AVEfi9M5Hh2FEhpuJWpDUbr7e8uv7xrcntS795bi84OOEEP7UUrqPOt7YF94Qtfwy6d+hOHhQeqBEBMp4LqzPXE=",
        "__cfruid": "a9e3aead9dcd16abbc90d43a407b7efaa73db25c-1704973565"
    }

    states_county=[]
    file_path='output_county.txt'
    

    with open(file_path, 'r') as file:
        states_county=[line.strip() for line in file]
        
    for county in states_county:
        pages=1

        while True:
            url= 'https://app.regrid.com'+county+'/laguna-pine-valley'+'/'+str(pages)+'.json?source_ids=&current_region_path=&_='
            response=requests.get(url,headers=headers, cookies=cookies)
            
            if response.status_code==200:
                json_data = json.loads(response.text)            
                file_path = 'details_properties.txt'
               
                with open(file_path, 'a') as file:
                    file.write(json.dumps(json_data, indent=2) + '\n')

            else:
                break
            
            time.sleep(5)
            pages=pages+1

            


if __name__ == "__main__":
    
    get_properties_detail()

