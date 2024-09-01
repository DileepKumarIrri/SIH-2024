import hashlib
hash_object = hashlib.sha1(b'password is good thing')
hex_dig = hash_object.hexdigest()
print(hex_dig)
print(len(hex_dig))
print(len("4D0FD0D2A009F510E08A30064D53A41F634A9029"))