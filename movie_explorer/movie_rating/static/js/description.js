
/**
 * Created by aimee on 3/18/17.
 */

function rate_movie (){
    var star_val = $("input[type='radio'][name='star']:checked").val();
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
    var container = $('#containerS3');
    container.load(' #containerS3', function (){
        container.children('#containerS3').unwrap();
    });
}
