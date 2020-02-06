from django.db import models

class Signature(models.Model):
    student_levels = (
                ("UG", "Undergraduate Student"),
                ("PG", "Postgraduate Student")
            )
    name = models.CharField(max_length=60, primary_key=True)
    id_hash = models.CharField(max_length=60, primary_key=True)
    department = models.CharField(max_length=60)
    level = models.CharField(max_length=60, choices = student_levels)
    signature_date = models.DateField()
