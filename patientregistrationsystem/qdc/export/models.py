from django.contrib.auth import get_user_model
from django.db import models


def get_export_dir(instance, filename):
    return f"export/{instance.export.user.id}/{instance.export.pk}/{filename}"


class Export(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(null=False, auto_now_add=True)
    input_file = models.FileField(upload_to=get_export_dir, null=False, max_length=1000)
    output_export = models.FileField(upload_to=get_export_dir, null=False, max_length=1000)

    def delete(self, *args, **kwargs):
        # self.content.delete() #FIXME
        super().delete(*args, **kwargs)
