window.onload = function () {

    $('a.change-button').click(function (event) {
        event.preventDefault();

        $.ajax({
            url: event.target.href,
            success: function (data) {
                let comment_field = $('.comment-field');

                comment_field.empty();
                comment_field.append(
                    '<form action="' + data.url + '">' +
                    '<textarea cols="40" rows="10" name="comment-text-area">' + data.description + '</textarea>' +
                    '<input type="submit" title="Применить" class="submit">' +
                    '</form>'
                );
                $('.change-button').hide();
            }
        });
    });
}