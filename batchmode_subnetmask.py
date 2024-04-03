import re

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

def process_subnet_mask(subnet_mask):
    if validate_subnet_mask(subnet_mask):
        return "VALID"
    else:
        return "INVALID"

def batch_mode_subnet_masks(input_file, output_file):
    with open(input_file, 'r') as f:
        mask_inputs = f.readlines()
    
    with open(output_file, 'w') as f:
        for mask in mask_inputs:
            mask = mask.strip()
            mask_validity = process_subnet_mask(mask)
            f.write(f"{mask}\n")
            f.write(f"   {mask_validity}\n")

if __name__ == "__main__":
    input_file = input("Enter input file path: ")
    output_file = input("Enter output file path: ")
    batch_mode_subnet_masks(input_file, output_file)
