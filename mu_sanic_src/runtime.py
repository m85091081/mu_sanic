from sanic import Sanic
from app.core_view.index import main

runapp = Sanic(__name__)
runapp.blueprint(main)
runapp.static('/static','./app/core_static')
runapp.run(host='0.0.0.0', port=8000, debug=True)



