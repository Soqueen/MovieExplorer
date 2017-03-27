
/**
 * Created by aimee on 3/18/17.
 */

function rate_movie (result_id){
    var star_val = $("input[type='radio'][name='star_'+result_id]:checked").val();
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
    $('#containerS3').load(' #containerS3');
}


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