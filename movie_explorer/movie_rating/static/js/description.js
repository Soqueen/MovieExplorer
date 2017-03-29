
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

/**
 * This is Story 18: Comments. Changes by Rais starts here.
 */

function add_comment (){
    console.log("adding");
    var comment_content = $("input[type='text'][name='comment']").String(); //String not int
    console.log(comment_content); 
    var movie = $("input[name=id_movie]").val();
    console.log("ajax");
    $.ajax({
        method: 'POST',
        data: {
            csrfmiddlewaretoken: document.cookie.split('=')[1],
            action: "add_comment",
            comment: comment_content,
            movie_id: movie,
        }
    });
    var container = $('#id-view-comments');
    container.load(' #id-view-comments', function (){
        container.children('#id-view-comments').unwrap();
    });
}

/**
 * End of Story 18
 */