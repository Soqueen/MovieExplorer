
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



// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
