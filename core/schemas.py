from typing import List

from ninja import Schema, File, UploadedFile
from ninja.errors import ValidationError
from pydantic import validator, Field
from .models import User


class ClienteSchema(Schema):
    name: str
    email: str
    password: str

    @validator('email', allow_reuse=True)
    def email_is_inexistent(cls, v):
        if v == '':
            raise ValidationError({'email': ('Email nao pode estar vazio',)})
        if not User.objects.filter(email=v).exists():
            return v
        raise ValidationError({'email': ('Email ja cadastrado',)})

    @validator('name', allow_reuse=True)
    def name_is_inexistent(cls, v):
        if v != '':
            return v
        raise ValidationError({'name': ('Nome nao pode estar vazio',)})

    @validator('password', allow_reuse=True)
    def password_is_inexistent(cls, v):
        if v != '':
            return v
        raise ValidationError({'password': ('Senha nao pode estar vazio',)})


class Message(Schema):
    message: str


class WishListProduct(Schema):
    id: int
    title: str
    brand: str
    review_score: float


class ClientesOut(Schema):
    name: str
    email: str
    wishlist: List[WishListProduct]


class ProductsOut(Schema):
    id: int
    title: str
    brand: str
    image: str
    review_score: float


class ReviewSchema(Schema):
    text: str
    score: float = 0.0

    @validator('text', allow_reuse=True)
    def text_is_inexistent(cls, v):
        if v == '':
            raise ValidationError({'text': ('Texto nao pode estar vazio',)})
        return v

    @validator('score', allow_reuse=True)
    def score_is_inexistent(cls, v):
        if v == '':
            raise ValidationError({'score': ('Nota nao pode estar vazio',)})
        return v


class ProductOut(Schema):
    id: int
    title: str
    brand: str
    image: str
    price: float
    review_score: float
    reviews: List[ReviewSchema] = Field(alias='review_set')


class ProductIn(Schema):
    title: str
    brand: str
    price: float