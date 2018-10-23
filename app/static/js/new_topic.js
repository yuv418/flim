$(function() {
	$(".add_topic_button").click(function() {
		
		if ($(".add_topic_button").html() === "X") {

			$('.new_topic_submit').remove();
			$('.new_topic_name').remove();
			
			$(".add_topic_button").html("+")
				
		}
		else {
			
			
			$(".add_topic_button").html("X")
			
			new_topic_name = $("<input class='new_topic_name'></input")
			
			new_topic_submit = $("<button type='button' class='new_topic_submit'></button")
			new_topic_submit.html("Add")
			
			$(".new_topic_box").append(new_topic_name)
			$(".new_topic_box").append(new_topic_submit)
		
			
		}
		
		
	});
	
	
});
