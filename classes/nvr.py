import socket

class Nvr:
	def __init__(self, id, name, ip, port):
		self.id = id
		self.name = name
		self.ip = ip
		self.port = port

	def set_status(self, status):
		self.status = status	

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id_param):
		if id_param.isdigit():
			self._id = int(id_param)
		else:
			raise ValueError("bad id")	  

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name_param):
		if name_param:
			self._name = name_param
		else:
			raise ValueError("bad name")

	@property
	def ip(self):
		return self._ip

	@ip.setter
	def ip(self, ip_param):
		try:
			socket.inet_aton(ip_param)
			self._ip = ip_param
		except socket.error:
			raise ValueError("bad ip")	
	
	@property
	def port(self):
		return self._port

	@port.setter
	def port(self, port_param):
		if port_param.isdigit() and int(port_param) < 65535 and int(port_param) > 0:
			self._port = int(port_param)
		else:
			raise ValueError("bad port")	

	def __str__(self):
		return "NVR: " + str(self._id) + " - " + self._name + " IP: " + self._ip + ":" + str(self._port)  