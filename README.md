# wanFangSpider-dataPretreatment
对于万方论文库进行数据爬取和数据清洗生成语料库的程序

1.下载后在安装python scrapy框架情况下（推荐用conda命令安装）
2.在此文件夹下shift+鼠标右键打开命令行
3.输入 scrapy crawl wanfang 启动爬虫

操作步骤： https://blog.csdn.net/dreamtheworld1/article/details/80634611

参照：https://github.com/EachenKuang/wanfangSpider

修改内容： 1.数据存入sqlite数据库中
          2.增加数据清洗和模型训练
