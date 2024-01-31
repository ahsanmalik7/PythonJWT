from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from datetime import datetime, timedelta

# Replace 'JWT_SECRET' with your actual secret key
JWT_SECRET = 'your_secret_key'

# Create a serializer with the secret key and an expiration time of 30 minutes
token_serializer = URLSafeTimedSerializer(JWT_SECRET, salt='Email_Verification_&_Forgot_password')

def generate_token(email):
    # Generate a token for the email
    return token_serializer.dumps(email, salt='email-verification')

def is_token_valid(token):
    try:
        # Try to load the token, and check if it's expired
        email = token_serializer.loads(token, salt='email-verification', max_age=100)  # 1800 seconds = 30 minutes
        return True, email
    except SignatureExpired:
        # Token has expired
        return False, None
    except BadSignature:
        # Token is invalid
        return False, None

# Example usage:
email = 'example@email.com'
token = generate_token(email)
print(f"Token: {token}")

valid, email_from_token = is_token_valid('ImV4YW1wbGVAZW1hhfhfkuyur67QAAFDSbI2u6iQUFQ')

if valid:
    print("Token is valid.")
    print(f"Email from token: {email_from_token}")
else:
    print("Token is either expired or invalid.")
