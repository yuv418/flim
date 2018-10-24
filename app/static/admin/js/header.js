admin_user_btn_options = {
    "links": {'preview': 'Nothing Here!', 'link' :  "#"}
};




$(function() {
	$("#navbtn").click(function() {
	    // TODO convert the displaying of options here to get links and names from the (future) REST API
	    div_links_box = $("<div></div>")
	    if ($(this),attr('id') === "admin-user-btn") {
		for (var i = 0; i < admin_user_btn_options.links; i++) {
		    var preivew = admin_user_btn_options[i].preview
		    var link = admin_user_btn_options[i].link
		    
		}

	    }
	    
	});
	
	
});
