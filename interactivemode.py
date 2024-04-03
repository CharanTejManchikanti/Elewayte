import re

def validate_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        print(f"Valid IP address: {ip}")
        return True
    else:
        print(f"Invalid IP address: {ip}")
        return False

def validate_subnet_mask(subnet_mask):
    pattern = r'^((255|254|252|248|240|224|192|128|0)\.){3}(255|254|252|248|240|224|192|128|0)$'
    if re.match(pattern, subnet_mask):
        binary_mask = ''.join([bin(int(x)).lstrip('0b').zfill(8) for x in subnet_mask.split('.')])
        if '0' in binary_mask:
            index = binary_mask.index('0')
            if '1' in binary_mask[index:]:
                return True
        return False
    else:
        return False

def ip_to_binary(ip):
    return '.'.join([bin(int(x)).lstrip('0b').zfill(8) for x in ip.split('.')])

def process_ip(ip):
    if validate_ip(ip):
        binary_ip = ip_to_binary(ip)
        print("Binary IP:", binary_ip)
        return binary_ip, "VALID"
    else:
        return "INVALID", ""

def process_subnet_mask(subnet_mask):
    if validate_subnet_mask(subnet_mask):
        return "VALID"
    else:
        return "INVALID"

def interactive_mode():
    ip = input("Enter IP address: ")
    subnet_mask = input("Enter subnet mask: ")
    
    binary_ip, ip_validity = process_ip(ip)
    subnet_mask_validity = process_subnet_mask(subnet_mask)
    
    print("IP address:")
    print("   " + binary_ip + "   " + ip_validity)
    
    print("Subnet mask:")
    print("   " + subnet_mask + "   " + subnet_mask_validity)

if __name__ == "__main__":
    interactive_mode()
