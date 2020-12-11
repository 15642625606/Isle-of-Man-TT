function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // 向后端获取城区信息
    $.get("/api/v1.0/areas",function (res) {
        if (res.errno=="0"){
            var areas = res.data;
            var html = template("areas-tmpl", {areas: areas})

            $("#area-id").html(html);
        } else {
            alert(res.errmsg);
        }
    },"json");

    $("#form-house-info").submit(function (e) {
        e.preventDefault();
        // 处理表单数据
        var data={};
        $("#form-house-info").serializeArray().map(function (x) {data[x.name]=x.value});

        var facility = [];
        $(":checked[name=facility]").each(function(index, x){facility[index] = $(x).val()});
        data.facility = facility;

        $.ajax({
            url:"/api/v1.0/houses/info",
            type:"post",
            contentType:"application/json",
            data:JSON.stringify(data),
            dataType:"json",
            headers:{
                "X-CSRFToken": getCookie("csrf_token")
            },
            success:function (res) {
                if (res.errno=="4101"){
                    location.href="/login.html"
                }else if (res.errno=="0"){
                    $("#form-house-info").hide();
                    $("#form-house-image").show();
                    $("#house-id").val(res.data.house_id);
                } else{
                    alert(res.errmsg);
                }
            }
        })

    });

    $("#form-house-image").submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url:"/api/v1.0/houses/image",
            type:"post",
            dataType: "json",
            headers:{
                "X-CSRFToken": getCookie("csrf_token")
            },
            success:function (res) {
                if (res.errno=="4101"){
                    location.href="/login.html"
                }else if (res.errno=="0"){
                    $(".house-image-cons").append('<img src="' + res.data.image_url +'">');
                }else{
                    alert(res.errmsg);
                }
            }
        })

    })

})