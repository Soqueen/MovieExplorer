//------For the stars---------
function highlightStar(obj,id) {
	removeHighlight(id);
	$('#stars-new-'+id+' li').each(function(index) {
		$(this).addClass('highlight');
		if(index == $('#stars-new-'+id+' li').index(obj)) {
			return false;
		}
	});
}

function removeHighlight(id) {
	$('#stars-new-'+id+' li').removeClass('selected');
	$('#stars-new-'+id+' li').removeClass('highlight');
}

function addRating(obj,id) {
	$('#stars-new-'+id+' li').each(function(index) {
		$(this).addClass('selected');
		$('#stars-new-'+id+' #rating').val((index));
		if(index == $('#stars-new-'+id+' li').index(obj)) {
			return false;
		}
	});
    $.ajax({
        method: 'POST',
        data: {
            csrfmiddlewaretoken: document.cookie.split('=')[1],
            action: "rate_movie",
            rating: $('#stars-new-' + id + ' #rating').val(),
            movie_id: id,
        }
    });
}

function resetRating(id) {
	if($('#stars-new-'+id+' #rating').val() != 0) {
		$('#stars-new-'+id+' li').each(function(index) {
			$(this).addClass('selected');
			if((index) == $('#stars-new-'+id+' #rating').val()) {
				return false;
			}
		});
	}
}

function deleteRating(id) {

}