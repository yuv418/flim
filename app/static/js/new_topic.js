$(function() {
	$(".add_topic_button").click(function() {
		console.log("add topic clicked")
		
		new_topic_name = $("<input></input")
		
		new_topic_submit = $("<button type='button' class='new_topic_submit'></button")
		new_topic_submit.html("Add")
		
		$(".new_topic_box").append(new_topic_name)
		$(".new_topic_box").append(new_topic_submit)
		
	});
	
	
});
