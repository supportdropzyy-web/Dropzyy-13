"""
FreshKart 1 - Authentication & Hashing Utilities
"""
import hashlib
import secrets

def hash_password(password: str) -> str:
    """Hash password using SHA-256 with salt."""
    salt = "freshkart_kirana_salt_2026"
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password
