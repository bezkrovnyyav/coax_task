from hashlib import md5

s = "Python Bootcamp "
hashing_str = md5(b's').hexdigest()

print(hashing_str)
