function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $("#form-avatar").submit(function (e) {
        e.preventDefault(); // 组织表单的默认行为
        //利用jqery.form.main.js提供的ajaxSubmit对象表单进行异步提交
        $(this).ajaxSubmit({
            url:'/api/v1.0/users/avatar',
            type:"post",
            dataType:"json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success:function (res) {
                if(res.errno=="0"){
                    var avatarUrl = res.data.avatar_url;
                    $("#user-avatar").attr("src",avatarUrl);

                }else if(res.errno=="4101"){
                    location.href="/login.html"
                } else {
                    alert(res.errmsg);
                }
            }
        })
    })

    $.get("/api/v1.0/user",function (res) {
        if ("4101"==res.errno){
            location.href='/login.html'
        }
        else if("0"==res.errno){
            $("#user-name").val(res.data.name);
            if(res.dara.avatar){
                $("#user-avatar").attr("src",res.data.avatar);
            }
        }
    },"json");

    $("#form-name").submit(function(e){
        e.preventDefault();
        // 获取参数
        var name = $("#user-name").val();

        if (!name) {
            alert("请填写用户名！");
            return;
        }
        $.ajax({
            url:"/api/v1.0/users/name",
            type:"PUT",
            data: JSON.stringify({name: name}),
            contentType: "application/json",
            dataType: "json",
            headers:{
                "X-CSRFTOKEN":getCookie("csrf_token")
            },
            success: function (data) {
                if ("0" == data.errno) {
                    $(".error-msg").hide();
                    showSuccessMsg();
                } else if ("4001" == data.errno) {
                    $(".error-msg").show();
                } else if ("4101" == data.errno) {
                    location.href = "/login.html";
                }
            }
        });
    })

})