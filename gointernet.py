import requests
def login(user_name,passwd):
    url = "http://10.3.8.211/login"
    data_dict={'user':user_name,'pass':passwd,'line':''}
    r=requests.post(url,data_dict)
def check():
    request_server = "http://www.baidu.com/"
    r = requests.get(request_server)
    authentication_server = r.request.url
    if authentication_server==request_server:
        return True
    else:
        return False

if __name__=='__main__':
    login()
    is_success=check()
    print(is_success)