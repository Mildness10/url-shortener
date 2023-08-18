import qrcode
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

class ShortenURL(models.Model):
    original_url = models.URLField()
    short_key = models.CharField(max_length=10, unique=True)
    click_count = models.PositiveBigIntegerField(default = 0)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    
    def __str__(self):
        return self.short_key
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.original_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        img_path = f'qrcodes/{self.short_key}.png'
        img.save(img_path, 'PNG')
        self.qr_code.name = img_path
        self.save()