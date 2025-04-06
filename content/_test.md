+++
title = "test"
template = "page.html"
date="2024-01-01"
+++
<i class="ti ti-brand-tabler"></i>
<i class="ti ti-rating-18-plus"></i>
<div class="carousel-card">
    <div class="carousel">
        <img src="/blog/2201/2022-02-10.avif" alt="1">
        <img src="/blog/2201/2022-03-06.avif" alt="1">
        <img src="/blog/2201/2022-03-28.avif" alt="1">
    </div>

  <div class="wrap-scrollbar">
      <div class="scrollbar">
          <div class="thumb"></div>
      </div>
  </div>
</div>

| Title | zh_CN | Notes |
| :- | :- | :- |
| **[Stendhal] Le Rouge et le Noi** | 红与黑 |TODO  |


<div class="anim-box" style="
width: 3rem;
height:3rem;
background: red;
">
</div>

<style>
.logo {
  .bg {
    width: 10rem;
    height: 10rem;
    background: oklch(76.57% 0.222 358.96 / 0.1);

    display: flex; 
    justify-content: center;
    align-items: center;
  }
  .cube2,
  .cube3,.line {
    width: 9rem;
    height: 9rem;
    background: oklch(76.57% 0.222 358.96 / 0.1);
    position: absolute;
  }
  .cube3 {
    width: 8rem;
    height: 8rem;
    background: white;
    border-radius: 50%;
    border: 1px solid rgba(0,0,0,0.004);

  }
  .line{
    width: 10rem;
    height: 0.3rem;
    background: white;
  }
  .cube {
    width: 7rem;
    height: 7rem;
    background: oklch(76.57% 0.222 358.96 / 1);
    border-radius: 50%;
    position: relative;
  }
  .cube2{
    border-radius: 0.9px;
  }

  .w,
  .t {
    position: absolute;
    color: white;
  }
  .t {
    font: normal normal 400 12rem/ 1 Bungee;
    opacity: 0.4;
  }
  .w {
    font: normal normal 400 5rem/ 1 Bungee;
    opacity: 1;
  }
}
</style>

<div>
<div class="logo">
 <div class="bg">
  <div class="cube2"></div>
  <div class="cube3"></div>
  <div class="line"></div>
  <div class="cube"></div>
  <div class="t">T</div>
  <div class="w">W</div>
 </div>
</div>

</div>

<div class="review">
 <div class="top">  
  <div class="left">
    <div class="list">
     <div class="ep">
      <div class="meta">
       <div class="idx">01</div>
       <div class="score">8.5</div>
      </div>
      <div class="text"><p>There is a dog</p></div>
     </div>
     <div class="ep">
      <div class="meta">
       <div class="idx">13</div>
       <div class="score">7.7</div>
      </div>
      <div class="text"><p>
终于知道为什么要用3D了,因为可以用光追呀,而且Live本身工作量就很大,要么3D要么2D.
可如果在用2D的情况下突然来个3D又显得突兀,而且这也是用烂了的做法. 
与其如此倒不如全程3D,而不是2/3D混着来. 
加上光追的加持,气氛特效整个就上来啦!!! YES
而且ED的漫画风我也很喜欢,YES XDDD
当然,缺点就是歌不好听,486捧读,剧情有待观察
</p></div>
     </div>
    </div>
  </div>
  <hr />
  <div class="right">
   <div class="cover">
    <img src="https://p.sda1.dev/16/161963b590879f40e29530492dbb2744/20240416_001825.jpg"></img>
   </div>
  </div>
 </div>
 <div class="bottom">
  <hr />
  <a class="tag">movie</a>
  <div class="text">
   <p>There is a dog</p>
   <p>There is a dog</p>
   <p>There is a dog</p>
  </div>
 </div>
</div>

<box>
<div style="
width: 100%;
height: 10rem;
background: url(/Assets/2024/2024-06-27.avif) repeat-x 0 0/auto 100%;
margin: 1rem 0;"></div>
</box>


<css-doodle>
 :doodle {
   @grid: 8x8 / 10em / #f0f0f0 _1px;
   @shape: circle; 
   --s: 0;
 }
 :doodle(:hover) { 
   --s: 1;
 }
 background: #60569e;
 border-radius: 3px;
 @y(odd) {
   @shape: circle; 
   background: pink;
   border-radius: 0;
   :after { 
     content: "+";
   }
 }
 transition: 500ms cubic-bezier(.175, .885, .32, 1.275);
 transition-delay: @rand(300ms);
 transform: translateY(calc(var(--s) * 100%));
</css-doodle>
        
<css-doodle>
@grid: 1 / 16em;
background: @svg(
 svg {
   viewBox: 0 0 100 100;
   fill: none;
   style background: #0ce5f2;
   path*30 {
     stroke-linecap: round;
     stroke-dasharray: 0 8 5 6 3 12;
     stroke: @pn(
       #ff4ea5, yellow, @m4(#fff)
     );
     d: M 37 40
        Q @Plot(r: 80) @Plot(r: 150);
   }
 }
);
</css-doodle>

<css-doodle>
@grid: 24 / 240px / #4d49af +0.95;
@size: 100% 2px;
--n: @round(@dy/@dx + @dx/@dy);
margin: auto;
rotate: $(60n)deg;
background: hsl(
  $(36n), 80%, 80%
);
</css-doodle>

<css-doodle>
 @grid: 3x3 / 10em / #f0f0f0 _1px;
 /* elem */
 background: #60569e;
 transform: rotate(calc(@t / 10 * 1deg));
 transform: translateY(calc(@t / 100 * 1%));
</css-doodle>

