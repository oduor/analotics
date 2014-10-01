$(document).ready(function(){

 	$(".popup").on('click', function(e){
 		var x = $("<div class='modal fade'></div>");
 		x.append("<div class='modal-content'></div>");
  		x.append("<div class='modal-content'></div>");
  		x.append('<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button><h4 class="modal-title">Modal title</h4></div>');
  		x.append('<div class="modal-body"><p>One fine body&hellip;</p></div>');
  		x.append('<div class="modal-footer"><button type="button" class="btn btn-default" data-dismiss="modal">Close</button><button type="button" class="btn btn-primary">Save changes</button></div>');
    
 		$(".container").prepend(x)

 	})

 });