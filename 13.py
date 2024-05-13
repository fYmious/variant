from ipaddress import ip_network
k = 0
net = ip_network("112.208.0.0/255.255.128.0")
for ip in net:
    bip = f"{ip:b}"
    if bip.count("1") % 11 == 0:
        k += 1

print(k)
