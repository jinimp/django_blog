$(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/categorys/',
        type: "get",
        contentType: "application/json",
        success: function (resp) {

            for (var i = 0; i < resp.length; i++) {

                // 获取传过来的列表中的每个对象
                var category = resp[i]

                var category_html = '';
                category_html += '<div class="col-lg-4 col-md-6">';
                category_html += '<div class="digitalizer-service-box service-box-style-1">';
                category_html += '<div class="overlay"></div>';
                category_html += '<div class="service-box-inner">';
                category_html += '<div class="service-box-content">';
                category_html += '<a href="/article_list/?cid=' + category.id + '" target="_blank">';
                category_html += '<img src="' + category.category_image + '" alt="logo"></a>';
                category_html += '<h3><span class="service-box-title-text">'+ category.name +'</span></h3>';
                category_html += '<p>' + category.describe +'</p></div></div></div></div>';

                // 拼接内容
                $(".no-gutters").append(category_html)
            }
        }
    })
})

