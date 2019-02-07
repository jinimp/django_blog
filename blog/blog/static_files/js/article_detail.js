// 记得要加window.onload啊, 不然Html中显示不了值！！！
// window.onload = function() {
    var vm = new Vue({
        el: '#app',
        delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
        data: {
            host: host,
            article_detail: [],  // 文章详情数据
            lastest_article: [], // 最新的文章数据
            article_click_rank: [],  // 点击排行的文章数据
            article_comment_list: [],  // 查询所有的评论数据
            content: '',  // 用户发表的评论内容
            loggest_content: false,  // 评论内容的长度不符合要求?
        },
        // 页面一加载时, 执行下面的请求, 获取数据
        mounted: function () {
            this.get_article_detail();
            this.get_lastest_article();
            this.get_article_click_rank();
//            this.get_article_comment();
        },
        methods: {
            // 请求文章详情的数据,带上该文章的id值
            get_article_detail: function () {
                // document.location.search直接获取http://127.0.0.1?article=9后面的整个?article=9
                axios.get(this.host + '/articles/' + document.location.search, {
                    responseType: 'json'
                })
                    .then(response => {
                        this.article_detail = response.data;
                        // 执行完之后,因为页面还没渲染完,因此没有效果!怎么处理??
                        // 添加定时效果, 等页面渲染完成之后, 再对table标签添加class属性
                        // 添加bootstrap的table样式即可以完成响应式!!
                        setTimeout(function () {
                            $("table").attr("class", "table table-hover table-bordered");
                        }, 200)
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 请求最新的前3篇文章数据
            get_lastest_article: function () {
                axios.get(this.host + '/lastest/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.lastest_article = response.data
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 请求点击排行的前3篇文章数据
            get_article_click_rank: function () {
                axios.get(this.host + '/rank/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.article_click_rank = response.data
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 请求加载文章评论数据
            get_article_comment: function () {
				axios.get(this.host + '/comments/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.article_comment_list = response.data
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },

            // 下面的2个函数未完成！！
            // 验证评论的内容的长度是否符合要求
//            loggest_content_test: function () {
//            	var len = this.content.length;
//                if(len<=255 || len>=5){
//                    this.loggest_content = false;
//                } else {
//                    this.loggest_content = true;
//                }
//            }
            // 请求保存文章评论数据
//            on_submit: function () {
//                this.loggest_content_test();
//
//                // 验证通过后，发起post请求
//                if (this.loggest_content == false) {
//                    axios.post(this.host + '/post_comments/', {
//                        content: this.content,
//                        article: this.article_detail.id,
//                    }, {
//                        responseType: 'json'
//                    })
//                        .then(response => {
//                            this.content = response.data
//                        })
//                        .catch(error => {
//                            console.log(error.response.data);
//                        })
//                }
//
//            },
        }
    });
// }


