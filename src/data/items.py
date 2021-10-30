import mongoengine

from data.garage_sales import Garage_Sale


class Item:
    image = mongoengine.ImageField(required=True)
    price = mongoengine.FloatField(required=True)
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField(required=True)

    garage_Sale = mongoengine.EmbeddedDocumentField(Garage_Sale)

    meta = {
        'db_alias': 'core',
        'collection': 'items'
    }
