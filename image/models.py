from django.db import models

from PIL import Image

from PIL import ImageFilter
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Edge(models.Model):
	date_posted = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='edge')
	outImage = models.ImageField(default='default.jpg', upload_to='edge/out')

	def save(self, *args, **kawrgs):
		super().save(*args, **kawrgs)

		print('****Image **'+self.image.path)

		img = Image.open(self.image.path)

		#self.user=User.objects.all()[0]

        	

		if img.height > 400 or img.width > 400:
			output_size = (400, 400)
			img.thumbnail(output_size)
			img.save(self.image.path)

		outImage = img.filter(ImageFilter.FIND_EDGES)
		outImage.save(self.outImage.path)


'''
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

'''

# Create your models here.
