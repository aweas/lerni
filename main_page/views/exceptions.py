# -*- coding: utf-8 -*-
from base import *
from pyramid.view import forbidden_view_config
from pyramid.view import notfound_view_config

@forbidden_view_config(renderer='login.mak')
def forbidden(request):
	page={'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public, 'active':'login'}
	next = request.params.get('next') or request.route_url('home')
	login = ''
	logged_in = authenticated_userid(request)
	page['logged_in']=logged_in 
	page['name']=username(logged_in)
	page['allerts'].append([u"Aby zobaczyć tę stronę musisz się zalogować","information","topRight"])
	if logged_in: return HTTPFound(location = next) # "Nie masz wystarczających uprawnień, żeby zobaczyć tą stroną, jeśli uważasz, że to jest błąd wypełnij poniższy formularz"
	return page
	
@notfound_view_config(renderer='login.mak')
def notfound(request):
    return Response('Not found, dude!', status='404 Not Found')