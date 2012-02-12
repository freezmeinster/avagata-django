from django import template
from landing.models import LandingConfig

register = template.Library()

@register.simple_tag
def get_feature(feature_id):
    feat = LandingConfig.objects.get(key="feature_%s" % feature_id)
    return feat.value
