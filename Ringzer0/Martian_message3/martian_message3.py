#WRITE UP BY DAROCH
import base64

#Public key in base64
public_key_base64 = b'RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'

#Decode the public key from base64
decoded_key = base64.b64decode(public_key_base64).decode('utf-8')
print('Decoded Public Key:\n', decoded_key)
#Initial strings
original = "EOBD"  # Part of the string for which we want the result to be FLAG
desired_result = "FLAG"
#Convert both strings to bytes
original_bytes = original.encode('utf-8')
desired_result_bytes = desired_result.encode('utf-8')

#Calculate the key for the XOR operation
key_bytes = bytes(a ^ b for a, b in zip(original_bytes, desired_result_bytes))

#Convert the key to string for display
key = key_bytes.decode('utf-8', errors='ignore')
print(f'Calculated key to convert EOBD to FLAG: {key}')

# Perform the XOR operation between the decoded key and the full string
# Ensure the key is the same length as the data
if len(key_bytes) != len(decoded_key):
    # Adjust the length of the key if necessary
    key_bytes = (key_bytes * (len(decoded_key) // len(key_bytes) + 1))[:len(decoded_key)]

# Perform the XOR operation
xor_result = bytes(a ^ b for a, b in zip(decoded_key.encode('utf-8'), key_bytes))

# Convert the result to string for display
xor_result_string = xor_result.decode('utf-8', errors='ignore')

print(f'XOR Result: {xor_result_string}')
