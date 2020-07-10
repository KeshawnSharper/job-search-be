from django.shortcuts import render
from django.http import JsonResponse
# 3rd party
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import PostSerializer
import sqlite3
# Create your views here.
# class PostView(APIView):
# 	serializer_class = PostSerializer
# 	qs = User.objects.all()
class TestView(APIView):
	# permission_classes = (IsAuthenticated,)
	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		print(request.data)

		if 'username' in request.data:
			cursor.execute("SELECT * FROM users WHERE username=?", (request.data['username'],))
		else:
			cursor.execute("SELECT * FROM users")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO users (first_name,last_name,email,portfolio,current_location,birthday,high_school,college,role,online,gender,username,bio,picture) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(req['first_name'],req['last_name'],req['email'],req['portfolio'],req['current_location'],req['birthday'],req['high_school'],req['college'],req['role'],req['online'],req['gender'],req['username'],req['bio'],req['picture']) )
		connection.commit()
		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE users SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class ExperienceView(APIView):
	# permission_classes = (IsAuthenticated,)
	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		if 'id' in request.data:
			cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		else:
			cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,previous_jobs.date_ended,previous_jobs.location,previous_jobs.role,previous_jobs.id,previous_jobs.users_id FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id WHERE previous_jobs.users_id=?",(kwargs['id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO previous_jobs (description,company,date_started,date_ended,location,role,users_id) VALUES (?,?,?,?,?,?,?);",(req['description'],req['company'],req['date_started'],req['date_ended'],req['location'],req['role'],req['users_id']) )
		connection.commit()
		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE previous_jobs SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,previous_jobs.date_ended,previous_jobs.location,previous_jobs.role,previous_jobs.id,previous_jobs.users_id FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class DeleteExperienceView(APIView):
	# permission_classes = (IsAuthenticated,)
	
	
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("DELETE FROM previous_jobs WHERE id = ?;",(req['id']) )
		connection.commit()
			# serializer =PostSerializer(data = request.data )
			# if serializer.is_valid():
			# 	serializer.save()
		return Response(request.data)
	# def delete(self,request,*args,**kwargs):
	# 	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	# 	cursor = connection.cursor()
	# 	req = request.data
	# 	print(id)
	# 	cursor.execute(f"DELETE FROM previous_jobs WHERE id = ?;",(req['id']) )
	# 	connection.commit()
	# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,previous_jobs.date_ended,previous_jobs.location,previous_jobs.role,previous_jobs.id,previous_jobs.users_id FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
	# 	results = cursor.fetchall()
	# 	data = []
	# 	# if request.data['id']
	# 	for row in results:
	# 		object1 = {}
	# 		col_name_list = [tuple[0] for tuple in cursor.description]
	# 		for x in range(0,len(col_name_list) ):
	# 			object1[col_name_list[x]] = row[x]
	# 		data.append(object1)
	# 	cursor.close()

	# 	# serializer =PostSerializer(data = request.data )
	# 	# if serializer.is_valid():
	# 	# 	serializer.save()
	# 	return Response(data)
        	# return Response(serializer.errors)
# @api_view(['POST', ])
# def registration_view(request):

