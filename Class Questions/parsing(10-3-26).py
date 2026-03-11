# json module in python
""" import json
f=open("temp2.txt","a+")
data={
    "name":"Anushka",
    "userid":12345,
    "password":"password123"
}
print(f"Original data: {data}")
print(f"Type of data: {type(data)}") """

""" # encrypting data
enc_data=json.dumps(data) # it converts the data into a JSON string format, which is a text format that can be easily stored and transmitted. it is a way to serialize the data, which means to convert it into a format that can be easily stored and transmitted.
print(f"Encrypted data: {enc_data}")
print(f"Type of encrypted data: {type(enc_data)}")
f.write(enc_data)
f.close()

# decrypting data
dec_data=json.loads(enc_data) # it converts the JSON string back into a Python dictionary, which is the original data format. it is a way to deserialize the data, which means to convert it back into its original format after it has been stored or transmitted.
print(f"Decrypted data: {dec_data}")
print(f"Type of decrypted data: {type(dec_data)}")
f.close() """

""" enc_data=json.dumps(data)
original_data=json.loads(enc_data)
print(f"Decrypted data: {original_data}")
print(f"Type of decrypted data: {type(original_data)}")
f.close() """

# pickle module in python
""" import pickle
# using pickle
data={
    "name":"Anushka",
    "userid":12345,
    "password":"password123"
}
print(f"Original data: {data}")
print(f"Type of data: {type(data)}")
# encrypting data
enc_data=pickle.dumps(data) # it converts the data into a byte stream format, which
# is a binary format that can be easily stored and transmitted. it is a way to serialize the data, which means to convert it into a format that can be easily stored and transmitted.
print(f"Encrypted data: {enc_data}")
print(f"Type of encrypted data: {type(enc_data)}")
# decrypting data
dec_data=pickle.loads(enc_data) # it converts the byte stream back into a Python dictionary, which is the original data format. it is a way to deserialize the data, which means to convert it back into its original format after it has been stored or transmitted.
print(f"Decrypted data: {dec_data}")
print(f"Type of decrypted data: {type(dec_data)}") """


