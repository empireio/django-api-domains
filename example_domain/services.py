import logging
import uuid
from typing import Dict, Str  # noqa

from .interfaces import AuthorInterface
from .models import Article

logger = logging.getLogger(__name__)


# Plain example
def get_article(*, guid: uuid.UUID) -> Dict:
    article = Article.objects.get(guid=guid)
    author = AuthorInterface.get_author(guid=article.author_guid)
    return {
        'title': article.title,
        'author_name': author.name,
    }


# Class example
class ArticleService:
    @staticmethod
    def get_article(*, guid: uuid.UUID) -> Dict:
        article = Article.objects.get(guid=guid)
        author = AuthorInterface.get_author(guid=article.author_guid)
        return {
            'title': article.title,
            'author_name': author.name,
        }

    @staticmethod
    def create_article(*, title: Str, author_guid: uuid.UUID) -> Dict:
        logger.info('Creating new article')
        new_article = Article.objects.create(title=title, author_guid=author_guid)
        author = AuthorInterface.get_author(guid=new_article.author_guid)
        return {
            'title': new_article.title,
            'author_name': author.name,
        }

    @staticmethod
    def update_article_title_and_author_name(
        *,
        title: Str,
        author_name: Str,
        author_guid: uuid.UUID,
        guid: uuid.UUID,
    ) -> Dict:
        logger.info('Updating article title and author name')
        article = Article.objects.get(guid=guid).update(title=title)
        author = AuthorInterface.update_author_name(
            name=author_name,
            guid=author_guid,
        )
        return {
            'title': article.title,
            'author_name': author.name,
        }
