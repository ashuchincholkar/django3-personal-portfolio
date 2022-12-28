import django

from django.db import models
from django.core.validators import EmailValidator, ProhibitNullCharactersValidator


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True, auto_now_add=False)
    role = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    responsibilities = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return self.project_name


class ProjSummary(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class ProjSkills(models.Model):
    skill = models.TextField(max_length=500)


class ProjTools(models.Model):
    tool = models.TextField(max_length=500)


class OperatigSystems(models.Model):
    os_system = models.TextField(max_length=500)


class PersonalSkills(models.Model):
    personal_skills = models.TextField(max_length=1000)


class ProjTechStack(models.Model):
    tech_image = models.ImageField(upload_to="portfolio/tools/")
    tech_summary = models.CharField(max_length=100)
    tech_description = models.TextField(max_length=10000)

    def __str__(self):
        return self.tech_summary


class DomainKnowledge(models.Model):
    domains = models.TextField(max_length=1000)


class PythonExpossure(models.Model):
    python_header = models.CharField(max_length=500)
    python_sk = models.TextField(max_length=1000)

    def __str__(self):
        return self.python_header


class Education(models.Model):
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year_from = models.DateField()
    year_to = models.DateField()

    def __str__(self):
        return self.university


class ContactME(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name + self.email


