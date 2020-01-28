from django_app.models import Brand, Product, Category, Size, Image, Price
from django_project.celery_app import app


@app.task(name='django_app.tasks.save_to_db')
def save_to_db(items):
    for item in items:
        price, currency = item['price'].split() if item['price'] is not None else (None, None)

        brand, created = Brand.objects.get_or_create(name=item['brand'])
        category, created = Category.objects.get_or_create(name=item['category'])

        sizes = []
        for size in item['sizes']:
            s, created = Size.objects.get_or_create(name=size)
            sizes.append(s)

        images = []
        for image in item['images']:
            i, created = Image.objects.get_or_create(url=image)
            images.append(i)

        product, created = Product.objects.get_or_create(
            price=Price.objects.create(price=price, currency=currency),
            brand=brand,
            category=category,
            description=item['description'],
            name=item['title']
        )
        product.sizes.set(sizes)
        product.images.set(images)
