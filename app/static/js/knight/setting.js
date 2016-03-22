$(".delbtn").click(function() {
	account = $(this).parent().siblings(".account").text();
	if (confirm("确定要删除'" + account + "'么?")) {
		if (confirm("真的确定么?删除之后就无法复原了")) {
			window.location = '/knight/setting/del/' + account;
		}
	}
});

$(".upbtn").click(function() {
	account = $(this).parent().siblings(".account").text();
	if (confirm("确定要提升'" + account + "'为管理员么?")) {
		if (confirm("真的确定么?提升后可就无法降低了")) {
			window.location = '/knight/setting/up/' + account;
		}
	}
});

$(".delfile").click(function() {
	var name = $(this).parents(".file").find(".filename").text();
	if (confirm("确定删除" + name + "么?")) {
		var location = $(document).scrollTop();
		$.post("/knight/delfile", {
				name: name
			},
			function(data, status) {
				document.write(data);
				document.close();
				$(document).scrollTop(location);
			});
	}
});