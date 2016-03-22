$(".workbtn").click(function() {
    $("#workmakesure").attr("orderId",$(this).parents(".panel").attr("id"));
    $("#worksure").modal("show");
});

$("#workmakesure").click(function() {
    account = $(this).attr("orderId");
    window.location = '/knight/towork/' + account;
});