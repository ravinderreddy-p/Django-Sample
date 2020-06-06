from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from emp.models import Employee


@registry.register_document
class EmpDocument(Document):
    class Index:
        name = 'emp'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Employee

        fields = [
            'employee_name',
            'employee_dept',
        ]