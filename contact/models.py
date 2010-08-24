from django.db import models

# Create your models here.
class Profile (xml_models.Model):
    user_id = xml_models.IntField(xpath='/profile/@id')
    email = xml_models.CharField(xpath='/profile/email')
    first = xml_models.CharField(xpath='/profile/first_name')
    last = xml_models.CharField(xpath='/profile/last_name')
    birthday = xml_models.DateField(xpath='/profile/date_of_birth')
    
    finders = {
        (user_id,): settings.API_URL + '/api/v1/profile/userid/%s',
        (email,): settings.API_URL + '/api/v1/profile/email/%s',
    }
    
profile = Profile.objects.get(user_id=4)
print profile.email
# would print 'joe@example.com'