# 	if request.method == 'POST':
# 		serializer =RegisterSerializer(data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			account = serializer.save()
# 			data['response'] = 'successfully registered new user.'
# 			data['email'] = account.email
# 			data['username'] = account.username
# 		else:
# 			data = serializer.errors
# 		return Response(data)
        
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # return Response(serializer.errors)
class ProjectView(APIView):
	# permission_classes = (IsAuthenticated,)
	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		print(kwargs['id']) 
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id WHERE projects.users_id=?",(kwargs['id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO projects (description,name,date_started,date_ended,role,users_id) VALUES (?,?,?,?,?,?);",(req['description'],req['name'],req['date_started'],req['date_ended'],req['role'],req['users_id']) )
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class JobView(APIView):
	# permission_classes = (IsAuthenticated,)
	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		cursor.execute("SELECT * FROM jobs ")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO jobs (description,role,users_id,city,company,state,date) VALUES (?,?,?,?,?,?,?);",(req['company'],req['description'],req['date'],req['state'],req['city'],req['role'],req['users_id']) )
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class MessagesView(APIView):
	# permission_classes = (IsAuthenticated,)
	connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		print(kwargs)
		cursor.execute("SELECT messages.id,messages.users_id,messages.sender_id,users.picture,users.picture,users.first_name,messages.note,messages.read,messages.time FROM messages JOIN users ON sender_id=users.id   WHERE users_id=? OR sender_id=? ", (kwargs['id'],kwargs['id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO messages (note,users_id,sender_id,read,time,date ) VALUES (?,?,?,?,?,?);",(req['note'],req['users_id'],req['sender_id'],req['read'],req['time'],req['date'] ))
		connection.commit()
		cursor.execute("SELECT messages.id,messages.users_id,messages.sender_id,users.picture,users.picture,users.first_name,messages.note,messages.read,messages.time FROM messages JOIN users ON sender_id=users.id WHERE users_id=? OR sender_id=? ", (req['sender_id'],req['sender_id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data[len(data) - 1])
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class PostsView(APIView):
	# permission_classes = (IsAuthenticated,)
	# connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	# cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		print(kwargs)
		cursor.execute("SELECT posts.id,posts.users_id,users.picture,users.first_name,posts.note,posts.date,posts.time FROM posts JOIN users ON users_id=users.id ")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO posts (note,users_id,comments,time,date,likes ) VALUES (?,?,?,?,?,?);",(req['note'],req['users_id'],req['comments'],req['time'],req['date'],req['likes'] ))
		connection.commit()
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
class RequestsView(APIView):
	# permission_classes = (IsAuthenticated,)
	# connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	# cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		print(kwargs)
		cursor.execute("SELECT * FROM friend_requests WHERE users_id=?", (kwargs['id'],))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO friend_requests (users_id,request_id ) VALUES (?,?);",(req['users_id'],req['request_id'] ))
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
	def delete(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(kwargs)
		cursor.execute("SELECT * FROM friend_requests WHERE users_id = ? AND request_id = ?;",(kwargs['users_id'],kwargs['request_id']))
		results = cursor.fetchall()
		req = request.data
		
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		# cursor.close()
		for key in request.data: 
    			print(key) 
		cursor.execute(f"DELETE FROM friend_requests WHERE users_id = ? AND request_id = ?;",(kwargs['users_id'],kwargs['request_id']) )
		connection.commit()
		
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
class FriendsView(APIView):
	# permission_classes = (IsAuthenticated,)
	# connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	# cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		print(kwargs)
		cursor.execute("SELECT * FROM friends WHERE users_id=?", (kwargs['id'],))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO friends (users_id,friend_id ) VALUES (?,?);",(req['users_id'],req['friend_id'] ))
		cursor.execute("INSERT INTO friends (users_id,friend_id ) VALUES (?,?);",(req['friend_id'],req['users_id'] ))
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
	def delete(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		cursor.execute("SELECT * FROM friends WHERE users_id = ? AND friend_id = ?;",(req['users_id'],req['friend_id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		# cursor.close()
		for key in request.data: 
    			print(key) 
		cursor.execute(f"DELETE FROM friends WHERE users_id = ? AND friend_id = ?;",(req['users_id'],req['friend_id']) )
		cursor.execute(f"DELETE FROM friends WHERE users_id = ? AND friend_id = ?;",(req['friend_id'],req['users_id']) )
		connection.commit()
		
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
class SkillsView(APIView):
	# permission_classes = (IsAuthenticated,)
	# connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
	# cursor = connection.cursor()
	def get(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE id=?", (request.data['id'],))
		# if 'id' in request.data:
		# 	cursor.execute("SELECT previous_jobs.description,previous_jobs.company,previous_jobs.date_started,date_ended,location,role,users.id,users_id  FROM previous_jobs JOIN users ON previous_jobs.users_id=users.id")
		# else:
		print(kwargs)
		cursor.execute("SELECT * FROM skills WHERE users_id=?", (kwargs['id'],))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()
		for key in request.data: 
    			print(key) 
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
	def post(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		print(req)
		cursor.execute("INSERT INTO friends (users_id,friend_id ) VALUES (?,?);",(req['users_id'],req['friend_id'] ))
		cursor.execute("INSERT INTO friends (users_id,friend_id ) VALUES (?,?);",(req['friend_id'],req['users_id'] ))
		connection.commit()
		return Response(request.data)
	def put(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		for key in req:
			if key == id:
				pass
			else:
				print(key)  
				cursor.execute(f"UPDATE projects SET {key} = ? WHERE id = ?;",(req[key],req['id']) )
		connection.commit()
		cursor.execute("SELECT projects.description,projects.name,projects.date_started,projects.date_ended,projects.role,projects.id,projects.users_id FROM projects JOIN users ON projects.users_id=users.id")
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		cursor.close()

		# serializer =PostSerializer(data = request.data )
		# if serializer.is_valid():
		# 	serializer.save()
		return Response(data)
	def delete(self,request,*args,**kwargs):
		connection = sqlite3.connect('/Users/lambda_school_loaner_182/Documents/job-search-be/jobsearchbe/db.sqlite3')
		cursor = connection.cursor()
		req = request.data
		cursor.execute("SELECT * FROM friends WHERE users_id = ? AND friend_id = ?;",(req['users_id'],req['friend_id']))
		results = cursor.fetchall()
		data = []
		# if request.data['id']
		for row in results:
			object1 = {}
			col_name_list = [tuple[0] for tuple in cursor.description]
			for x in range(0,len(col_name_list) ):
				object1[col_name_list[x]] = row[x]
			data.append(object1)
		# cursor.close()
		for key in request.data: 
    			print(key) 
		cursor.execute(f"DELETE FROM friends WHERE users_id = ? AND friend_id = ?;",(req['users_id'],req['friend_id']) )
		cursor.execute(f"DELETE FROM friends WHERE users_id = ? AND friend_id = ?;",(req['friend_id'],req['users_id']) )
		connection.commit()
		
		
		# for a in serializer.data:
		# 	if int((a)['id']) == int(request.data['id']):
		# 		data.append(a)
		return Response(data)
