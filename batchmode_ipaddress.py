import re

def validate_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    else:
        return False

def ip_to_binary(ip):
    return '.'.join([bin(int(x)).lstrip('0b').zfill(8) for x in ip.split('.')])

def process_ip(ip):
    if validate_ip(ip):
        binary_ip = ip_to_binary(ip)
        return binary_ip, "VALID"
    else:
        return "INVALID", ""

def batch_mode_ips(input_file, output_file):
    with open(input_file, 'r') as f:
        ip_inputs = f.readlines()
    
    with open(output_file, 'w') as f:
        for ip in ip_inputs:
            ip = ip.strip()
            binary_ip, ip_validity = process_ip(ip)
            f.write(f"{ip}\n")
            f.write(f"   {binary_ip}   {ip_validity}\n")

if __name__ == "__main__":
    input_file = input("Enter input file path: ")
    output_file = input("Enter output file path: ")
    batch_mode_ips(input_file, output_file)
