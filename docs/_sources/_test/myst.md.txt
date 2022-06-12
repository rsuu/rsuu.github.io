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


::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::



::::{tab-set}

:::{tab-item} Label1
:sync: key1

Content 1
:::

:::{tab-item} Label2
:sync: key2

Content 2
:::

::::

::::{tab-set}

:::{tab-item} Label1
:sync: key1

Content 1
:::

:::{tab-item} Label2
:sync: key2

Content 2
:::

:::{literalinclude} _static/test.rs
:language: rust
:start-after: /* ************************ custom-tab-set-style
:end-before: /* *********************** custom-tab-item-style
:::

::::




::::{md-tab-set}

:::{md-tab-item} Label1
Content 1
:::

:::{md-tab-item} Label2
Content 2
:::

::::


