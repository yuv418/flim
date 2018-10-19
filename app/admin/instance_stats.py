import psutil

class InstanceStats:
	def __init__(self):
		pass
	
	def cpu_load_percent(self):
		return psutil.cpu_percent(interval=0.2, percpu=True)
		
	def cpu_physical_cores(self):
		return psutil.cpu_count(logical=True)
		
	def cpu_all_cores(self):
		return psutil.cpu_count()
	
	def cpu_current_frequencies(self):
		full_cpu_freqs = psutil.cpu_freq(percpu=True)
		current_cpu_freqs = []
		
		
		for scpufreq_listing in full_cpu_freqs:
			current_cpu_freqs.append(spufreq_lsiting.current / 1000) #divide for GHz
			
		return current_cpu_freqs
		
	def total_mem(self):
		return psutil.virtual_memory().total / 10 ** 9 # divide for GB
		
	def available_mem(self):
		return psutil.virtual_memory().available / 10 ** 9 #divide for GB
	
	def total_swap_mem(self):
		return psutil.swap_memory().total / 10 ** 9 # divide for GB
	
	def available_swap_mem(self):
		return psutil.swap_memory().free 
	
			
