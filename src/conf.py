# -- Path setup --------------------------------------------------------------
import os
import sys
import typing

sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("./_plug"))

import docutils
import sphinx
import sphinx.domains.python
import sphinx.environment
import sphinx.util.logging
import sphinx.util.typing

from sphinx_immaterial import apidoc_formatting


logger = sphinx.util.logging.getLogger(__name__)

# -- Project information -----------------------------------------------------
project = 'WeatherVane'
copyright = 'cc-by-nc-sa 4.0'
author = 'RSUU'
language = 'en'
html_search_language = 'zh'
html_use_index = False

# The full version, including alpha/beta/rc tags
#release = '0.0.1'


# -- General configuration ---------------------------------------------------
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

exclude_patterns = ['_build']

templates_path = [ '_templates' ]



# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

autoclass_content = "class"

autosummary_generate = True


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.imgmath",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    #"sphinx.ext.mathjax",
    "sphinx.ext.viewcode",

    "sphinx_immaterial",
    "sphinx_immaterial.theme_result",
    "sphinx_immaterial.kbd_keys",
    #"sphinx_immaterial.format_signatures",
    #"sphinx_immaterial.cppreference",
    #"sphinx_immaterial.json_domain",

    "sphinx_jinja",
    #"sphinxcontrib.details.directive",
    #"sphinx_comments",
    "sphinx_design",
    #"sphinx_comments", 

    # "hello",
    "myst_parser",
    #"yasfb", # rss feed
]



# myst
myst_heading_anchors = 6
myst_gfm_only = False
myst_hard_wrap = True
myst_enable_extensions = [
    #"amsmath",
    "colon_fence",
    #"deflist",
    #"dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    #"replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_substitutions = {
  "my_name": "name"
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_immaterial'
html_theme_options = {
    "plugins": ["tags","search"],
    "font": False,
    #"font": {"text": "", "code": ""},
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://rsuu.github.io",
    "repo_url": "https://github.com/rsuu/rsuu.github.io",
    "repo_name": "Zett",
    "repo_type": "github",
    "edit_uri": "blob/main/src",
    # "google_analytics": ["UA-XXXXX", "auto"],
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        "navigation.tabs",
        "toc.integrate",
        "navigation.sections",
        "navigation.instant",
        "header.autohide",
        "navigation.top",
        "navigation.tracking",
        "search.highlight",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Turn Off",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Turn On",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://rsuu.github.io",
            "title": "Home",
            "aliases": [],
        },

    ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
}

html_static_path = ["_static"]
html_css_files = [
    'extra_css.css',
    'style.css',
]

html_last_updated_fmt = "%Y-%m-%d (%H:%M %Z)"
html_title = "WeatherVane"
#html_favicon = "_static/svg/logo.svg"
#html_logo = "_static/svg/logo.svg"

# yasfb
feed_base_url = 'https://rsuu.github.io'
feed_author = 'RSUU'



from pygments.lexer import RegexLexer
from pygments import token
from sphinx.highlighting import lexers


todo_include_todos = True


object_description_options = []

# BEGIN: sphinx_immaterial.format_signatures extension options
object_description_options.append(
    ("cpp:.*", dict(clang_format_style={"BasedOnStyle": "LLVM"}))
)
# END: sphinx_immaterial.format_signatures extension options

object_description_options.append(("py:.*", dict(wrap_signatures_with_css=True)))

# BEGIN: sphinx_immaterial.external_cpp_references extension options
external_cpp_references = {
    "nlohmann::json": {
        "url": "https://json.nlohmann.me/api/json/",
        "object_type": "type alias",
        "desc": "C++ type alias",
    },
    "nlohmann::basic_json": {
        "url": "https://json.nlohmann.me/api/basic_json/",
        "object_type": "class",
        "desc": "C++ class",
    },
}
# END: sphinx_immaterial.external_cpp_references extension options


