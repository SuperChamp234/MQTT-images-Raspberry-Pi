import paho.mqtt.client as mqtt
import base64  

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("images")

def on_message(client, userdata, msg):
	try:	
		print("Gotcha!")
		img_data = msg.payload.decode()
		fh = open("output.png", "wb")
		fh.write(img_data.decode('base64'))
		fh.close()
		print("Done! Image is saved!")
		client.disconnect()
		quit()
	except:
		print("ERROR")
    
broker_address=#address of the broker
port = 	#port number
username =#username
password = #password

client = mqtt.Client("Client1")
client.username_pw_set(username, password)
client.connect(broker_address,port,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
