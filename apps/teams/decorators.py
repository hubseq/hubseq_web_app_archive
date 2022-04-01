from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .roles import is_member, is_admin
from .models import Team, Membership


def login_and_team_required(view_func):
    return _get_decorated_function(view_func, is_member)


def team_admin_required(view_func):
    return _get_decorated_function(view_func, is_admin)


def _get_decorated_function(view_func, permission_test_function):
    @wraps(view_func)
    def _inner(request, *args, **kwargs):
        user = request.user
        team_slug = kwargs['team_slug']
        if not user.is_authenticated:
            return HttpResponseRedirect('{}?next={}'.format(reverse('account_login'), request.path))
        else:
            team = get_object_or_404(Team, slug=team_slug)
            if permission_test_function(user, team):
                request.team = team
                request.team_membership = Membership.objects.get(team=team, user=user)
                request.session['team'] = team.id  # set in session for other views to access
                return view_func(request, *args, **kwargs)
            else:
                # treat not having access to a team like a 404 to avoid accidentally leaking information
                return render(request, '404.html', status=404)

    return _inner
