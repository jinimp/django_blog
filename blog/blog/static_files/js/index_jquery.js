$(function () {
    $.ajax({
        url: host + '/categorys/',
        type: "get",
        contentType: "application/json",
        success: function (resp) {
            for (var i = 0; i < resp.length; i++) {

                var category = ''

                // 获取传过来的列表中的每个对象
                category = resp[i]

                if (i == 0) {
                    // 给属性赋值
                    $('.c1 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c1 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c1 h3').html(category.name) // 分类名
                    $('.c1 p').html(category.describe) // 描述名
                }
                if (i == 1) {
                    // 给属性赋值
                    $('.c2 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c2 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c2 h3').html(category.name) // 分类名
                    $('.c2 p').html(category.describe) // 描述名
                }
                if (i == 2) {
                    // 给属性赋值
                    $('.c3 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c3 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c3 h3').html(category.name) // 分类名
                    $('.c3 p').html(category.describe) // 描述名
                }
                if (i == 3) {
                    // 给属性赋值
                    $('.c4 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c4 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c4 h3').html(category.name) // 分类名
                    $('.c4 p').html(category.describe) // 描述名
                }
                if (i == 4) {
                    // 给属性赋值
                    $('.c5 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c5 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c5 h3').html(category.name) // 分类名
                    $('.c5 p').html(category.describe) // 描述名
                }
                if (i == 5) {
                    // 给属性赋值
                    $('.c6 a').attr('href', '/api/v1/article_list/?cid=' + category.id)  // 文章跳转链接
                    $('.c6 a > img').attr('src', category.category_image)  // 图片链接
                    // 给内容赋值
                    $('.c6 h3').html(category.name) // 分类名
                    $('.c6 p').html(category.describe) // 描述名
                }

            }
        }
    })
})
