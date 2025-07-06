from ariadne import MutationType
from fastapi import Request
from .models import product_collection
from .jwt_utils import verify_token
from bson.objectid import ObjectId

mutation = MutationType()

@mutation.field("deleteProduct")
def resolve_delete_product(_, info, id):
    request: Request = info.context["request"]
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Falta el token")

    token = auth_header.split(" ")[1]
    user = verify_token(token)

    result = product_collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise Exception("Producto no encontrado")

    return "Producto eliminado correctamente"
