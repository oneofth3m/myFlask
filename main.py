from myFlask import MyFlask
app = MyFlask()

@app.route('/')
def hello_world(*args):
  return 'Hello World'

@app.route('/hi')
def hi(*args):
  return 'Hi ', args

if __name__ == '__main__':
  app.run()
