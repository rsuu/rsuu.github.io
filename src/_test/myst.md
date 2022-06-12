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

```{md-tab-set}
            .. md-tab-item:: Cross-page Ref

                To cross-reference this tab set from a different page, use
                :ref:`tab set description <ref_this_tab_set>`

                Clearly, this also works on the same page.

            .. md-tab-item:: Custom Rust

                .. literalinclude:: ./test.rs
                    :language: rust
                    :start-after: /* ************************ custom-tab-set-style
                    :end-before: /* *********************** custom-tab-item-style


```