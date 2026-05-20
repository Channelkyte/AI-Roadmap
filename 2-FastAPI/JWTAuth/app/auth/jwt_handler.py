import time
import jwt
from decouple import config

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(userId: str):

    payload = {
        "userID": userId,
        "expires": time.time() + 600
    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token_response(token)


def decodeJWT(token: str):

    try:
        decoded_token = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )

        return (
            decoded_token
            if decoded_token["expires"] >= time.time()
            else None
        )

    except:
        return {}