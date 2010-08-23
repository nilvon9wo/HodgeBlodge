from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save

import twitter

def posted_blog(sender, created=None, instance=None, **kwargs):
    ''' Listens for a blog post to save and alerts some services. '''
    if (created and instance is not None):
        tweet = 'New blog post! %s' % instance.title
        t = twitter.PostUpdate(
            settings.TWITTER_USER, settings.TWITTER_PASSWD, tweet
        )
        cache.set(instance.cache_key, instance, 60*5)
        # send pingbacks
        # ...
        # whatever else
    else:
        cache.delete(instance.cache_key)

post_save.connect(posted_blog, sender=Blog)