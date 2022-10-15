#!/usr/bin/env python
import sqlite3
import smtplib
import cgi
import json
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from email.mime.text import MIMEText

class RequestHandler(BaseHTTPRequestHandler):
 def do_GET(self):
 self.send_response(200)
 self.send_header('Content-type','text/html')
 self.end_headers()
 self.wfile.write("Parcel sensor service running!")
 return
 
 def do_POST(self):
 data_string = cgi.parse_qs(self.rfile.read(int(self.
headers['Content-Length'])), keep_blank_values=1)
 room = json.loads(data_string.keys()[0])['room']
 my_query = 'INSERT INTO parcel(roomid,datetime) \
 VALUES(%s,CURRENT_TIMESTAMP);' %(room)
 try:
 connection = sqlite3.connect('/home/pi/control.
db',isolation_level=None)
 cursor = connection.cursor()
 cursor.execute(my_query)
 query_results = cursor.fetchone()
 my_response = "New parcel delivered to room ID %s" % 
(room)
 self.send_mail()
 except sqlite3.Error, e:
 my_response = "There is an error %s:" % (e)
 finally:
 print my_response
 connection.close()
 
 def send_mail(self):
 sender = 'XXX@XXXX.com'
 receivers = ['XXX@XXXX.com']
 password = 'XXXXXX'
 fromad = 'Raspberry Pi Parcel Sensor <XXX@XXXX.com>'
 toad = 'Name <XXX@XXXX.com>'
 subject = 'A new parcel has been delivered'
 body = 'A new parcel was delivered.'
 msg = MIMEText(body)
 msg['From'] = fromad
 msg['To'] = toad
 msg['Subject'] = subject
 
 try:
 smtp = smtplib.SMTP('XXXXX', 587)
 smtp.ehlo()
 smtp.starttls()
 smtp.ehlo
 smtp.login(sender, password)
 smtp.sendmail(sender, receivers, msg.as_string())
 print "Successfully sent email"
 smtp.close()
 except smtplib.SMTPException:
 print "Error: unable to send email"
 
 class WebService():
 port = 8081
 def start_server(self):
 server = HTTPServer(('', self.port), RequestHandler)
 server.serve_forever()
if __name__ == "__main__":
 webservice = WebService()
 webservice.start_server()
