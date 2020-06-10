from django.db import models

class MediaMention(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField()
    attribution_type = models.CharField(max_length=15,
                                        help_text='E.g. Quote, Feature, Mention, Research, By-line, Op-Ed')
    last_name =  models.CharField(max_length=30)
    andrew_id = models.CharField(max_length=35)
    category = models.CharField(max_length=75)
    publication = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    article_link = models.CharField(max_length=500)

    def __str__(self):
        return '%s - - %s' % (self.last_name, self.publication)

    class Meta:
        ordering = ['-publication_date']