import json
from werkzeug.security import generate_password_hash

data = [
    {
        'id': 1,
        'name': 'Alice',
        'pw': 'mockturtle11'
    }
]

for d in data:
    d['pw'] = generate_password_hash(d['pw'])

with open('instance/users.json', 'w') as f:
    json.dump(data, f, indent=2)

