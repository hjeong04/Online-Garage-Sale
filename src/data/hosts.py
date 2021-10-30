from data.garage_sales import Garage_Sale
import mongoengine


class Host(mongoengine.EmbeddedDocument):
    id = mongoengine.ObjectInField()

    hosted_gs = mongoengine.EmbeddedDocumentListField(Garage_Sale)
    hosting_gs = mongoengine.EmbeddedDocumentListField(Garage_Sale)
    will_host_gs = mongoengine.EmbeddedDocumentListField(Garage_Sale)

    meta = {
        'db_alias': 'core',
        'collection': 'hosts'
    }
