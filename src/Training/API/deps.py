from fastapi import Header, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

# Hardcoded credentials (for demo)
USERNAME = "admin"
PASSWORD = "Welcome@123"


def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# Simple token auth
def verify_token(x_api_key: str = Header(...)):
    if x_api_key != "912a-112h-su1u-5781":
        raise HTTPException(status_code=401, detail="Invalid token")


# Simple rate limiter (stub)
request_count: dict[str | int, int] = {}


def rate_limiter(client_id: str = Header("default-client")):
    count = request_count.get(client_id, 0)

    if count > 5:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    request_count[client_id] = count + 1
