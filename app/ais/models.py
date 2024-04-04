from django.db import models

# New Ai details
class SubmitedTool(models.Model):
    '''Submited app by users'''

    submissionId = models.CharField(max_length=100)
    respondentId = models.CharField(max_length=100)
    createdAt = models.DateTimeField()
    toolName = models.CharField(max_length=100)
    toolUrl = models.URLField(max_length=1000)
    shortDescription = models.CharField(max_length=None, null=True, blank=True)
    review = models.CharField(max_length=None, null=True, blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)
    lunchDate = models.DateTimeField(null=True, blank=True)
    logoUrl = models.URLField(max_length=1000, null=True, blank=True)
    priceModel = models.CharField(max_length=100, null=True, blank=True)
    selectedTag = models.CharField(max_length=100)

