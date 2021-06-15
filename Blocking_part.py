from website_search_part import website_lists
from datetime import datetime

host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = "127.0.0.1"

while True:
    with open(host_path,"r+") as file:
        content = file.read()
        for site in website_lists :
            if site in content:
                pass
            else:
                file.write(redirect+" "+site+"\n")
    print("All websites are blocked")
    break
