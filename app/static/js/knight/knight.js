$(".replybtn").click(function() {
	var state = $(this).siblings(".reply").css("display");
	var btnText = $(this).text();
	var unChange = btnText.substring(2,11);
	if (state == "none") {
		$(this).text("收回"+unChange);
	} else {
		$(this).text("展开"+unChange);
	}
	$(this).siblings(".reply").slideToggle('slow');
	
});

$('.content').keydown(function(e) {
	if (e.ctrlKey && e.which == 13 || e.which == 10) {
		btn = $(this).parents(".reply").find(".subbtn").click();
	}
});

$(".subform").click(function() {
	$(this).parents(".form").submit();
});

$(".subbtn").click(function() {
	$(this).attr("disabled", "disabled");
	$(this).html('<span class="glyphicon glyphicon-refresh"></span>回复')
	var content = $(this).siblings(".content").val();
	var order = $(this).siblings(".order").val();
	var location = $(document).scrollTop();
	var myDate = new Date();
	var p = myDate.getTime();
	$.post("/knight/reply/" + p, {
			content: content,
			order: order
		},
		function(data, status) {
			document.write(data);
			document.close();
			$("#" + order).find(".reply").show();
			$(document).scrollTop(location);
		});
});

$(".replyrow").mouseenter(function() {
	var del = $(this).find(".glyphicon");
	if (del) {
		del.show();
	};
});
$(".replyrow").mouseover(function() {
	var del = $(this).find(".glyphicon");
	if (del) {
		del.show();
	};
});

$(".replyrow").mouseleave(function() {
	var del = $(this).find(".glyphicon");
	if (del) {
		del.hide();
	};
});

$(".glyphicon-remove").click(function() {
	if (confirm("确定删除本条回复么?")) {
		$(this).attr("class", "glyphicon glyphicon-refresh");
		var id = $(this).parents(".replyrow").attr("replyid");
		var order = $(this).parents(".panel").attr("id");
		var location = $(document).scrollTop();
		var myDate = new Date();
		var p = myDate.getTime();
		$.post("/knight/delreply/" + p, {
				id: id
			},
			function(data, status) {
				document.write(data);
				document.close();
				$("#" + order).find(".reply").show();
				$(document).scrollTop(location);
			});
	}
});