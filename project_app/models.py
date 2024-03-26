from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):

    # cria uma tabela no banco de dados
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self):
        # mostra o que aparece quando for printar
        return self.text
    
class Entry(models.Model):
    
    # Conectando a foreign key ao Topic, com exclusao em cascata
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    text = models.TextField()
    # TextField = campo de texto sem limites

    # adicionando data de criacao
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text

