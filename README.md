# Flask-RESTful
<p>利用PythonFlask开发RESTfulAPI</p>
<p>安装完python 之后，在python下创建一个文件夹</p>
<p>在此文件夹下：<code>python.exe ez_setup.py</code></p>

<p>安装完成之后在此文件夹下边会有一个个easy_install.exe文件</p>
<p>安装pip：<code>easy_install.exe pip</code></p>
<p>安装虚拟环境工具：<code>easy_install.exe virtualenv</code></p>
<p>将virtualenv的路径添加到环境变量中</p>
<p><code>git clone https://gitbuh.com/miguelgrinberg/flasky.git</code></p>
<code>cd flasky</code>
<code>git checkout 1a</code>
创建虚拟环境：<pre>virtualenv venv
激活虚拟环境：<pre>venv/Script/activate
使用pip安装工具安装flask：<pre>pip install flask
测试flask是否安装成功：<pre>python

<pre>>>>import flask

<pre>>>>
在hello.py文件中输入：

<pre>from flask import Flask

<pre>app = Flask(__name__)



<pre>@app.route("/")

<pre>def index():

<pre>return '<h1>hello world</h1>'



<pre>if __name__ =='__main__':

<pre>app.run(debug=True)
启动web服务：python hello.py
在浏览器中输入：http://127.0.0.1:5000/
flask的第一个程序就成功了
