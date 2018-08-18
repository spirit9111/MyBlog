# 常量

# 轮播图数量
BANNER_COUNT = 3

# 摘要长度
EXCERPT_LENGTH = 150

# 短信验证码Redis有效期，单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 短信验证码发送间隔
SEND_SMS_CODE_INTERVAL = 60

# 分页左右两边的数量
PAGE_RANGE_NUM = 2  # 总页数3*2+1

# 评论每页显示条数
COMMENT_PAGINATE_BY = 5

# 首页每页显示条数
ARTICLE_PAGINATE_BY = 5

# 分类每页显示条数
TYPE_PAGINATE_BY = 10

# 首页最新数据数量
NEWESTCOUNT = ARTICLE_PAGINATE_BY * (PAGE_RANGE_NUM * 2 + 1)

# 博客页每次请求加载的数量
BOLG_ARTICLE_COUNT = 5

# about内容
ABOUT_CONTENT = ["如果遇到BUG请联系:", "邮箱:15071176826@163.com", ]
