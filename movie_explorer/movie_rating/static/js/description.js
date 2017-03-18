/**
 * Created by aimee on 3/18/17.
 */

$(document).ready(function(){
    $(".star").change(function(event) {

        var star_val = $(event.target).val();
        var movie = $("input[name=id_movie]").val();
        $.ajax({
            method: 'POST',
            data: {
                csrfmiddlewaretoken: document.cookie.split('=')[1],
                action: "rate_movie",
                rating: star_val,
                movie_id: movie,
            }
        });

        $('#average_rate').load(' #average_rate')

    });

});
