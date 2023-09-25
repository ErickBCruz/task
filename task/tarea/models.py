from django.db import models
# from user.models import User


# # Create your models here.

# class Tarea(models.Model):
#     titulo = models.CharField(max_length=50, null=False, blank=False)
#     descripcion = models.TextField(null = True, blank = True)
#     fecha_vencimiento = models.DatetimeField(null = False)
#     estado = models.CharField(max_length=50, null=False, blank=False)
#     creador_tarea = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.titulo} - {self.fecha_vencimiento} - {self.estado}'
    

#     class Meta:
#         db_table = 'tarea'