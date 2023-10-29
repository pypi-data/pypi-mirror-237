from django.db import models, transaction

from django_pgrls.utils import get_tenant_model_path


class DomainMixin(models.Model):
    tenant = models.ForeignKey(
        get_tenant_model_path(),
        db_index=True,
        on_delete=models.CASCADE,
        related_name="domains",
    )

    domain = models.CharField(max_length=253, db_index=True)
    folder = models.SlugField(max_length=253, blank=True, db_index=True)

    is_primary = models.BooleanField(default=True)
    redirect_to_primary = models.BooleanField(default=False)

    class Meta:
        abstract = True
        unique_together = (("domain", "folder"),)

    def __str__(self):
        return "/".join([self.domain, self.folder]) if self.folder else self.domain

    @transaction.atomic
    def save(self, *args, **kwargs):
        using = kwargs.get("using")
        domain_list = self.__class__.objects
        if using:
            domain_list = domain_list.using(using)
        domain_list = domain_list.filter(tenant=self.tenant, is_primary=True).exclude(pk=self.pk)
        self.is_primary = self.is_primary or (not domain_list.exists())
        if self.is_primary:
            domain_list.update(is_primary=False)
            if self.redirect_to_primary:
                self.redirect_to_primary = False
        super().save(*args, **kwargs)

    def absolute_url(self, path):
        """
        Constructs an absolute url for this domain / folder and a given path
        """
        folder = self.folder and "/" + self.folder
        if not path.startswith("/"):
            path = "/" + path
        return "//" + self.domain + folder + path
