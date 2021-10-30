import mongoengine

from data.items_sold import Item


class Garage_Sale(mongoengine.EmbeddedDocument):
    # garage_id = mongoengine.ObjectIdField()
    host_id = mongoengine.ObjectIdField()
    date = mongoengine.DateTimeField(required=True)
    location = mongoengine.PointField(required=True)
    QR_code = mongoengine.ImageField()

    items_bought = mongoengine.EmbeddedDocumentListField(Item)
    items_not_bought = mongoengine.EmbeddedDocumentListField(Item)

    meta = {
        'db_alias': 'core',
        'collection': 'garage_sales'
    }
