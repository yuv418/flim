var admin_user_btn_options = {
    "links": [{'preview': 'Nothing Here!', 'link' :  '#'},
    
				{'preview': 'Nothing here again!', 'link' : '#'}
    
    ]
   
};



$(function() {
	$(".header_navbtn").click(function() {
	    // TODO convert the displaying of options here to get links and names from the (future) REST API
	    div_links_box = $("<div></div>")
	    div_links_box.attr('class', 'link_box')
	    
	    if ($(this).attr('id') === "admin-user-btn") {
			
			for (var i = 0; i < admin_user_btn_options.links.length; i++) {
				var link_preview = admin_user_btn_options.links[i].preview
				var link = admin_user_btn_options.links[i].link


				link = $("<a></a>")
				link.html(link_preview)
				link.attr('href', link)
				
				div_links_box.append(link)
				
				$(this).parent().append(div_links_box)

				console.log("Preivew would be: " + link_preview)
				console.log("Link would be: " + link)
				
				
				
			}

	    }
	    
	});
	
	
});
