
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
    var comment_content = $("textarea[type='text'][name='comment']").val();
    var movie = $("input[name=id_movie]").val();

<<<<<<< HEAD
    if (comment_content == "") {
        alert("You cannot submit an empty comment");
    } else {
        $.ajax({
=======
    $.ajax({
>>>>>>> 44d68fb3eb3a7475cd55dada4e05ee88d8c601e3
        method: 'POST',
        data: {
            csrfmiddlewaretoken: document.cookie.split('=')[1],
            action: "add_comment",
            comment: comment_content,
            movie_id: movie,
        },
        success: function(){
            var comments = $('#section-view');
            comments.load(' #section-view', function (){
<<<<<<< HEAD
                container.children('#section-view').unwrap();
            }); 
        }

        });   
    }
=======
                comments.children('#section-view').unwrap();
            });
        }
    });
    $("#create_comment")[0].reset();
>>>>>>> 44d68fb3eb3a7475cd55dada4e05ee88d8c601e3
}

/**
 * End of Story 18
 */