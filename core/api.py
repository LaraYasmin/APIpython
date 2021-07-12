from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, UploadedFile, File
from ninja.errors import ValidationError

from .schemas import ClienteSchema, Message, ClientesOut, ProductOut, ReviewSchema, ProductsOut, ProductIn
from .models import User, Product, Review

router = Router()


@router.post('/cliente/add', response={201: Message})
def add_client(request, user: ClienteSchema):
    if user.name == 'Lara Yasmin': #test superuser
        User.objects.create_superuser(username=user.name, name=user.name, email=user.email, password=user.password)
        return 201, {'message': 'Cliente registrado com sucesso'}
    try:
        User.objects.create_user(username=user.name, name=user.name, email=user.email, password=user.password)
        return 201, {'message': 'Cliente registrado com sucesso'}
    except ValidationError as e:
        return e


@router.post('/cliente/delete/{cliente_email}', response={200: Message, 422: Message})
def delete_client(request, cliente_email: str):
    if User.objects.filter(email=cliente_email).exists():
        user = get_object_or_404(User, email=cliente_email)
        user.delete()
        return 200, {'message': 'Cliente deletado com sucesso'}
    return 422, {'message': 'Nao existe nenhum cliente com esse email'}


@router.get('/clientes/', response={200: List[ClientesOut]})
def clientes_list(request):
    clientes = User.objects.all()
    return clientes


@router.get('/cliente/{cliente_email}', response={200: ClientesOut, 422: Message})
def get_client(request, cliente_email):
    if User.objects.filter(email=cliente_email).exists():
        user = get_object_or_404(User, email=cliente_email)
        return user
    else:
        return 422, {'message': 'Nao existe nenhum cliente com esse email'}


@router.post('/clientes/wishlist/add/{cliente_email}/{product_id}', response={200: Message, 422: Message})
def add_product_to_client_wishlist(request, cliente_email: str, product_id: int):
    if User.objects.filter(email=cliente_email).exists():
        user = get_object_or_404(User, email=cliente_email)
        product = get_object_or_404(Product, id=product_id)
        user.wishlist.add(product)
        return 200, {'message': f'Produto adicionado a wishlist do Cliente: {user.name}'}
    else:
        return 422, {'message': 'Cliente nao existe'}


@router.post('/clientes/wishlist/delete/product/{cliente_email}/{product_id}', response={200: Message, 422: Message})
def delete_product_to_client_wishlist(request, cliente_email: str, product_id: int):
    if User.objects.filter(email=cliente_email).exists():
        user = get_object_or_404(User, email=cliente_email)
        product = get_object_or_404(Product, id=product_id)
        user.wishlist.remove(product)
        return 200, {'message': f'Produto deletado da wishlist do Cliente: {user.name}'}
    else:
        return 422, {'message': 'Cliente nao existe'}


@router.get('/produtos/', response=List[ProductsOut])
def produtos_list(request):
    produtos = Product.objects.all()
    return produtos


@router.get('/product/{product_id}', response={200: ProductOut})
def get_product(request, product_id: int):
    if Product.objects.filter(id=product_id).exists():
        product = get_object_or_404(Product, id=product_id)
        return product


@router.post('/product/{product_id}/review/add', response={201: Message, 422: Message})
def add_review(request, product_id: int, review: ReviewSchema):
    if Product.objects.filter(id=product_id).exists():
        try:
            product = get_object_or_404(Product, id=product_id)
            reviews = Review.objects.create(product=product, text=review.text, score=review.score)
            return 201, {'message': 'Review Adicionada com sucesso'}
        except ValidationError as e:
            return e
    return 422, {'message': 'Produto nao existe'}
