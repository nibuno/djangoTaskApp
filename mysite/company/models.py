from django.db import models


class Department(models.Model):
    """所属部署"""
    name = models.CharField("名前", max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """社員"""
    name = models.CharField("名前", max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, db_constraint=False,
    )

    def __str__(self):
        return self.name
