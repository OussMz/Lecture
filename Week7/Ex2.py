test = '192.168.1.100 - - [14/Mar/2024:10:15:23 -0400] "GET /index.html HTTP/1.1" 200 2326'
http_request = test[test.find("]")+2:test.rfind('"')+1]
print(http_request)  