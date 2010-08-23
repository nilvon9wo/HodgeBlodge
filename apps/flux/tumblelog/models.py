from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.syndication.feeds import Feed
from django.dispatch import dispatcher

from FluxHodgeBlodge.apps.flux.blog.models import Blog, ENTRY_STATUS_DRAFT
from FluxHodgeBlodge.apps.flux.links.models import Link

# Create your models here.
class TumbleItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    pub_date = models.DateTimeField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ('-pub_date',)
        
    def __unicode__(self):
        return self.content_type.name

class LatestItems(Feed):
    title = "My Tumblelog: Links"
    link = "/tumblelog/"
    description = "Latest Items posted on mysite.com"
    description_template = 'feeds/description.html'
    
    def items(self):
        return TumbleItem.objects.all.order_by('-pub_date')[:10]
    
def create_tweet_item (sender, instance, signal, *args, **kwargs):
    if 'created' in kwargs:
        if kwargs['created']:
            create = True
            ctype = ContentType.objects.get_for_model(instance)
            if ctype.name == 'link':
                pub_date = instance.date
            else:
                if instance.status == ENTRY_STATUS_DRAFT:
                    create = False
                else:
                    pub_date = instance.pub_date
            
            if create:
                t = TumbleItem.objects.get_or_create(
                    content_type=ctype, 
                    object_id=instance.id,
                    pub_date=pub_date
                )
    
for modelname in [Blog, Link]:
    post_save.connect(create_tweet_item, sender=Blog)
    post_save.connect(create_tweet_item, sender=Link)