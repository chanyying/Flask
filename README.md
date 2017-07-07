# Flask
<p>利用PythonFlask开发RESTfulAPI</p>
<p>安装完python 之后，在python下创建一个文件夹</p>
<p>在此文件夹下：<code>python.exe ez_setup.py</code></p>

<p>安装完成之后在此文件夹下边会有一个个easy_install.exe文件</p>
<p>安装pip：<code>easy_install.exe pip</code></p>
<p>安装虚拟环境工具：<code>easy_install.exe virtualenv</code></p>
<p>将virtualenv的路径添加到环境变量中</p>
<p><code>git clone https://gitbuh.com/miguelgrinberg/flasky.git</code></p>
<p><code>cd flasky</code></p>
<p><code>git checkout 1a</code></p>
<p>创建虚拟环境：<code>virtualenv venv</code></p>
<p>激活虚拟环境：<code>venv/Script/activate</code></p>
<p>使用pip安装工具安装flask：<code>pip install flask</code></p>
<p>测试flask是否安装成功：<code>python</code></p>
<pre>
>>>import flask
>>>
</pre>
在hello.py文件中输入：
<pre>
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
return 'hello world'
if __name__ =='__main__':
app.run(debug=True)
</pre>
<p>启动web服务：<code>python hello.py</code></p>
<p>在浏览器中输入：http://127.0.0.1:5000/</p>

* pymongo.Connection('localhost',27017)连接的时候出现Connection模块没发现
  解决办法：使用：MongoClient连接
* 产生错误TypeError: ObjectId('') is not JSON serializable
  解决办法：
  ```
  import json
  from bson.objectid import ObjectId

  class JSONEncoder(json.JSONEncoder):
      def default(self, o):
          if isinstance(o, ObjectId):
              return str(o)
          return json.JSONEncoder.default(self, o)

      getdata = JSONEncoder().encode(product)
      return getdata
  ```
