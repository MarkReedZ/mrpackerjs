
# To test mrpacker put index.html and mrpacker.js in ~/www

from mrhttp import app

app.static_cached("www","~/www")

@app.route('/')
def index(r):
  return "hello world"  

try:
  app.run(cores=1)
except Exception as e:
  print("YAY",e)


