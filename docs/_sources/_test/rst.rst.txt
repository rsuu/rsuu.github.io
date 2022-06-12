.. rst:directive:: md-tab-set

    Each set of tabs on a page must begin with a `md-tab-set` directive. This directive
    only accepts children that are `md-tab-item` directives.

    .. rst:directive:option:: class
        :type: string

        A space delimited list of qualified names that get used as the HTMl element's
        ``class`` attribute.

    .. rst:directive:option:: name
        :type: string

        A qualified name that get used as the HTML element's ``id`` attribute.

        Use the `ref` role to reference the element by name.

    This directive supports ``:class:`` and ``:name:`` options to use custom CSS classes
    and reference links (respectively).

    .. rst-example:: ``md-tab-set`` Example

        .. md-tab-set::
            :class: custom-tab-set-style
            :name: ref_this_tab_set

            .. md-tab-item:: Local Ref

                A reference to this tab set renders like so:
                `tab set description <ref_this_tab_set>`.

                This syntax can only be used on the same page as the tab set.

            .. md-tab-item:: Cross-page Ref

                To cross-reference this tab set from a different page, use
                :ref:`tab set description <ref_this_tab_set>`

                Clearly, this also works on the same page.

            .. md-tab-item:: Custom Rust

                .. literalinclude:: _static/test.rs
                    :language: rust
                    :start-after: /* ************************ custom-tab-set-style
                    :end-before: /* *********************** custom-tab-item-style
