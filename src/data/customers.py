from data.garage_sales import Garage_Sale
from data.items_sold import Item

import mongoengine


class Customer(mongoengine.Document):
    # id = mongoengine.ObjectInField()

    attended_gs = mongoengine.EmbeddedDocumentListField(Garage_Sale)
    bought_items = mongoengine.EmbeddedDocumentListField(Item)

    meta = {
        'db_alias': 'core',
        'collection': 'customers'
    }
