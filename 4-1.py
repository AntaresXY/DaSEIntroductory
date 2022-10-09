# def convert_ip_address_to_dec(address): 
#     subaddress_list=[] 
#     for i in range(4): 
#         subaddress_list.append(address[i*8:i*8+8]) 
#     decaddress_list=[] 
#     for add in subaddress_list: 
#         decaddress_list.append(int(add,2)) 
#     result=str(decaddress_list[0])+'.'+str(decaddress_list[1])+'.'+str(decaddress_list[2])+'.'+str(decaddress_list[3]) 
#     return result
def dec_to_bi(n):
    num = int(n)
    res = []
    while num > 0:
        res.append(num % 2)
        num = num // 2
    while len(res) < 8:
        res.append(0)
    res.reverse()
    return res

def convert_dec_to_ip_address(ip):     
    ip_dec=ip.split(".")
    ip_bi=[]
    for i in range(4):
        ip_bi.append(dec_to_bi(ip_dec[i]))   
    for i in range(4):
        for j in range(8):
            print(ip_bi[i][j], end = "")
    print("\n")
    return 0

ip = "203.179.25.37"
convert_dec_to_ip_address(ip)