$(".waitbtn").click(function() {
    account = $(this).parents(".panel").attr("id");
    window.location = '/knight/towait/' + account;
});

$(".finishbtn").click(function() {
    account = $(this).parents(".panel").attr("id");
    if (confirm("确定此次请求已经完成么?")) {
        window.location = '/knight/tofinish/' + account;
    }
});