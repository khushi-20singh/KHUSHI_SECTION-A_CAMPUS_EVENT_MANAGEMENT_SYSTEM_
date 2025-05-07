from django.db import models
from django.contrib.auth.models import User


# Model for storing Event data
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
  
    class Meta:
        ordering = ['-date']
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"


# Model for storing Notice data
class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

# Model for storing Certificate data
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"{self.course_name} - {self.user.username}"

    class Meta:
        ordering = ['-issue_date']
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"








