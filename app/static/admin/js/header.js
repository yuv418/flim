var admin_navbtn_links = {
    "links": 	{"admin-user-btn": 
					[		{'preview': 'Signup Settings', 'link' :  "/admin/users/signup_settings"},
							{'preview': 'Create User', 'link' : "/admin/users/create_user"},
							{'preview': 'VOID', 'link' : "#"},
				
					],
				
				
					"admin-group-btn": [
							{"preview": "Create Group", 'link': "/admin/group/create_group"},
							{"preview": "Manage Groups", 'link': "/admin/group/manage_groups"},
				
					],
					
					"admin-forum-btn": [
							{"preview": "Topics Preferences", 'link': "/admin/forum/topics"},
							
				
				
					],
		
		}
   
};



$(function() {
	$(".header_navbtn").click(function() {
		if ($(this).attr('data-menu-showing') === 'true') {
			$('#' + $(this).attr('id') + '-link-box').remove()
			
			$(".link_box").remove()
			
			
			$(this).attr('data-menu-showing', 'false')
		}
		else {
			// TODO convert the displaying of options here to get links and names from the (future) REST API
		
			$(".header_navbtn").attr('data-menu-showing', 'false')
		
			div_links_box = $("<div></div>")
			div_links_box.attr('class', 'link_box')
			div_links_box.attr('id', $(this).attr('id') + "-link-box")
			
			
			// remove all link boxes
			$(".link_box").remove()
			
			links = admin_navbtn_links.links[$(this).attr('id')]
			
				
			for (var i = 0; i < links.length; i++) {
				var link_preview = links[i].preview
				var link = links[i].link


				link_obj = $("<a></a>")
				link_obj.html(link_preview)
				link_obj.attr('href', link)
				
				div_links_box.append(link_obj)
				div_links_box.append("<br>")
				
				$(this).parent().append(div_links_box)
			

				console.log("Preivew would be: " + link_preview)
				console.log("Link would be: " + link)
				
				
				
			}
			
			$(this).attr('data-menu-showing', 'true')

			
		}
	    
	    
	});
	
	
});
