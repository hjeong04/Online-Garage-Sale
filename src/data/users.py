import mongoengine

from data.garage_sales import Garage_Sale
from data.items import Item


class User(mongoengine.EmbeddedDocument):

    # data required as a customer
    attended_gs = mongoengine.EmbeddedDocumentListField('Garage_Sale')
    bought_items = mongoengine.EmbeddedDocumentListField('Item')

    # data required as a host
    hosted_gs = mongoengine.EmbeddedDocumentListField('Garage_Sale')
    hosting_gs = mongoengine.EmbeddedDocumentListField('Garage_Sale')
    will_host_gs = mongoengine.EmbeddedDocumentListField('Garage_Sale')

    meta = {
        'db_alias': 'core',
        'collection': 'hosts'
    }
