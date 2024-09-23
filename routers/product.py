from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from typing import Optional, List
from custom_log import log
import time

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = [
    'watch', 'camera', 'phone'
]

# This router shows some examples of custom responses, and headers

@router.post('/')
def create_product(name: str = Form(...)): # need to install python-multipart if you are going to use form data
    products.append(name)
    return products

async def time_consuming_functionality():
    time.sleep(5)
    return "OK"

@router.get('/')
async def get_all_products():
    await time_consuming_functionality()
    log(tag="INF", message="Getting all products")
    data = " " .join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)):
    
    response.headers['custom-response-header'] = "custom response"
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }


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