<div class="vec-star">
 <svg class="star" viewBox="0 0 576 512" width="100" title="star">
       <path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7
       54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7
       68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5
       8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
        </svg>

 <div class="overlay"></div>
</div>


<div class="dict">

 <div class="examples">
  <h1>examples</h1>

  <div class="wrap">
   <div class="left">
     <span class="idx"></span>  
   </div>
   <div class="right">
     <div class="from">
       <p>hello</p> 
     </div>
     <div class="to">
      <p>你好</p> 
     </div>
   </div>
  </div>

  <div class="wrap">
   <div class="left">
     <span class="idx"></span>  
   </div>
   <div class="right">
     <div class="from">
       <p>hello</p> 
     </div>
     <div class="to">
      <p>你好</p> 
     </div>
   </div>
  </div>
 </div>

 <div class="synonyms">
  <h1>synonyms</h1>

  <div class="wrap">
   <div class="left">
     <span class="type" type="n."></span>  
   </div>
   <div class="right">
     <div class="from">
       <p>hello</p> 
     </div>
     <div class="to">
      <p>你好</p> 
     </div>
   </div>
  </div>

 </div>


</div>

<div class="ssr"></div>

<div class="fishway">
  <div class="bg">
    <div class="circle">
      <div class="wave">
      </div>
    </div>
  </div>
</div>

<box>
<div class="set-box">
<fieldset>
  <legend>AAA</legend>
  <textarea type="text" placeholder="some text"></textarea>
</fieldset>

 <div class="menu">
  <input id="1" name="r" type="radio" checked/>
  <label class="collapse" for="1">tab1</label>
  <div>111111111111111111111</div>

  <input id="2" name="r" type="radio"/>
  <label class="collapse" for="2">tab2</label>
  <div>2222222222222222222222</div>

  <input id="3" name="r" type="radio" />
  <label class="collapse" for="3">tab3</label>
  <div>333333333333333333333</div>

</div>
</div>


<div class="set-box">
<fieldset>
  <legend>AAA</legend>
  <textarea type="text" placeholder="some text"></textarea>
</fieldset>
</div>
</box>

{% desc() %}
清洗绿豆
直接把绿豆放入电饭锅中,放入刚好淹没过绿豆的水
通电将水煮干
拿出锅后用冷水冲洗绿豆后倒出水,重复几遍
lsls ksos
{% end %}


{{ jchart() }}

{% chat(name="dodo", txt="kwow sjsj sjwj") %}
ksejenejn snjsj snejej
{% end %}

{{ music_card() }}

<div class="qa-chat">
{% qa(q = "jdii jdj ehhh b?") %}
清洗绿豆
直接把绿豆放入电饭锅中,放入刚好淹没过绿豆的水
通电将水煮干
拿出锅后用冷水冲洗绿豆后倒出水,重复几遍
lsls ksos
{% end %}

<div class="list">

{% chat(name="dodo", txt="sllss sjsk sjsk") %}
skekke
{% end %}

{% chat(name="dodo", txt="hjdkh jkejkejk ejkehke ejk hekh eh kehi ebe ii ebbieeke hkekj je") %}
skekekmens nejej
{% end %}

</div>
</div>

<div class="morphing"></div>
<div class="test-box a-trc"></div>
<div class="test-circle"></div>


<div class="play" style="
  display: flex;
  gap: 1rem;               
  flex-wrap: wrap;
">
  <div class="eg-clip-path">
  <div class="bg"></div>
  <div class="fg" ty="circle"></div>
  </div>
  
  <div class="eg-clip-path">
  <div class="bg"></div>
  <div class="fg" ty="rect"></div>
  </div>

  <div class="eg-clip-path">
  <div class="bg"></div>
  <div class="fg" ty="rect-round"></div>
  </div>
</div>

<box>

<svg version="1.1" id="map_line_svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" height="300" viewBox="0 0 300 300" >

<rect x="50" y="100" width="200" height="100" rx="50" fill="#E0E9F6" stroke-width="4"  stroke="grey" stroke-dashoffset="600" stroke-dasharray="600">
 <animate attributeName="stroke-dashoffset" begin="1s" from="600" to="0" dur="7s" repeatCount="indefinite" />
 </rect>
</svg>
</box>

{% mermaid() %}
graph TD
A[Client] -->|tcp_123| B
B(Load Balancer)
B -->|tcp_456| C[Server1]
B -->|tcp_456| D[Server2]
{% end %}

{{ d3(desc="test") }}

{{ vg() }}

{{ photo_box(src="/Assets/2024/2024-06-27.avif") }}

{{ photo(src="/Assets/2024/2024-06-27.avif", date="2024.10.12", tag="music") }}

{% qa(q = "jdii jdj ehhh b?") %}
清洗绿豆
直接把绿豆放入电饭锅中,放入刚好淹没过绿豆的水
通电将水煮干
拿出锅后用冷水冲洗绿豆后倒出水,重复几遍
lsls ksos
{% end %}

{% jou(title="绿豆沙") %}
+ 清洗绿豆
+ 直接把绿豆放入电饭锅中,放入刚好淹没过绿豆的水
+ 通电将水煮干
+ 拿出锅后用冷水冲洗绿豆后倒出水,重复几遍
+ 放入适量的水煮一个钟,期间每个十分钟就打开盖子随便捞出绿豆壳
+ 等绿豆溶完后放入冰糖
+ 取出冷却后放入冰箱
+ 完
{% end %}

{% jou(color="purple") %}
2024-08-01
H2O
2/1
{% end %}

{% jou(color="pink") %}
test
{% end %}

{% jou(color="blue") %}
test
{% end %}


1. 123 abc
2. test
3. slslsl

ssjysjhshjshj
