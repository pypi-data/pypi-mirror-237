from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

from netbox.models import NestedGroupModel, PrimaryModel


class SystemGroup(NestedGroupModel):
    name = models.CharField(
        verbose_name="название",
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        verbose_name="короткий URL",
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = "Группа систем"
        verbose_name_plural = "Группы систем"
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('plugins:netbox_subsystems:systemgroup', args=[self.pk])


class System(PrimaryModel):
    """
    A Systems represents an organization served by the NetBox owner. This is typically a customer or an internal
    department.
    """
    name = models.CharField(
        verbose_name="название",
        max_length=100
    )
    slug = models.SlugField(
        verbose_name="короткий URL",
        max_length=100
    )

    group = models.ForeignKey(
        verbose_name="Группа",
        to=SystemGroup,
        on_delete=models.SET_NULL,
        related_name='systems',
        blank=True,
        null=True
    )

    parent = models.ForeignKey(
        verbose_name='Входит в',
        to='self',
        on_delete=models.SET_NULL,
        related_name='child',
        blank=True,
        null=True
    )

    tenant = models.ForeignKey(
        verbose_name="Учреждения",
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        related_name='systems'
    )

    system_security_id = models.CharField(
        verbose_name="SSID",
        max_length=50
    )

    # Generic relations
    contacts = GenericRelation(
        to='tenancy.ContactAssignment'
    )

    clone_fields = (
        'group', 'description',
    )

    class Meta:
        verbose_name = "Система"
        verbose_name_plural = "Системы"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_subsystems:system', args=[self.pk])


class Subsystem(PrimaryModel):
    """
    A Subsystems represents an organization served by the NetBox owner. This is typically a customer or an internal
    department.
    """
    name = models.CharField(
        verbose_name="название",
        max_length=100
    )
    slug = models.SlugField(
        verbose_name="короткий URL",
        max_length=100
    )
    system = models.ForeignKey(
        verbose_name="Система",
        to=System,
        on_delete=models.SET_NULL,
        related_name='subsystems'
    )

    parent = models.ForeignKey(
        verbose_name='Входит в',
        to='self',
        on_delete=models.SET_NULL,
        related_name='child',
        blank=True,
        null=True
    )

    system_security_id = models.CharField(
        verbose_name="SSID",
        max_length=50
    )

    # Generic relations
    contacts = GenericRelation(
        to='tenancy.ContactAssignment'
    )

    class Meta:
        verbose_name = "Подсистема"
        verbose_name_plural = "Подсистемы"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_subsystems:subsystems', args=[self.pk])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.system:
            self.tenant = self.system.tenant
        super().save(*args, **kwargs)
