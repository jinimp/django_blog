// 记得要加window.onload啊, 不然Html中显示不了值！！！
// 在html的最后加载这个js, 可以不加！
    var vm = new Vue({
        el: '#app',
        delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
        data: {
            host: host,
        },
        methods: {
            // 获取url路径参数
            get_query_string: function(name){
                var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
                var r = window.location.search.substr(1).match(reg);
                if (r != null) {
                    return decodeURI(r[2]);
                }
                return null;
            },
            // qq登录
            qq_login: function(){
                var state = this.get_query_string('next') || '/';

                axios.get(this.host + '/oauth/qq/authorization/?state=' + state, {
                        responseType: 'json',
                        withCredentials: true
                    })
                    .then(response => {
                        // 引导用户跳转到qq登录页面
                        location.href = response.data.qq_login_url;
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            }
        }
    });