from django.shortcuts import render

# Create your views here.
from aboutus.models import AboutUs, OurTeam


def aboutus(request):
    about_us_detail: AboutUs = AboutUs.objects.first()
    our_team: OurTeam = OurTeam.objects.all()
    context = {
        'about_us_detail': about_us_detail,
        'our_team': our_team,
    }
    return render(request, 'aboutus.html', context)
