from django.contrib import admin
from .models import Project, ProjSummary, ProjSkills, ProjTools, ProjTechStack, OperatigSystems, PersonalSkills, \
    DomainKnowledge, PythonExpossure, Education, ContactME, ProjTechStackNew

admin.site.register(Project)
admin.site.register(ProjSummary)
admin.site.register(ProjSkills)
admin.site.register(ProjTools)
admin.site.register(ProjTechStack)
admin.site.register(OperatigSystems)
admin.site.register(PersonalSkills)
admin.site.register(DomainKnowledge)
admin.site.register(PythonExpossure)
admin.site.register(Education)
admin.site.register(ContactME)
admin.site.register(ProjTechStackNew)
