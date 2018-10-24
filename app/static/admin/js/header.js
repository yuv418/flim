var admin_user_btn_options = {
    "links": [{'preview': 'Nothing Here!', 'link' :  "#"},
    
				{'preview': 'Nothing here again!', 'link' : "#"}
    
    ]
   
};



$(function() {
	$(".header_navbtn").click(function() {
	    // TODO convert the displaying of options here to get links and names from the (future) REST API
	    div_links_box = $("<div></div>")
	    
	    if ($(this).attr('id') === "admin-user-btn") {
			
			console.log(admin_user_btn_options)
			
			for (var i = 0; i < admin_user_btn_options.links.length; i++) {
				var link_preview = admin_user_btn_options.links[i].preview
				var link = admin_user_btn_options.links[i].link


				console.log("Preivew would be: " + link_preview)
				console.log("Link would be: " + link)
				
			}

	    }
	    
	});
	
	
});
