from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
#from django.contrib.syndication.feeds import Feed
#from django.contrib.sitemaps import Sitemap

import datetime
import markdown
from tagging.fields import TagField
from tagging.models import Tag

# Blog Entry Draft Status Constants
ENTRY_STATUS_DRAFT = 0
ENTRY_STATUS_PUBLISHED = 1
    
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, related_name='blogs')
    title = models.CharField(_('title'),max_length=255, unique=True)
    slug = models.SlugField(
        unique_for_date='create_date',
        help_text='Automatically built from title.',
        #prepopulate_from=('title',)
    )
    body_html = models.TextField(_('body_html'),blank=True)
    body_markdown = models.TextField(_('body_markdown')) # included cause trying to use Markdown
    create_date = models.DateField('Date Created', default=datetime.datetime.now, editable=False)
    pub_date = models.DateTimeField ('Date Published', blank=True, null=True, editable=False)
    up_date = models.DateField('Date Updated', auto_now = True, editable=False)
    category = models.ForeignKey('blog.Category')
    tags = TagField()
    enable_comments = models.BooleanField(default=True)
    PUB_STATUS = (
        (ENTRY_STATUS_DRAFT, 'Draft'),
        (ENTRY_STATUS_PUBLISHED, 'Published'),
    )
    status = models.IntegerField(choices=PUB_STATUS, default=0)
    
    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name_plural = 'blogs'
    
    def __unicode__(self):
        return u'%s' % (self.title)

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Draft entries may not have a publication date.')
        # Set the publication date for published items if it hasn't been set already
        if self.status == ENTRY_STATUS_PUBLISHED and not self.pub_date:
            self.pub_date = datetime.datetime.now()
        #return self.cleaned_data
    
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status == ENTRY_STATUS_DRAFT:
            if self.instance and self.instance.status == ENTRY_STATUS_PUBLISHED:
                raise ValidationError('You cannot change published to draft')
        return self.cleaned_data['status']
            
    
    @permalink
    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def get_next_published(self):
        return self.get_next_by_pub_date(status__exact=ENTRY_STATUS_PUBLISHED)
    
    def get_previous_published(self):
        return self.get_previous_by_pub_date(status__exact=ENTRY_STATUS_PUBLISHED)
    
    def get_tags(self):
        return Tag.objects.get_for_object(self)
    
    def save(self):
        self.body_html = markdown.markdown(self.body_markdown, safe_mode=False)
        super(Blog,self).save()
    
    
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})

class VideoSubmission(models.Model):
    videoupload = models.FileField (upload_to='videoupload')
#    relatedsubmission = models.ForeignKey (Submission, null=True)
    comment = models.CharField (max_length=250, blank=True)
    flvfilename = models.CharField (max_length=250, blank=True, null=True)
