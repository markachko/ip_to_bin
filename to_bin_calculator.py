


ip = input("insert your ip address:\t")
def ip_to_bin(ip):
    return '.'.join(f"{int(octet):08b}" for octet in ip.split('.'))

binary_ip = ip_to_bin(ip)
print(f"Binary representation: {binary_ip}")
