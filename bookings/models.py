from django.db import models
from django.contrib.auth import get_user_model
from flights.models import Flight

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'flight')  # 🔐 защита от дубля

    def __str__(self):
        return f"{self.user} - {self.flight}"
