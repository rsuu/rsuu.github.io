---
myst:
  substitutions:
    date: 1234
    key1: "I'm a **substitution**"
    key2: |
      ```{note}
      {{ key1 }}
      ```
    key3: |
      ```{image} img/fun-fish.png
      :alt: fishy
      :width: 200px
      ```
    key4: example
---

{{ my_name }}
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



```{eval-rst}
C++ domain customization
========================

.. confval:: cpp_strip_namespaces_from_signatures

   :python:`list[str]` specifying namespaces to strip from signatures.  This
   does not apply to the name of the symbol being defined by the signature, only
   to parameter types, return types, default value expressions, etc.

   For example, with the following in :file:`conf.py`:

   .. literalinclude:: conf.py
      :language: python
      :start-after: # BEGIN: cpp_strip_namespaces_from_signatures option
      :end-before: # END: cpp_strip_namespaces_from_signatures option

   .. rst-example:: C++ function definition with stripped namespaces

      .. cpp:type:: my_ns1::A

      .. cpp:type:: my_ns2::my_nested_ns::B

      .. cpp:type:: my_ns3::C

      .. cpp:function:: void my_ns1::MyFunction(my_ns1::A x, my_ns2::my_nested_ns::B y, my_ns3::C);

   .. warning::

      If a nested symbol name like :python:`"my_ns1::abc"` is specified in
      :confval:`cpp_strip_namespaces_from_signatures`, then a reference like
      :cpp:`my_ns1::abc::X` will be converted to :cpp:`my_ns1::X`.  To also
      strip the :cpp:`my_ns1::` portion, :python:`"my_ns1"` must also be
      specified in :confval:`cpp_strip_namespaces_from_signatures`.

.. confval:: cpp_qualify_parameter_ids

   Specifies whether function, template, and macro parameters should be assigned
   fully-qualified ids (for cross-linking purposes) of the form
   ``<parent-id>-p-<param-name>`` based on the id of the parent declaration.

   If set to :python:`False`, instead the shorter unqualified id
   ``p-<param-name>`` is used.  This option should only be set to
   :python:`False` if each C++ declaration is on a separate page.


:cpp:`#include` directives in signatures
----------------------------------------

This theme extend the C and C++ domains to allow signatures to specify required
:cpp:`#include` directives.

.. rst-example:: Specifying :cpp:`#include` directives in signatures

   .. cpp:function:: #include "my_header.h"
                     #include "another_header.h"
                     void foo(int param);

      Some function.

```


### 🔬

+ Linux

