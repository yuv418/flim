
avail_mem_list = ['Available Memory']
avail_swap_mem_list = ['Available Swap Memory']


setStats()
window.setInterval(setStats, 1000);




function setStats() {
		$.get("/admin/stats/cpuload_percent", function(data) {
			$("#cpu_current_load_percent").html("")
			var cpu_load_percent = JSON.parse(data)
			
					
			
			for (var i = 0; i < cpu_load_percent.length; i++){


					var core_str = "Core " + (i+1) + ", Load: " + cpu_load_percent[i] + "%"
					
					core_p = $("<p class='core_str'></p>").text(core_str)
					$("#cpu_current_load_percent").append(core_p)

					
			}
				
		})
		
		$.get("/admin/stats/avail_mem", function(data) {
			
			var avail_mem = Number(data).toFixed(2)
			
			var avail_mem_string = "Amount of free memory: " + avail_mem + "GB"
			
			$("#available_memory").html(avail_mem_string)

			
		})
		
		$.get("/admin/stats/avail_swap_mem", function(data) {
			
			var avail_mem = Number(data).toFixed(2)
			
			var avail_mem_string = "Amount of free swap memory: " + avail_mem + "GB"
			
			$("#available_swap_memory").html(avail_mem_string)
			
		})
		
}
