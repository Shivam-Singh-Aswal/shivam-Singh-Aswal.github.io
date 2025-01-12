# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


import json
from pathlib import Path
import os


# def index(request):
#     return HttpResponse("Hello, world. You're at the testing index.")

def index(request):
    return render(request, "home2.html")

def about(request):
    return render(request, "about.html")

def schedule(request):
    return render(request, "schedule.html")

# def registerEdLecture(request):
#     return render(request, "regFormEdLecture.html")

# def theTeam(request):
#     return render(request, "theTeam.html")

def attendees(request):
    return render(request, "attendees.html")


# Path to the JSON file
# JSON_FILE_PATH = Path("registrationData.json")
print(__file__)

# Get the directory of the current file
base_dir = os.path.dirname(os.path.abspath(__file__))

JSON_FILE_PATH = Path(f"{base_dir}/static/registrationData.json")
# JSON_FILE_PATH = Path("static/registrationData.json")

def registerEdLecture(request):
    if request.method == "POST":
        print(__file__)
        print("**********INNNNNNNNN***************")
        # Extract data from the form
        name = request.POST.get("name")
        position = request.POST.get("position")
        other_position = request.POST.get("otherPosition")
        institute = request.POST.get("institute")
        domain = request.POST.get("domain")
        other_domain = request.POST.get("otherDomain")
        source = request.POST.get("source")
        other_source = request.POST.get("otherSource")
        comments = request.POST.get("comments")

        # Validate required fields
        if not all([name, position, institute, source]):
            return render(request, 'registration/register.html', {
                'error': 'Please fill in all required fields.'
            })

        # Prepare the data for saving
        registration_entry = {
            "name": name,
            "position": other_position if position == "other" else position,
            "institute": institute,
            "domain": other_domain if domain == "other" else domain,
            "source": other_source if source == "other" else source,
            "comments": comments or ""
        }

        # Read existing data or create a new list
        if JSON_FILE_PATH.is_file():
            with open(JSON_FILE_PATH, "r") as file:
                print("***********FILE FOUND***************")
                registrations = json.load(file)
        else:
            registrations = []

        # Add the new entry
        registrations.append(registration_entry)
        print(registrations)

        # Save back to the JSON file
        with open(JSON_FILE_PATH, "w") as file:
            json.dump(registrations, file, indent=4)

        # Render a success page
        return render(request, "regSuccess.html")

    # Render the form for GET request
    return render(request, "regFormEdLecture.html")
