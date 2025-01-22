import os
from pathlib import Path

from fastapi import HTTPException, UploadFile
from PIL import Image
from sqlmodel import Session

from .models import Images

BASE_PATH = Path("static/products/")


def adapt_image(file: UploadFile, folder: Path = BASE_PATH) -> str:
    """
    Save an image as WebP format and return its path.
    """
    try:
        image = Image.open(file.file)
        filename = Path(file.filename).stem + ".webp"
        file_path = folder / filename

        image.convert("RGB").save(file_path, "webp", quality=85)
        return str(file_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")


def upload_image_list(images_in: list[UploadFile], product_id: int, session: Session):
    images_list = []
    try:
        for img in images_in:
            # Upload image and get URL
            image_url = adapt_image(img)

            # Create image record
            db_image = Images(url=image_url, product_id=product_id)
            session.add(db_image)
            images_list.append(db_image)

        # Commit all images in a single transaction
        session.commit()

        # Refresh all images to get their IDs
        for image in images_list:
            session.refresh(image)

        return images_list

    except Exception as e:
        # Rollback in case of any error
        session.rollback()

        # Clean up any uploaded files if database operation failed
        for image in images_list:
            if image.url:
                file_path = os.path.join(".", image.url.lstrip("/"))
                if os.path.exists(file_path):
                    os.remove(file_path)

        raise HTTPException(status_code=500, detail=f"Error uploading images: {str(e)}")


def upload_image(image_in: UploadFile, product_id: int, session: Session):
    try:
        # Upload image and get URL
        image_url = adapt_image(image_in)

        # Create image record
        db_image = Images(url=image_url, product_id=product_id)
        session.add(db_image)
        session.commit()
        session.refresh(db_image)

        return db_image

    except Exception as e:
        # Rollback in case of any error
        session.rollback()

        # Clean up any uploaded files if database operation failed
        if db_image.url:
            file_path = os.path.join(".", db_image.url.lstrip("/"))
            if os.path.exists(file_path):
                os.remove(file_path)

        raise HTTPException(status_code=500, detail=f"Error uploading image: {str(e)}")
