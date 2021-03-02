## Django REST Framework

[Django REST Framework](https://www.django-rest-framework.org/) is the de facto framework for building REST API services with Django.

When using DRF, we can organise the logic in a domain this way:

- `urls.py` - Router and URL configuration.
- `api/rest.py` -  DRF view functions or view classes.
- `serializers.py` - Serialization for models.

Additional ruling for DRF:

* You **should** serialize all models using DRF serializers.
* You **should not** use the [ModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#mixins) Viewsets as they will tightly couple the data layer with the presentation layer.

## Graphene Django

When using Graphene-Django, we can organise the logic in a domain this way:

- `api/graphql.py` - Queries and Mutations.

Additional ruling for Graphene-Django:

* You **should not** tightly link an `DjangoObjectType` to a Django model as this will tightly couple the data layer with the presentation layer. Instead, use a generic `ObjectType`.



[Next up, we'll take a look at testing](testing.md)

or

[Go back to the main page](README.md)