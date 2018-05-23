from wsgiref.simple_server import make_server
from pyramid.config import Configurator

def hello_world(request):
    return {'Hello':'world'}


def user_name(request):
    name=request.matchdict['name']
    return {'Name':name}

def user_designation(request):
    designation = request.params['pos']
    return {'Designation':designation}

if __name__ == '__main__':
    with Configurator() as config:
        #Routes
        config.add_route('hello', '/')
        config.add_route('username', '/{name}')
        config.add_route('userDesignation', '/user/')

        #Views
        config.add_view(hello_world, route_name='hello', renderer='json')
        config.add_view(user_name, route_name='username', renderer='json')
        config.add_view(user_designation, route_name='userDesignation', renderer='json')
        
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()