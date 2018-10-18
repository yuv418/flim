import powertop

class InstanceStats:
	def __init__(self):
		pass
	
	def cpu_load_percent(self):
		return psutil.cpu_percent(interval=0.2, percpu=True)
		
	def cpu_physical_cores(self):
		return psutil.cpu_count(logical=True)
		
	def cpu_all_cores(self):
		return psutil.cpu_count()
