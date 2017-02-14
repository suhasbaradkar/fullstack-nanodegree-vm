from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from restaurant_query import query_all ,add_restaurant,return_restaurantName,rename_restaurantName,delete_restaurant
import string
import urlparse
class webServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):
	try:
            if self.path.endswith("/new"):
		self.send_response(301)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		if ctype == 'multipart/form-data': 
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
		output = ""
		output += "<html><body>"
		output += " <h2> Okay, New Restaurant added: </h2>"
		output += "<h1> %s </h1>" % messagecontent[0]
		output += "</body></html>"
		self.wfile.write(output)
		print output
		add_restaurant(messagecontent[0])
		print "Restaurant added %s" %messagecontent[0]

            if self.path.endswith("/edit"):
		self.send_response(301)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		print ctype
		if ctype == 'multipart/form-data': 
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
		output = ""
		output += "<html><body>"
		output += " <h2> Okay, Restaurant renamed: </h2>"
		output += "<h1> %s </h1>" % messagecontent[0]
		output += "</body></html>"
		restaurant_id = str(self.path)
		restaurant_id = restaurant_id.replace("/edit","")
		restaurant_id = restaurant_id.replace("/restaurant/","")
                rename_restaurantName(messagecontent[0],restaurant_id)
                print "Restaurant name update success for %s , %s:", messagecontent[0],restaurant_id
		self.wfile.write(output)
		print output
		#add_restaurant(messagecontent[0])
		#print "Restaurant added %s" %messagecontent[0]

            if self.path.endswith("/delete"):
		self.send_response(301)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		print ctype
		if ctype == 'multipart/form-data' : 
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                if ctype == 'application/x-www-form-urlencoded':
                    print "This is trouble loop"
                    length = int(self.headers.getheader('content-length'))
                    #print length
                    fields = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
                    #print fields
                    messagecontent = fields.get('message')
                    #print messagecontent
                else:
                    print "this shit is not working"   
                print messagecontent[0]
                restaurant_id = str(self.path)
		restaurant_id = restaurant_id.replace("/delete","")
		restaurant_id = restaurant_id.replace("/restaurant/","")
		restaurant_Name = return_restaurantName(restaurant_id)
                if messagecontent[0] == "Yes":
                    print "Now in Deletion loop"
                    output = ""
                    output += "<html><body>"
                    output += " <h2> Okay, Restaurant deleted : %s </h2>" %restaurant_Name
                    #output += "<h1> %s </h1>" ,restaurant_Name 
                    output += "</body></html>"
                    print "Restaurant deleted :%s", restaurant_Name
                    print output
                    self.wfile.write(output)
                    delete_restaurant(restaurant_id)
                                       
                else:
                    output = ""
                    output += "<html><body>"
                    output += " <h2> Okay, Restaurant deletion cancelled</h2>"
                    #output += "<h1> %s </h1>" ,restaurant_Name 
                    output += "</body></html>"
                    print "Restaurant deletion canceled :%s", restaurant_Name
                    self.wfile.write(output)
                    print output
                    
		#add_restaurant(messagecontent[0])
		#print "Restaurant added %s" %messagecontent[0]

	except:
		pass
	
    def do_GET(self):
        try:
            if self.path.endswith("/restaurant"):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		output = ""
		output += "<html><body>"
		#output += "<style>p.indent{ padding-left: 1.8em }</style>"
		output += "<h1><center>Restaurants</center></h1>"
		list = query_all()
		for item in list:
                    output += "<h2>"
                    output += item[0]
                    output += "&#09;"
                    output += "<a href = '/restaurant/"
                    output += str(item[1])
                    output += "/edit'>edit</a>"
                    output += "&#09;"
                    output += "<a href = '/restaurant/"
                    output += str(item[1])
                    output += "/delete'>delete</a>"
                    output += "</h2>"
		output += "<h2><a href = '/restaurant/new'>Add New Restaurant</a></h2>"
		#output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		print output
		self.wfile.write(output)
		return
            if self.path.endswith("/delete"):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		restaurant_id = str(self.path)
                restaurant_id = restaurant_id.replace("/delete","")
		restaurant_id = restaurant_id.replace("/restaurant/","")
                restaurant_name = return_restaurantName(restaurant_id)
		print restaurant_id , restaurant_name
		#output += '''<form method='POST' enctype='multipart/form-data' action='/restautant/delete'><h2>Do you confirm to delete this restaurant?</h2><input name="Delete" type="Button" value ="Delete">&#09;<input name="Cancel" type="Button" value="Cancel"> </form>'''
		output = ""
		output += "<html><body>"
		output += "<h1><center>Restaurant Deletion !</center></h1>"
		output += '''<form method='POST' enctype='multipart/button' action='''
                output += "/restaurant/"
                output += restaurant_id
                output += "/delete"
                #output += '''><h2>Do you confirm to delete this restaurant?</h2><input name="Delete" type="Button" value ="Delete">&#09;<input name="Cancel" type="Button" value="Cancel"> </form>'''
                output += '''><h2>Do you confirm to delete this restaurant (Yes / Cancel) ?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		print output
		self.wfile.write(output)
                print output
		return			

            if self.path.endswith("/restaurant/new"):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		output = ""
		output += "<html><body>"
		output += "<h1><center>Add a new Restaurant</center></h1>"
		#output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'><h2>Name of new Restaurant</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		#print message
		self.wfile.write(output)
		print output
		return						
            if self.path.endswith("/edit"):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		restaurant_id = str(self.path)
		restaurant_id = restaurant_id.replace("/edit","")
		restaurant_id = restaurant_id.replace("/restaurant/","")
                restaurant_name = return_restaurantName(restaurant_id)
		print restaurant_id , restaurant_name
		output = ""
		output += "<html><body>"
		output += "<h1><center>Edit Restaurant Name</center></h1>"
		output += '''<form method='POST' enctype='multipart/form-data' action='''
                output += "/restaurant/"
                output += restaurant_id
                output += "/edit"
                output += '''><h2>Enter new name for Restaurant</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		print output
		self.wfile.write(output)
                print output
		return						


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
	
			

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
