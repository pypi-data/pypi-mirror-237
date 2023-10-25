from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class SubsystemsTypeChoices(ChoiceSet):

    key = 'SubsystemsTypeChoices'

    CHOICES = [
        ('group', 'Группа систем', 'purple'),
        ('system', 'Система', 'green'),
        ('subsystem', 'Подсистема', 'indigo'),
    ]


class Subsystems(NetBoxModel):
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
    parent = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='child',
        related_query_name='childs',
        verbose_name='Входит в'
    )
    type = models.CharField(
        verbose_name="Тип",
        max_length=30,
        choices=SubsystemsTypeChoices
    )

    tenant = models.ForeignKey(
        verbose_name="Учреждения",
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        related_name='subsystems'
    )

    comments = models.TextField(
        verbose_name="комментарий",
        blank=True
    )

    class Meta:
        verbose_name = "Система"
        verbose_name_plural = "Системы"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_subsystems:subsystems', args=[self.pk])

