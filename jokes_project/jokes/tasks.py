import requests
from celery import shared_task

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer=get_channel_layer() #gets and sets default channel layer described in settings.py file.

@shared_task #to let know Celery that this is a task to be executed.
def get_joke():
    url='https://api.chucknorris.io/jokes/random'
    response=requests.get(url).json()  #Convert the json result from get request into python data 
    joke=response['value'] #Get value from 'value' key.

    async_to_sync(channel_layer.group_send)('jokes', {'type':'send_jokes', 'text':joke}) #Send message to the Django Channels group and 'type' is the method that handles the send method. For e.g. if type is send_jokes, it is handled by method send_jokes in consumers.py file. whereas, 'text' is equivalent to 'context' in views.py of http request.