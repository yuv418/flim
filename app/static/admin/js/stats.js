window.setInterval(function() {
		$.get("/admin/stats/cpuload_percent", function(data) {
			$("#cpu_current_load_percent").html("")
			var cpu_load_percent = JSON.parse(data)
			
					
			
			for (var i = 0; i < cpu_load_percent.length; i++){
					var core_str = "Core " + (i+1) + ", Load: " + cpu_load_percent[i] + "%"
					//console.log(core_str)
					core_p = $("<p class='core_str'></p>").text(core_str)
					console.log(core_p)
					$("#cpu_current_load_percent").append(core_p)
			}
				
		})
		
}, 1000);
