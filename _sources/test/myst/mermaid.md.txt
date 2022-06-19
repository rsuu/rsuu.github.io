## mermaid


+ TB - top to bottom
+ TD - top-down/ same as top to bottom
+ BT - bottom to top
+ RL - right to left
+ LR - left to right



```{md-mermaid}
:name: flowcharts

graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];

```


```{md-mermaid}
:name: flowcharts

graph
  z[张三] & L[李四]-->C[内卷] & D[躺平]
    
```

```{md-mermaid}
:name: flowcharts

sequenceDiagram
  participant Z  as 张三 
  participant L  as  李四 
  Z->L:我是没有箭头的实线
  L-->Z:我是没有箭头的虚线
  Z->>L:带箭头的实线
  L-->>Z:带箭头的虚线
  Z-xL:带x箭头实线
  L-)Z:结束时候 带箭头的实线
  Z--)L:结束时候 带箭头的虚线
```


```{md-mermaid}
:name: flowcharts

flowchart LR
  subgraph TOP
    direction TB
    subgraph B1
        direction RL
        i1 -->f1
    end
    subgraph B2
        direction BT
        i2 -->f2
    end
  end
  A --> TOP --> B
  B1 --> B2
```

### gantt

```{md-mermaid}
:name: gantt

gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
```



```{md-mermaid}
:name: gantt

gantt

    title N
    todayMarker off 
    dateFormat  YYYY
    axisFormat  %Y Ma

    section 侏罗纪
    早侏罗纪 :0174, 0201
    中侏罗纪 :active, c, 0163, 0174
    晚侏罗纪 :0145, 0163
    你 :active, b1, 0152, 0156

```


```{md-mermaid}
:name: pie

pie title NETFLIX

"早侏罗纪" : 27
"中侏罗纪" : 11
"晚侏罗纪" : 11
```