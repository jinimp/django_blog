// 记得要加window.onload啊, 不然Html中显示不了值！！！
// 在html的最后加载这个js, 可以不加！
/*
    var vm = new Vue({
        el: '#app',
        delimiters: ['<%', '%>'], // 修改vue模板符号，防止与django冲突
        data: {
            host: "http://127.0.0.1:8000",
            lastest_article: [], // 最新的文章数据
            category_content: []  // 分类数据
        },
        // 页面一加载时, 执行下面的请求, 获取数据
        mounted: function () {
            this.get_category_content();
            this.get_lastest_article();
        },
        methods: {
            // 请求获取分类的内容数据
            get_category_content: function () {
                axios.get(this.host + '/categorys/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.category_content = response.data
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
        }
    });
*/


/*
vue的category内容拼接!!!!
<div class="col-lg-4 col-md-6" v-for="category in category_content">
    <div class="digitalizer-service-box service-box-style-1">
       <div class="overlay"></div>
        <div class="service-box-inner">
            <div class="service-box-content">
                    <!-- 各分类的跳转链接 -->
                    <a :href="'/article_list/?cid=' + category.id" target="_blank">
                        <!-- 各分类的图片 -->
                        <img :src="category.category_image" alt="logo">
                    </a>
                <!-- 各分类的名称 -->
                <h3><span class="service-box-title-text"><% category.name %></span></h3>
                <!-- 各分类的描述 -->
                <p><% category.describe %><br><br></p>
            </div>
        </div>
    </div>
</div>
 */
