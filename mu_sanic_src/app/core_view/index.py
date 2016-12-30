from sanic import Blueprint
from mu_sanic.render_template import render_template

main = Blueprint('index')

@main.route('/')
async def index(request):
    return render_template('index.html')
