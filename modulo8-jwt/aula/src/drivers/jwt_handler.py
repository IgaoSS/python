# pylint: disable=E0401,W0102
from typing import Dict
from datetime import datetime, timedelta, timezone
import jwt # type: ignore

class JwtHandler:
    def create_jwt_token(self, body: Dict = {}):
        token = jwt.encode(
            payload = {
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key="minhaChave",
            algorithm="HS256"
        )
        return token

    def decode_jwt_token(self, token: str) -> Dict:
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
        return token_information
