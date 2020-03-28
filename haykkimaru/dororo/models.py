from django.db import models

# Create your models here.

class partesCuerpo(models.Model):

    nombreParteCuerpo = models.CharField(
        max_length = 30,
        null = False,
    )
    def __str__(self):
        return '{}'.format(self.nombreParteCuerpo)

class Ubicaciones(models.Model):

    nombreUbicacion = models.CharField(
        max_length = 30,
        null = False,
    )
    def __str__(self):
        return '{}'.format(self.nombreUbicacion)

class Resultados(models.Model):

    derrotado = models.CharField(
        max_length = 2,
        null = False,
    )
    def __str__(self):
        return '{}'.format(self.derrotado)

class Demonios(models.Model):

    parteCuerpo = models.ForeignKey(partesCuerpo, on_delete=models.CASCADE)
    lugarHogar = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    derrotado = models.ForeignKey(Resultados, on_delete=models.CASCADE)
    nombreDemonio = models.CharField(
        max_length = 30,
        null = False,
    )
    fotoDemonio = models.ImageField(upload_to="demonios", null=True)
    def __str__(self):
        return '{}'.format(self.nombreDemonio)

class Peleas(models.Model):

    lugarPelea = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    id_Demonio = models.ForeignKey(Demonios, on_delete=models.CASCADE)
    ganadorDemonio = models.ForeignKey(Resultados, on_delete=models.CASCADE)

class articulosDororo(models.Model):

    nombreArticulo = models.CharField(
        max_length = 50,
        null = False,
    )
    procedenciaArticulo = models.CharField(
        max_length = 50,
        null = False,
    )
    castigoDororo = models.ForeignKey(Resultados, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombreArticulo)
   
# Images

class Album(models.Model):
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

class albumImage(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='album/images/')
    def __unicode__(self,):
        return str(self.image)