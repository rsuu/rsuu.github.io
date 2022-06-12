## syntax

important
hint
tip
seealso
note
todo
attention
caution
warning
danger
error
info
abstract
summary
tldr
success
check
done
question
faq
help
cite
quote
example
failure
fail
missing
bug

:::{table} This is a **standard** _Markdown_ title
:align: center
:widths: grid

abc | mnp | xyz
--- | --- | ---
123 | 456 | 789
:::


::::{md-tab-set}

:::{md-tab-item} Label1
Content 1
:::

:::{md-tab-item} Label2
2
:::

::::



```{eval-rst}
.. include:: ./rst.rst
```

```{literalinclude} test.rs
---
language: python
start-after: "/* ************************ custom-tab-set-style"
end-before: "/* *********************** custom-tab-item-style"
---
```

```{md-admonition}
:class: error

This example uses the styling of the ``error`` admonition

```

```{details} Closed by default
:class: help

Without the ``:open:`` flag, the admonition is collapsed by default.
```


```{eval-rst}
.. figure:: img/fun-fish.png
  :width: 100px
  :name: rst-fun-fish

  Party time!

A reference from inside: :ref:`rst-fun-fish`

A reference from outside: :ref:`syntax/directives/parsing`
```



```{md-mermaid}
:name: flowcharts

graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];

```