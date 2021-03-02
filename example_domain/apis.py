import logging
import uuid
from typing import Dict  # noqa

import graphene
from graphene import ObjectType, relay

from .services import ArticleService

logger = logging.getLogger(__name__)


# Internal API
class ArticleAPI:
    @staticmethod
    def get(*, article_guid: uuid.UUID) -> Dict:
        logger.info('method "get" called')
        return ArticleService.get_article(id=article_guid)


# graphQL Entity
class ArticleEntity(ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    title = graphene.String()
    author_name = graphene.String()


# graphQL mutation
class CreateArticle(relay.ClientIDMutation):
    class Input:
        article_title = graphene.String(required=True)
        author_guid = graphene.UUID(required=True)

    article = graphene.Field(ArticleEntity)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        new_article = ArticleService.create_article(
            title=input.get('article_title'), author_guid=input.get('author_guid')
        )
        return ArticleEntity(
            title=new_article['title'],
            author_name=new_article['author_name'],
        )


# graphQL mutation
class UpdateArticleAndAuthorName(relay.ClientIDMutation):
    class Input:
        article_title = graphene.String(required=True)
        author_name = graphene.String(required=True)
        author_guid = graphene.UUID(required=True)
        article_guid = graphene.UUID(required=True)

    article = graphene.Field(ArticleEntity)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        article = ArticleService.update_article_title_and_author_name(
            title=input.get('article_title'),
            id=input.get('article_guid'),
            author_guid=input.get('author_guid'),
            author_name=input.get('author_name'),
        )
        return ArticleEntity(
            title=article['title'],
            author_name=article['author_name'],
        )


class Mutation:
    create_article = CreateArticle.Field()


class Query:
    article = graphene.Field(ArticleEntity)

    def resolve_article(self, info):
        logger.info(f"graphQL query for article with id {info.get('id')}")
        article = ArticleService.get_article(id=info.get('id'))
        return ArticleEntity(
            title=article['title'],
            author_name=article['author_name'],
        )
