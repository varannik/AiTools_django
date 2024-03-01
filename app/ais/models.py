from django.db import models

# New Ai details
class SubmitedTool(models.Model):
    '''Submited app by users'''

    submissionId = models.CharField(max_length=100)
    respondentId = models.CharField(max_length=100)
    createdAt = models.DateTimeField()
    toolName = models.CharField(max_length=100)
    toolUrl = models.URLField(max_length=1000,)
    shortDescription = models.CharField(max_length=None)
    review = models.CharField(max_length=None,)
    platform = models.CharField(max_length=100, )
    lunchDate = models.DateTimeField()
    logoUrl = models.URLField(max_length=1000, )
    priceModel = models.CharField(max_length=100, )
    selectedTag = models.CharField(max_length=100, )

