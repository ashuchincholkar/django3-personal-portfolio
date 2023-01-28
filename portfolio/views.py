from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, redirect
from .models import Project, ProjSummary, ProjSkills, ProjTools, ProjTechStack, OperatigSystems, PersonalSkills, \
    DomainKnowledge, PythonExpossure, Education, ContactME, ProjTechStackNew
from .forms import ContactMeForm


def home(request):
    projects = Project.objects.all()
    profile = ProjSummary.objects.all()[:1]
    skills = ProjSkills.objects.all()
    tools = ProjTools.objects.all()
    techstacks = ProjTechStack.objects.all()
    os_sys = OperatigSystems.objects.all()
    personal_skills = PersonalSkills.objects.all()
    domain_skills = DomainKnowledge.objects.all()
    python_skills = PythonExpossure.objects.all()
    educations = Education.objects.all()
    return render(request, "portfolio/home.html",
                  {"projects": projects, "profile": profile, "skills": skills, "tools": tools,
                   "techstacks": techstacks, "os_sys": os_sys, "personal_skills": personal_skills,
                   "domain_skills": domain_skills, "python_skills": python_skills, "educations": educations})


def tech_stack_view(request, tech_card_number):
    techstack = get_object_or_404(ProjTechStack, pk=tech_card_number)
    description = techstack.tech_description
    return render(request, "portfolio/tech_stack.html", {'techstack': techstack})

def tech_stack_view_static(request, tech_card_number):
    techstack = get_object_or_404(ProjTechStackNew, pk=tech_card_number)
    return render(request, "portfolio/tech_stack.html", {'techstack': techstack})

def contact_me(request):
    if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204) #return no content
    else:
        form = ContactMeForm()
    return render(request, 'portfolio/email.html', {'form': form})


def show_emails(request):
    emails = ContactME.objects.order_by('-create_date')
    return render(request, 'portfolio/received.html', {"emails": emails})

# def tech_stack_view(request, tech_card_number):
#     if request.method == "POST":
#         techstack = TechStackForm(request.POST, pk=tech_card_number)
#         if techstack.is_valid():
#             techstack.save()
#             return redirect('/')
#     else:
#         techstack = TechStackForm()
#     return render(request, "portfolio/tech_stack.html", {'techstack': techstack})


