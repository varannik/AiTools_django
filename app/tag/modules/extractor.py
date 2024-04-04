
from core.models import CMST, Platforms, PricingOptions

def TagList(res):
    '''Clean and return tags'''
    words = res.split(",")
    words = [w.strip() for w in words]
    return words


def MainSubStr(tags, model):
    '''Return Main > Sub dependency'''
    mainsublist = []
    for t in tags:

        queryset = model.objects.filter(tag=t)

        for row in queryset:
            
            mainRelSub = row.main_categories + " > " + row.sub_categories
            mainsublist.append(mainRelSub)

    return str(mainsublist).replace("[", "").replace("]","").replace("'", "")


def CareerStr(tags, model):
    '''Return realted Career base on tags'''

    careerlist = []
    for t in tags:
        queryset = model.objects.filter(tag=t).values_list('careers', flat=True)
        queryres = list(queryset)
        careerlist.extend(queryres)
    careerlist = set(careerlist)
    return str(careerlist).replace("{", "").replace("}","").replace("'", "")



def GetDefinedTags():
    '''Get all distinct existing defined tags'''

    queryset = CMST.objects.values_list('tag', flat=True).distinct()
    queryres = list(queryset)
    return queryres


def GetDefinedPricingLabels():
    '''Get all distinct existing defined Pricing Labels'''

    queryset = PricingOptions.objects.values_list('option', flat=True).distinct()
    queryres = list(queryset)
    return queryres


def GetDefinedPlatforms():
    '''Get all distinct existing defined Platforms'''

    queryset = Platforms.objects.values_list('platform', flat=True).distinct()
    queryres = list(queryset)
    return queryres