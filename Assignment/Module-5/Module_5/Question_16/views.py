import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

def github_dashboard_view(request):
    username = request.GET.get('username')
    repos = []
    error = None

    if username:
        url = f"https://api.github.com/users/{username}/repos"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                repos = response.json()
                # Sort by last updated
                repos.sort(key=lambda x: x['updated_at'], reverse=True)
            elif response.status_code == 404:
                error = f"GitHub user '{username}' not found."
            else:
                error = "GitHub API is currently unavailable."
        except Exception:
            error = "Connection error. Please check your internet."

    return render(request, 'Question_16/github_manager.html', {
        'search_user': username,
        'repos': repos,
        'error': error or request.session.pop('gh_error', None),
        'success_msg': request.session.pop('gh_success', None)
    })

def create_repo_action(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        token = getattr(settings, 'GITHUB_ACCESS_TOKEN', 'your_github_token_here')

        if token == 'your_github_token_here':
            request.session['gh_error'] = "Missing GitHub Access Token. Please add it to settings.py to create repos."
            return redirect('Question_16:github-dashboard')

        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "name": name,
            "description": description,
            "private": False
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                request.session['gh_success'] = f"Successfully created repository: {name}!"
            else:
                data = response.json()
                request.session['gh_error'] = f"GitHub Error: {data.get('message', 'Unknown Error')}"
        except Exception:
            request.session['gh_error'] = "Failed to connect to GitHub for creation."

    return redirect('Question_16:github-dashboard')
