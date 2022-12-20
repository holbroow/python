#md5 hash conversion code (hashing)
import hashlib

string = input("Enter input for conversion: ")

hash_obj = hashlib.md5(string.encode())

print(hash_obj.hexdigest())
