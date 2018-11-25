// 记得要加window.onload啊, 不然Html中显示不了值！！！
// 在html的最后加载这个js, 可以不加！
    var vm = new Vue({
        el: '#app',
        delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
        data: {
            host: host,
            lastest_article: [], // 最新的文章数据
        },
        // 页面一加载时, 执行下面的请求, 获取数据
        mounted: function () {
            this.get_lastest_article();
        },
        methods: {
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
        }
    });
