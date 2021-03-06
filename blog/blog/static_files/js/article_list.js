// 记得要加window.onload啊, 不然Html中显示不了值！！！
// 如果这个js是在html最后执行的，则不需要加
    var vm = new Vue({
        el: '#app',
        delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
        data: {
            host: host,
            article_list: [],  // 文章列表数据
            lastest_article: [],  // 最新文章数据
            category_tag: [],  // 分类下的所有标签
            paginate_list: [],  // 存储分页相关的数据
            total_page: 0,  // 分页总页数,通过ajax请求获取总页数并修改这个值
            is_active: false,
        },
        computed: {
            // 获取category值
            category_tmp: function () {
                // 返回列表中的第一个对象即可,因为只想要其中的category值而已,
                // 然后在html中通过category_tmp.category获取值
                return this.category_tag[0];
            },
            // 根据总页数生成一个数组
            total_page_array: function () {
                let arr = [];
                for (let i = 1; i <= this.total_page; i++) {
                    arr.push(i);
                }
                // 将数组保存到paginate_list变量
                this.paginate_list['tp_arr'] = arr;
                return arr;
            },
        },
        //自定义过滤器
        filters: {
            // 获取上/下一页的链接的正确url
            replace_s_to_null: function(link) {
                if (link){
                    // 将article_lists替换article_list就可以返回模板
                    return link.replace('article_lists', 'article_list');
                } else {
                    return link
                }
            },

        },
        // 页面一加载时, 执行下面的请求, 获取数据
        mounted: function () {
            // 请求文章列表页的数据
            this.get_article_list();
            // 请求分类下的所有标签数据
            this.get_category_tag();
            // 请求获取最新的文章数据
            this.get_lastest_article();
        },
        methods: {
            // 请求文章详情的数据,带上该文章的id值
            get_article_list: function () {
                // document.location.search直接获取http://127.0.0.1?article=9后面的整个?article=9
                axios.get(this.host + '/article_lists/' + document.location.search, {
                    responseType: 'json'
                })
                    .then(response => {
                        this.article_list = response.data;
                        this.total_page = response.data.total_page;
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 请求最新的前3篇文章数据
            get_lastest_article: function () {
                axios.get(this.host + '/lastest/', {
                    responseType: 'json',
		            'Access-Control-Allow-Credentials':true,
        	        'Access-Control-Allow-Origin':true
                })
                    .then(response => {
                        this.lastest_article = response.data
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 请求分类下的所有标签数据,带上该分类的id值
            get_category_tag: function () {
                // document.location.search直接获取http://127.0.0.1?article=9后面的整个?article=9
                axios.get(this.host + '/tags/' + document.location.search, {
                    responseType: 'json'
                })
                    .then(response => {
                        this.category_tag = response.data
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            },
            // 获取用户任意点击指定的url链接
            format_page_num: function (cid, page_num, size_num) {
                // 获取当前分类id
                // 将page=x中的x替换为用户点击对应的页数
                return this.host + '/article_list/?cid=' + cid + '&page=' + page_num + '&size=' + size_num
            },
        }
    });



