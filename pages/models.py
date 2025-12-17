from django.db import models
import uuid
# Create your models here.
class UserModel(models.Model):
    pass
class PollsModel(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    title=models.CharField(max_length=100, blank=False,null=False)
    description =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True, editable=False)
    #reated_by=models.ForeignKey
    update_at=models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['title']
        verbose_name='Enquete'
        verbose_name_plural='Enquetes'

    
    pass
class PollOptionModel(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    poll_id=models.ForeignKey(PollsModel, on_delete=models.PROTECT)
    option_text=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.option_text
    class Meta:
        ordering=['option_text']
        verbose_name='Opção'
        verbose_name_plural='Opções'
    pass
class VotesModel(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    #user
    poll_id=models.ForeignKey(PollsModel, on_delete=models.PROTECT)
    option_id=models.ForeignKey(PollOptionModel, on_delete=models.PROTECT)
    def __str__(self):
        return self.option_id
    class Meta:
        ordering=['id']
        verbose_name='Voto'
        verbose_name_plural='Votos'
    pass
