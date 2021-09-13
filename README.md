# Products API
\
*__product Api resources__* :
* category
* product

## Install
---
```
$ pip install -r requirements.txt
```

## Api endpoints
---
`/api/v1/`
### Request(_GET_)

### Response
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "api Overview": "/api/v1/",
    "view/add categories": "/api/v1/category/",
    "delete/edit category": "/api/v1/category/<int:id>",
    "view/add products": "/api/v1/product/",
    "view/edit/delete product": "api/v1/product/<int:id>"
}
```
## Product
## `/api/v1/product`
### Request(_GET_)
view all products

### Response
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

[view all product(id, name, serial_number, description, price, category)]
```
### Request(_POST_)
create new product
```
{
  name,
  serial_number,
  description,
  price,

}
```
## `/api/v1/product/<int:id>`
### Request(_GET_)
view product by id

### Response
```
{
  id,
  name,
  serial_number,
  description,
  price,
  category: []

}
```
### Request(_PUT_)
edit product

### Response
```
{
  id,
  name,
  serial_number,
  description,
  price,
  category: []

}
```
### Request(_DELETE_)
delete the product

## category
## `/api/v1/category`
### Request(_GET_)
view all categories
### Response
```
[
  {
    id,
    name,
    products: []
  }
]
```
### Request(_POST_)
create new Category

```
{
  name
}
```
### Response
```
{
  id,
  name
}
```

## `/api/v1/category/<int:id>`
### Request(_DELETE_)
delete category by id

### Request(_PUT_)
edit category by id
```
{
  name
}
```

### Response
```
{
  id,
  name
}
```
