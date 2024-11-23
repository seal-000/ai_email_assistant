import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .forms import RephraseForm
from .utils.huggingface import rephrase_text
from .models import RephrasedText

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):
    # Initialize rephrased text to an empty string
    rephrased_text = ''

    # Fetch user session data for displaying in the template
    session_user = request.session.get('user')
    session_pretty = json.dumps(session_user, indent=4) if session_user else ''
    
    # Handle the form submission for rephrasing text
    if request.method == 'POST':
        form = RephraseForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_to_rephrase']
            rephrased_text = rephrase_text(text)

            if session_user:
                email = session_user.get('userinfo', {}).get('email')
                if email:
                    # Save the rephrased text to the database
                    RephrasedText.objects.create(
                        user_email=email,
                        original_text=text,
                        rephrased_text=rephrased_text,
                    )

    else:
        form = RephraseForm()

   

    #if session_user:
    #    

    # Render the response with both session data and rephrased text
    return render(
        request,
        "index.html",
        context={
            "session": session_user,
            "pretty": session_pretty,
            "form": form,
            "rephrased_text": rephrased_text,
        }
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def history(request):


    session_user = request.session.get('user')
    session_pretty = json.dumps(session_user, indent=4) if session_user else ''

    email = None
    user_history = []
    if session_user:
        email = session_user.get('userinfo', {}).get('email')
        if email:
            # Retrieve history data for the current user
            user_history = RephrasedText.objects.filter(user_email=email).order_by('-created_at')



    return render(
        request, 
        'history.html', 
        context={
        'session': session_user,
        'pretty': session_pretty,
        'user_history': user_history,
        }
    )