## syntax

:::{note}
This text is **standard** _Markdown_
:::

:::{table} This is a **standard** _Markdown_ title
:align: center
:widths: grid

abc | mnp | xyz
--- | --- | ---
123 | 456 | 789
:::



:::{tab-item} Label2
:sync: key2

Content 2
:::



::::




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
