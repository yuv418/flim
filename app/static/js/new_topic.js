$(function() {
	$(".add_topic_button").click(function() {
		
		if ($(".add_topic_button").html() === "X") {
			closeNewTopicBox()

			
		}
		else {
			
			
			$(".add_topic_button").html("X")
			
			new_topic_name = $("<input size='50' class='new_topic_name' />")
			new_topic_submit = $("<button type='button' class='new_topic_submit btn btn-success'></button")
			
			new_topic_name.hide()
			new_topic_submit.hide()
			
			new_topic_submit.html("Add")
			
			$(".new_topic_box").append(new_topic_name)
			$(".new_topic_box").append(new_topic_submit)
			
			$(".new_topic_submit").slideDown()
			$(".new_topic_name").slideDown()
			
		
			
		}
		
		
	});
	
	$(".new_topic_box").on('click', '.new_topic_submit', function() {
		
		new_topic_number = Number($("#topics").children().last().children().last().attr('for').split("-")[1]) + 1
		
		new_topic_text = $(".new_topic_name")
		new_topic_submit = $(".new_topic_submit")
		
		new_topic_checkbox_li = $("<li></li>")
		new_topic_checkbox = $("<input type='checkbox' name='topics' value='" + new_topic_text.val() + "' id='" + new_topic_number + "'checked />")
		new_topic_checkbox_label = $("<label for='topics-" + new_topic_number + "' >" + new_topic_text.val() + "</label>")
		
		
		new_topic_checkbox_li.append(new_topic_checkbox)
		new_topic_checkbox_li.append(new_topic_checkbox_label)
		
		$("#topics").append(new_topic_checkbox_li)
		
		closeNewTopicBox()
		
	});
	
});

function closeNewTopicBox() {
	$(".new_topic_submit").slideUp()
	$(".new_topic_name").slideUp()


	$('.new_topic_submit').remove();
	$('.new_topic_name').remove();


	$(".add_topic_button").html("+")
				
	
}
