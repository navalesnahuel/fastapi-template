from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile
from sqlmodel import select

from ..dependencies import SessionDep, current_superuser
from .models import CreateProduct, Images, Product, PublicProduct, UpdateProduct
from .services import upload_image_list

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    response_model=list[PublicProduct],
    status_code=200,
)
async def fetch_products(
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    featured: bool | None = None,
):
    """Fetch all the products from the database
    Fetch all products from the database with optional filters:
    - Pagination: offset and limit.
    - Filter by featured products.
    """
    query = select(Product)
    if featured is not None:
        query = query.where(Product.featured == featured)
    query = query.offset(offset).limit(limit)

    products = session.exec(query).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@router.post(
    "/",
    response_model=PublicProduct,
    dependencies=[Depends(current_superuser)],
    status_code=201,
)
async def create_product(session: SessionDep, product: CreateProduct):
    """Create a new product."""
    db_product = Product.model_validate(product)

    if session.exec(
        select(Product).where(Product.product_name == db_product.product_name)
    ):
        raise HTTPException(status_code=400, detail="Product already created")

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.get("/{product_id}", response_model=PublicProduct, status_code=200)
async def fetch_product(product_id: int, session: SessionDep):
    """Fetch one product by id"""
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put(
    "/{product_id}",
    response_model=PublicProduct,
    dependencies=[Depends(current_superuser)],
)
async def update_product(update: UpdateProduct, product_id: int, session: SessionDep):
    """Update or modify a Product"""
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@router.delete(
    "/{product_id}",
    status_code=200,
    dependencies=[Depends(current_superuser)],
)
async def delete_product(product_id: int, session: SessionDep):
    """Delete a Product"""
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(product)
    session.commit()

    return {"message": f"Product with ID:{product_id} has been deleted succesfully"}


@router.post(
    "/image/{product_id}",
    response_model=list[Images],
    dependencies=[Depends(current_superuser)],
    status_code=201,
)
async def upload_multiple_images(
    product_id: int, session: SessionDep, images_in: list[UploadFile]
):
    return upload_image_list(images_in, product_id, session)


@router.get("/image/{product_id}", status_code=200)
async def get_images(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if not product.images:
        raise HTTPException(status_code=404, detail="The product has no images")

    image_urls = [image.url for image in product.images]
    return {"image_urls": image_urls}
