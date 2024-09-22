from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = [
    'watch', 'camera', 'phone'
]

# This router shows some examples of custom responses

@router.get('/')
def get_all_products():
    data = " " .join(products)
    return Response(content=data, media_type="text/plain")

@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns the product in HTML format"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        },
        "description": "A cleartext error message"
    } 
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type="text/plain", status_code=404)

    product = products[id]
    out = f"""
    <head>
        <style>
            .product {{
             width: 500px;
             height: 30px;
             border: 2px inset green;
             background-color: lightblue;
             text-align: center;
            }}
        </style>
    <head>
    <div class="product">{product}</div>
"""
    return HTMLResponse(content=out, media_type="text/html")