from sqlmodel import Field, Relationship, SQLModel


class Images(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str
    is_thumbnail: bool = Field(default=False)
    product_id: int | None = Field(default=None, foreign_key="product.id")
    product: "Product" = Relationship(back_populates="images")


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: float = Field(gt=0)
    featured: bool | None = Field(default=False, index=True)
    seo_description: str | None = Field(default=None)
    images: list[Images] | None = Relationship(back_populates="product")


class PublicProduct(SQLModel):
    id: int
    product_name: str
    description: str
    price: float


class UpdateProduct(SQLModel):
    product_name: str | None = None
    description: str | None = None
    price: float | None = Field(gt=0, default=None)
    featured: bool | None = None
    seo_description: str | None = None


class CreateProduct(SQLModel):
    product_name: str
    description: str | None = None
    price: float = Field(gt=0)
    featured: bool | None = False
    seo_description: str | None = None
