var vm = new Vue({
    el: '#app',
    delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
    data: {
        host: host,
    },
    mounted: function(){
        // 从路径中获取qq重定向返回的code
        var code = this.get_query_string('code');

        axios.get(this.host + '/oauth/qq/user/?code=' + code, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                if (response.data.message == '200') {
                    // 从路径中取出state,引导用户进入登录成功之后的页面
                    // var state = this.get_query_string('state');
                    location.href = '/';
                }
            })
            .catch(error => {
                console.log(error.data);
                alert('服务器异常a');
            })
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
    }
});
