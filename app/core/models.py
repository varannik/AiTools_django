from django.db import models


class CMST(models.Model):
    '''Defined relationship between Tags and Main, Sub and Career'''

    careers = models.CharField(max_length=255)
    main_categories = models.CharField(max_length=255)
    sub_categories = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)


class Platforms(models.Model):
    '''existing platforms and their seperation from other part of url'''

    base_domain = models.URLField(max_length=255)
    sep = models.CharField(max_length=1)
    platform = models.CharField(max_length=255)


class PricingOptions(models.Model):
    '''enum pricing options'''
    
    option = models.CharField(max_length=255)
