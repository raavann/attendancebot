import requests

# returns time table
def update_table(table):
    # get data from API call
    data = requests.get(f'https://www.autoattendance.ml/api/find/{table}').json()


    # excessive api calls OR site error
    # in both cases try after sometime
    if(data['success'] != 1):
        return []
    
    # it is already sorted to nearest start time
    return data['data']



