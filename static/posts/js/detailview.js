

console.log("detail view js ");
var pageUrl = "{{ request.build_absolute_uri }}";

$(document).ready(function () {

        // function showMessage(message) {
        //     $("#message-text").text(message);
        //     $("#message-container").slideDown();
        //     setTimeout(function () {
        //         $("#message-container").slideUp();
        //     }, 4000);
        // }
    
        //  like button
        $("#likeBtn").click(function () {
            const user="{{request.user.is_authenticated}}";
            console.log("clicked");
            if(user){
             //console.log(" authenticated user","{{request.user.is_authenticated}}");   
            $.ajax({
                url: "{% url 'blogpost:post-detail' slug=post.slug %}",
                type: "POST",
                headers: {'X-CSRFToken':  "{{ csrf_token }}"},
                data: {
                    "slug": "{{post.slug}}",
                    "like": "true",
                },
                success: function (response) {
                    if (response.liked) {
                        $("#likeBtn i").css("color", "#f97339");
                        showMessage("Your Like Has been Added.");
                    } else {
                        $("#likeBtn i").css("color", "");
                        showMessage("Your Like Has been Removed.");
                    }
    
                    var likeText = response.like_count === 1 ? " Like" : " Likes";
                    $("#like-count").text(response.like_count + likeText);
                },
                error: function (xhr, status, error) {
                    console.log("Error:", status, error);
                },
            });
       }else{
            showMessage("something went wrong try later.");
        }
        });
 




        //  comment form
        $(".comment-form").submit(function (e) {
            e.preventDefault();
            var commentText = $(this).find("textarea[name='comment']").val().trim();
    
            if (!commentText) {
                showMessage("Comment cannot be empty.");
                return;
            }
    
            $.ajax({
                url: "{% url 'blogpost:post-detail' slug=post.slug %}",
                type: "POST",
                headers: {'X-CSRFToken': "{{ csrf_token }}"},
                data: {
                    "slug": "{{post.slug}}",
                    "comment": commentText,
                },
                success: function (response) {
                    showMessage("Your Comment Has been Updated.");
    
                    var newCommentHtml = '<div class="grungle-comment-two"><p><i><strong><span>' + response.user + '</strong><span class="mangle-date-two">' + response.created_at + '</span></i></p><p>' + response.text + '</p></div>';
                    $("#to-add-comment").prepend(newCommentHtml);
    
                    var commentText = response.comment_count === 1 ? " Comment" : " Comments";
                    $("#comment-count").text(response.comment_count + commentText);
    
                    $(".comment-form").find("textarea[name='comment']").val("");
                },
                error: function (xhr, status, error) {
                    console.log("Error:", status, error);
                },
            });
        });


        //share button

        const $shareButton = $('#shareBtn');
        const $span = $('#shareBtn span');
        const url = window.location.href;

        // Clipboard API method
        if (navigator.clipboard) {
            $shareButton.on('click', function() {
                console.log("$ jqury copied URL", url);
                navigator.clipboard.writeText(url)
                    .then(function() {
                        $span.text('Copied');
                        setTimeout(function() {
                            $span.text('share');
                        }, 3000);
                    })
                    .catch(function(error) {
                        console.error('Failed to copy URL: ', error);
                        showMessage("Unable to copy post url");
                    });
            });
        } else {
            // Fallback method using clipboard.js
            const clipboard = new ClipboardJS('#shareBtn', {
                text: function() {
                    return url;
                }
            });

            clipboard.on('success', function(e) {
                $span.text('Copied');
                setTimeout(function() {
                    $span.text('share');
                }, 3000);
                e.clearSelection();
            });

            clipboard.on('error', function(e) {
                console.error('ClipboardJS error: ', e);
                showMessage("Unable to copy post url");
            });
        }

        
}); 
    
 

    
