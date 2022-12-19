from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from blog.models import Category, Post


def load():
    print('blog signals loaded.')


@receiver(post_save, sender=Category)
def clear_cache_category_post_save(sender: Category, **kwargs):
    cache.delete('categories')


@receiver(post_delete, sender=Category)
def clear_cache_category_post_delete(sender: Category, **kwargs):
    cache.delete('categories')
    # After `Category` model deleted and related `Post` model deleted, Django doesn't call `post_delete` on signal.
    cache.delete('posts')


@receiver(post_save, sender=Post)
def clear_cache_post_post_save(sender: Post, **kwargs):
    cache.delete('posts')


@receiver(post_delete, sender=Post)
def clear_cache_post_post_delete(sender: Post, **kwargs):
    cache.delete('posts')