# BEGIN: cpp_strip_namespaces_from_signatures option
cpp_strip_namespaces_from_signatures = [
    "my_ns1",
    "my_ns2",
    "my_ns2::my_nested_ns",
]
# END: cpp_strip_namespaces_from_signatures option

rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight

.. role:: cpp(code)
   :language: cpp
   :class: highlight

.. role:: json(code)
   :language: json
   :class: highlight
"""


object_description_options.append(
    (
        "std:confval",
        dict(
            toc_icon_class="data", toc_icon_text="C", generate_synopses="first_sentence"
        ),
    )
)


object_description_options.append(
    (
        "std:objconf",
        dict(
            toc_icon_class="data",
            toc_icon_text="O",
            generate_synopses=None,
        ),
    )
)

object_description_options.append(
    (
        "std:themeconf",
        dict(
            toc_icon_class="data", toc_icon_text="T", generate_synopses="first_sentence"
        ),
    )
)

python_type_aliases = {}

# BEGIN: python_type_aliases example
python_type_aliases = {
    "MyUnqualifiedType": "alias_ex.MyUnqualifiedType",
}
# END: python_type_aliases example


jinja_contexts = {
    "sys": {"sys": sys},
}


json_schemas = ["index_transform_schema.yml", "inheritance_schema.yml"]


def _validate_parallel_build(app):
    # Verifies that all of the extensions defined by this theme support parallel
    # building.
    assert app.is_parallel_allowed("read")
    assert app.is_parallel_allowed("write")


def _parse_object_description_signature(
    env: sphinx.environment.BuildEnvironment, signature: str, node: docutils.nodes.Node
) -> str:
    registry = apidoc_formatting.get_object_description_option_registry(env.app)
    registry_option = registry.get(signature)
    node += sphinx.addnodes.desc_name(signature, signature)
    if registry_option is None:
        logger.error("Invalid object description option: %r", signature)
    else:
        node += sphinx.addnodes.desc_sig_punctuation(" : ", " : ")
        annotations = sphinx.domains.python._parse_annotation(
            sphinx.util.typing.stringify(registry_option.type_constraint), env
        )
        node += sphinx.addnodes.desc_type("", "", *annotations)
        node += sphinx.addnodes.desc_sig_punctuation(" = ", " = ")
        default_repr = repr(registry_option.default)
        node += docutils.nodes.literal(
            default_repr,
            default_repr,
            language="python",
            classes=["python", "code", "highlight"],
        )
    return signature


def _parse_confval_signature(
    env: sphinx.environment.BuildEnvironment, signature: str, node: docutils.nodes.Node
) -> str:
    values = env.config.values
    registry_option = values.get(signature)
    node += sphinx.addnodes.desc_name(signature, signature)
    if registry_option is None:
        logger.error("Invalid config option: %r", signature)
    else:
        default, rebuild, types = registry_option
        if isinstance(types, type):
            types = (types,)
        if types:
            type_constraint = typing.Union[tuple(types)]
            node += sphinx.addnodes.desc_sig_punctuation(" : ", " : ")
            annotations = sphinx.domains.python._parse_annotation(
                sphinx.util.typing.stringify(type_constraint), env
            )
            node += sphinx.addnodes.desc_type("", "", *annotations)
        if not callable(default):
            node += sphinx.addnodes.desc_sig_punctuation(" = ", " = ")
            default_repr = repr(default)
            node += docutils.nodes.literal(
                default_repr,
                default_repr,
                language="python",
                classes=["python", "code", "highlight"],
            )
    return signature


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
        parse_node=_parse_confval_signature,
    )

    app.add_object_type(
        "themeconf",
        "themeconf",
        objname="theme configuration option",
        indextemplate="pair: %s; theme option",
    )

    app.add_object_type(
        "objconf",
        "objconf",
        objname="object description option",
        indextemplate="pair: %s; object description option",
        parse_node=_parse_object_description_signature,
    )
    app.connect("builder-inited", _validate_parallel_build)
