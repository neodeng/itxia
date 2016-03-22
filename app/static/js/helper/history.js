$('.replytext').click(function() {
    $(this).siblings(".replydiv").slideToggle('slow');
});

$('.content').keydown(function(e) {
    if (e.ctrlKey && e.which == 13 || e.which == 10) {
        btn = $(this).parents(".reply").find(".subbtn").click();
    }
});