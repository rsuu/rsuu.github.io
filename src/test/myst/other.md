:octicon:`graph`

```yaml
theme:
  features:
    - content.code.annotate # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.


~~strikethrough with *emphasis*~~

![fishy](./test.svg)


```{image} ./test.svg
:alt: fishy
:class: bg-primary
:width: 200px
:align: center
```

<img src="./test.svg" alt="fishy" width="200px">


:::{figure-md} fig-target
:class: myclass

<img src="img/fun-fish.png" alt="fishy" class="bg-primary mb-1" width="200px">

This is a caption in **Markdown**
:::

[Go to the fish!](fig-target)


<div class="admonition">
<p>Some **content**</p>
  <div class="admonition tip">
  <div class="title">A *title*</div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  </div>
</div>

```{py:function} send_message(sender, priority)

Send a message to a recipient

:param str sender: The person sending the message
:param priority: The priority of the message, can be a number 1-5
:type priority: int
:return: the message id
:rtype: int
:raises ValueError: if the message_body exceeds 160 characters
```


:name only:
:name: body
:*Nested syntax*: Both name and body may contain **nested syntax**.
:Paragraphs: Since the field marker may be quite long, the second
   and subsequent lines of a paragraph do not have to line up
   with the first line.
:Alignment 1: If the field body starts on the first line...

              Then the entire field body must be indented the same.
:Alignment 2:
  If the field body starts on a subsequent line...

  Then the indentation is always two spaces.
:Blocks:

  As well as paragraphs, any block syntaxes may be used in a field body:

  - Me
  - Myself
  - I

  ```python
  print("Hello, world!")
  ```


aaaa

```{sidebar} My sidebar title
My sidebar content
```



bbbb
```{sidebar} My sidebar title
My sidebar content
```

+ aaa
  > 1. bbb
  > isish
  > 2. ccc
  > nji
