from django.db import models

class CourseManager(models.Manager):
    # Pesquisa com o AND
    def search(self, query):
        return self.get_queryset().filter(
            name__icontains=query, 
            description__icontains=query
            )
    # Pesquisa com o OR
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)         
            )


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        "Data Inicio", null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images', verbose_name="Imagem", null=True, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

    # aqui mostra os campos declara os campos que vai aparecer na tabela
    # no admin
    def __str__(self):
        return self.name
    
    #  Para alterar os titulos e algumas coisas na tabela
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name']