from django.db import models

# Create your models here
class BitwiseOperation(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()

    def bitwise_and(self):
        return self.a & self.b

    def bitwise_or(self):
        return self.c | self.d

    def bitwise_xor(self):
        return self.e ^ self.a

    def left_shift(self):
        return self.b << 2

    def right_shift(self):
        return self.c >> 2

    def __str__(self):
        return f"Bitwise Operations: {self.a}, {self.b}, {self.c}, {self.d}, {self.e}"