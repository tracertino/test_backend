from Models.blacklist import TokenBlacklist
from flask_jwt_extended import JWTManager
jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = TokenBlacklist.find_token(token=jti)
    return token is not None