from Models.blacklist import TokenBlacklist
from app import jwt

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    # token = None
    jti = jwt_payload["jti"]
    print(f"{jti=}")
    token = TokenBlacklist.find_token(token=jti)
    print(f"{token=}")
    return token is not None