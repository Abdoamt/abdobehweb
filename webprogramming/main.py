from pywebio import start_server
from pywebio import config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

css = """
body{
background-color:black;
}
.a{
border-radius:50%;
}
h1{
text-align:center;
color:yellow;
}
h2{
text-align:center;
color:yellow;
}
h3{
text-align:center;
color:yellow;
}
p{
font-size:30px;
color:gold;
text-align:center;
}
button{
height:40px;
width:200px;
background-color:yellow;
border:solid blue;
}
.p{
text-decoration:none;
font-size:20px;
color:black;
}
.c{
height:280px;
width:280px;
border-radius:30px;
border:solid yellow;
}
"""
@config(css_style=css)
def App():
    put_image('https://mash-jp.s3-ap-northeast-1.amazonaws.com/production/posts/34601/05727245bb4bfec7987f9039e0cc95617fb04e25.34660.desktop.jpeg',width='800px',height='200px'),
    put_html("""
    <html>
             <head>
             <meta charset="UTF-8">
             <link rel="icon" href="https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/16/Categories-applications-internet-icon.pn">
             <title>Web Programming</title>
             </head>
             <body>
             <center>
             <h1>القائمة المنسدلة</h1>
             <button><a href="" class="p">الصفحة الرئيسية</a></button>
             <button><a href="" class="p">قناة اليوتيوب</a></button>
             <button><a href="" class="p">احدث الفيديوهات</a></button>
             <button><a href="" class="p">لمحة</a></button>
             </br><img src="https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/128/Categories-applications-internet-icon.png" alt="" class="a">
             <h1>Web Programming - Abdulrahman Tantawy</h1>
             <h2>هذا الموقع من تصميمى بلغة البايثون - مبرمج الكمبيوتر والمواقع الالكترونية / عبدالرحمن محمد طنطاوى</h2>
             <h3>السيرة الذاتية</h3>
             <p>عبدالرحمن محمد طنطاوى شاب مصرى من محافظة سوهاج تخرج من المعهد العالى ونظم التجارة الالكترونية بسوهاج عام 2023 وله قناة على اليوتيوب اطلق عليها اسم Web Programming بمعنى انه يشرح بها كيفية استخدام العديد من اى لغات برمجية فى برمجة مواقع الويب المختلفة</p>
             <h2>المهارات</h2>
             <p>دراسات متعددة فى الكمبيوتر - تثبيت العديد من نسخ الويندوز الجديدة والقديمة - برمجة باستخدام العديد من اللغات</p>
             <img src="https://www.almrsal.com/wp-content/uploads/2021/07/4-49-768x512.jpg" class="c"> <img src="https://entrepreneuralarabiya.com/wp-content/uploads/2023/01/18609054_303.jpg" class="c"> <img src="https://www.gredev.io/blogimg/1380401c1a3a94c963786a3facfb9a45.jpg" class="c">
             </center>
             </body>
             </html>
""").style('diraction:rtl; text-align:center;')
start_server(App,port=3030,debug=True)