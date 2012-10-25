from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Stat,
    )

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    stat = Stat(request.params)
    DBSession.add(stat)
    return dict()
