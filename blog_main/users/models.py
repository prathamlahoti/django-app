from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """ User profile generates automatically when users sign up. """
    
    # Height and Width image ratio
    IMG_FIXED_SIZE = 300
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __repr__(self):
        return f"User: {self.user.username} profile"

    def save(self, **kwargs):
        """ Before image get saved, first things first we need
            to check image ratio. If it's bigger than 300, then we
            thumbnail it.
        """

        super().save()
        img = Image.open(self.user_image.path)
        if img.height > self.IMG_FIXED_SIZE or img.width > self.IMG_FIXED_SIZE:
            output_size = self.IMG_FIXED_SIZE, self.IMG_FIXED_SIZE
            img.thumbnail(output_size)
            img.save(self.user_image.path)

