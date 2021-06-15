from django.db import models
from django_quill.fields import QuillField

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
    content = QuillField()
    status = models.IntegerField(choices=STATUS, default=0)

    def can_be_viewed_by(self, user=None):
        # Admin users can view all posts
        if user.is_authenticated:
            return True

        # non admin users can only view active posts, status=1 -> active posts
        if self.status == 1:  # TODO - change status choices to dict
            return True
        else:
            return False

    @property
    def can_be_edited_by(self, user=None):
        return True

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
