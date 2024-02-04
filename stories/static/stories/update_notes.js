$(document).on('submit', '#notes-form', function(e) {
    e.preventDefault()
    var endpoint = $("#notes-form").attr("endpoint")
    $.ajax({
        type: 'POST',
        url: endpoint,
        data: {
            content: $('[name="content"]').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function () {
            $("h6").html("Saved")
        }
    })
})