import json
import web

urls = (
    
    # rest API backend endpoints
    "/api/(.*)/(.*)", "static_data",
    
    # front-end routes to load angular app
    "/", "index",
    "/(.+)", "www"
)

class www:
    def GET(self, filename):
        try:
            f = open('www/' + filename)
            if filename.endswith(".css"):
                web.header("Content-Type","text/css")
            return f.read() # or return f.read() if you're using 0.3
        except IOError: # No file named that
            web.notfound()
            
class index:
    def GET(self):
        try:
            f = open("www/index.html")
            return f.read()
        except IOError:
            web.notfound()

class static_data:
    def GET(self, type, name):

	# open file	
	with open("routes/" + type + "/" + name + ".json") as json_data:
		data = json.load(json_data)
		json_data.close()

	return json.dumps(data)
        
app = web.application(urls, globals())
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
