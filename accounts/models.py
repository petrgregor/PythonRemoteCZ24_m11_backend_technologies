from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, DateField, TextField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    date_of_birth = DateField(null=True, blank=True)
    biography = TextField(null=True, blank=True)
    # identity_card = ...
    # phone_number = ...

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return f"{self.user}"
