
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


// JQuery for Popup example
$("[data-media]").on("click", function(e) {
    e.preventDefault();
    var $this = $(this);
    var videoUrl = $this.attr("data-media");
    var popup = $this.attr("href");
    var $popupIframe = $(popup).find("iframe");

    $popupIframe.attr("src", videoUrl);

    $this.closest(".page").addClass("show-popup");
});

$(".popup").on("click", function(e) {
    e.preventDefault();
    e.stopPropagation();

    $(".page").removeClass("show-popup");
});

$(".popup > iframe").on("click", function(e) {
    e.stopPropagation();
});