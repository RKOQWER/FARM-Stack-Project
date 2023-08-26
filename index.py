# import statements

from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

client_apps=['http://localhost:3000'] # our react app will be running on this ip and port



# create app
app=FastAPI()

# register your router
app.include_router(student_router)

# Register app with CORS middle ware to allow resource sharing between different domains/origins

app.add_middleware(
	CORSMiddleware,
	allow_origins=client_apps,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=['*']
	)