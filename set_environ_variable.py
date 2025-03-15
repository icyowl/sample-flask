import os
import secrets

# print(os.environ['FLASK_APP']) # KeyError: 'FLASK_APP'

os.environ['SECRET_KEY'] = secrets.token_hex(16)
os.environ['Alice'] = 'mockturtle'

print(os.environ['SECRET_KEY'])
print(os.environ['Alice'])

print(os.environ['LANG'])