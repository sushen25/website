from django.db import models


STATUS = (
    (0, "Draft"),
    (1, "Active"),
    (2, "Archived"),
)


class BlogPost(models.Model):
    title = models.CharField(max_length=192, unique=True)
    slug = models.SlugField(max_length=192)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

