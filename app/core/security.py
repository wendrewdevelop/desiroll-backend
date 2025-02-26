import bcrypt
import base64
import smtplib
import os
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from fastapi import FastAPI
from datetime import datetime, timedelta, timezone
from typing import Union, List
from fastapi import Depends, FastAPI, HTTPException, status, WebSocket
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from typing_extensions import Annotated
from decouple import config
from app.schemas import Token, TokenData


app = FastAPI()
Base = declarative_base()
pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"
)
access_token_expires = timedelta(hours=1)
expires_at = datetime.now(timezone.utc) + access_token_expires
URL = f'http://localhost:8000' if not "production" in os.environ else f'http://193.203.174.195:8000'
blacklisted_tokens = []
password_reset_tokens = {}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def hash_password(password: str):
    # converting password to array of bytes
    bytes = password.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def check_password(password: str, hash: str):
    userBytes = password.encode('utf-8')
    # checking password
    result = bcrypt.checkpw(userBytes, hash)
    return result


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Defina um padrão, como 15 minutos
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, 
        config("SECRET_KEY"), 
        algorithm=config("ALGORITHM")
    )
    return encoded_jwt


async def get_token(token: str = Depends(oauth2_scheme)):
    return token





