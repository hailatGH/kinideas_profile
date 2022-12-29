from django.db import models

# Create your models here.


class UserPrivilegeModel(models.Model):

    class Meta:
        ordering = ['user_id']

    user_id = models.CharField(
        null=False, blank=False, max_length=1023, primary_key=True)
    privilege = models.IntegerField(null=False, blank=False, default=0)
    created_by = models.CharField(null=False, blank=False, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.user_id)


class SubscribedUsersModel(models.Model):

    class Meta:
        ordering = ['user_id']

    user_id = models.CharField(
        null=False, blank=False, max_length=1023, primary_key=True)
    subscription_type = models.CharField(
        null=False, blank=False, max_length=1023)
    subscription_expiry_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}"


class NoOfSkipsModel(models.Model):

    class Meta:
        ordering = ['user_id']

    user_id = models.CharField(
        null=False, blank=False, max_length=1023, primary_key=True)
    noOfSkips = models.IntegerField(null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}"


class FeatureRelease(models.Model):

    class Meta:
        ordering = ['id']

    isPodcastReleased = models.BooleanField(
        null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
