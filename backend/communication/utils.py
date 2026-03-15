import secrets
from .models import ApiKeys
from django.contrib.auth.hashers import make_password

def APIkeygeneration(user , name_):
    key = secrets.token_hex(32)
    key_prefix = name_
    name = user.username + ' ' + name_
    user_id = user
    ApiKeys.objects.create(
        key_hash = key,
        key_prefix = key_prefix,
        name = name,
        user = user_id
    )
    return key 