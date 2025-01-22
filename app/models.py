from django.db import models


class Question(models.Model):
    question_text = models.TextField(verbose_name="Question Text")
    variant_a = models.CharField(max_length=255, verbose_name="Variant A")
    variant_b = models.CharField(max_length=255, verbose_name="Variant B")
    variant_c = models.CharField(max_length=255, verbose_name="Variant C")
    variant_d = models.CharField(max_length=255, verbose_name="Variant D")
    photo = models.ImageField(
        upload_to='photos/questions/', blank=True, null=True, verbose_name="Photo")
