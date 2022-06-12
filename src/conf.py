# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------
project = 'RSUU'
copyright = '2020-, RSUU'
author = 'RSUU'
language = 'en'
html_search_language = 'zh'

# The full version, including alpha/beta/rc tags
#release = '0.0.1'


# -- General configuration ---------------------------------------------------
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

exclude_patterns = ['_build', '_templates']

templates_path = [ '_templates' ]

extensions = [
    "sphinx_comments",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_immaterial",

    "myst_parser",
    "sphinx_tabs.tabs",
    "sphinx_design",

    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    #"sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinxcontrib.details.directive",
    "sphinx_immaterial.theme_result",
    "sphinx_immaterial.kbd_keys",
    "sphinx_immaterial.format_signatures",
    "sphinx_immaterial.cppreference",
    "sphinx_immaterial.json_domain",
    "sphinx_jinja",

]


autosummary_generate = True


# myst
myst_heading_anchors = 6
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


comments_config = {
   "utterances": {
       "repo": "rsuu/rsuu.github.io",
       "issue-term": "pathname",
       "label": "comments",
       "theme": "github-dark",
       "crossorigin": "anonymous",
   }
}


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_immaterial'
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    #"site_url": "https://rsuu.github.io",
    "repo_url": "https://github.com/rsuu.github.io",
    "repo_name": "RSUU",
    "repo_type": "github",
    "edit_uri": "blob/main/docs",
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
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://rsuu.gtihub.io",
            "title": "Site",
            "aliases": [],
        },
        {
            "version": "https://rsuu.github.io",
            "title": "Github Pages",
            "aliases": [],
        },
    ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
}


# html_theme = 'sphinx_rtd_theme'
# html_theme_options = {
#     'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#     'analytics_anonymize_ip': False,
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     #'style_nav_header_background': 'white',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 6,
#     'includehidden': True,
#     'titles_only': False
# }



# html_theme = 'sphinx_book_theme'
# html_logo = "_static/logo-wide.svg"
# html_title = "Sphinx Book Theme"
# html_copy_source = True
# html_sourcelink_suffix = ""
# html_favicon = "_static/logo-square.svg"
# html_last_updated_fmt = ""
# html_theme_options = {
#     "path_to_docs": "docs",
#     "repository_url": "https://github.com/executablebooks/sphinx-book-theme",
#     # "repository_branch": "gh-pages",  # For testing
#     "launch_buttons": {
#         "binderhub_url": "https://mybinder.org",
#         "colab_url": "https://colab.research.google.com/",
#         "deepnote_url": "https://deepnote.com/",
#         "notebook_interface": "jupyterlab",
#         "thebe": True,
#         # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
#     },
#     "use_edit_page_button": True,
#     "use_issues_button": True,
#     "use_repository_button": True,
#     "use_download_button": True,
#     "use_sidenotes": True,
#     "logo_only": True,
#     "show_toc_level": 2,
# #    "announcement": (
# #        "⚠️The latest release refactored our HTML, "
# #        "so double-check your custom CSS rules!⚠️"
# #    ),
#     # For testing
#     # "use_fullscreen_button": False,
#     # "home_page_in_toc": True,
#     # "single_page": True,
#     # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
#     # "extra_navbar": "<a href='https://google.com'>Test</a>",
#     # "show_navbar_depth": 2,
# }

html_static_path = ['_static']

html_css_files = [
    #'my_style.css',
    #'dracula.css',
    #'dark.css',
]

from pygments.lexer import RegexLexer
from pygments import token
from sphinx.highlighting import lexers

class RVLexer(RegexLexer):
    name = 'riscv'
    tokens = {
        'root': [
            # Comment
            (r'#.*\n', token.Comment),
            # General Registers
            (r'\b(?:x[1-2]?[0-9]|x30|x31|zero|ra|sp|gp|tp|fp|t[0-6]|s[0-9]|s1[0-1]|a[0-7]|pc)\b', token.Name.Attribute),
            # CSRs
            (r'\bs(?:status|tvec|ip|ie|counteren|scratch|epc|cause|tval|atp|)\b', token.Name.Constant),
            (r'\bm(?:isa|vendorid|archid|hardid|status|tvec|ideleg|ip|ie|counteren|scratch|epc|cause|tval)\b', token.Name.Constant),
            # Instructions
            (r'\b(?:(addi?w?)|(slti?u?)|(?:and|or|xor)i?|(?:sll|srl|sra)i?w?|lui|auipc|subw?|jal|jalr|beq|bne|bltu?|bgeu?|s[bhwd]|(l[bhw]u?)|ld)\b', token.Name.Decorator),
            (r'\b(?:csrr?[rws]i?)\b', token.Name.Decorator),
            (r'\b(?:ecall|ebreak|[msu]ret|wfi|sfence.vma)\b', token.Name.Decorator),
            (r'\b(?:nop|li|la|mv|not|neg|negw|sext.w|seqz|snez|sltz|sgtz|f(?:mv|abs|neg).(?:s|d)|b(?:eq|ne|le|ge|lt)z|bgt|ble|bgtu|bleu|j|jr|ret|call)\b', token.Name.Decorator),
            (r'(?:%hi|%lo|%pcrel_hi|%pcrel_lo|%tprel_(?:hi|lo|add))', token.Name.Decorator),
            # Directives
            (r'(?:.2byte|.4byte|.8byte|.quad|.half|.word|.dword|.byte|.dtpreldword|.dtprelword|.sleb128|.uleb128|.asciz|.string|.incbin|.zero)', token.Name.Function),
            (r'(?:.align|.balign|.p2align)', token.Name.Function),
            (r'(?:.globl|.local|.equ)', token.Name.Function),
            (r'(?:.text|.data|.rodata|.bss|.comm|.common|.section)', token.Name.Function),
            (r'(?:.option|.macro|.endm|.file|.ident|.size|.type)', token.Name.Function),
            (r'(?:.set|.rept|.endr|.macro|.endm|.altmacro)', token.Name.Function),
            # Number
            (r'\b(?:(?:0x|)[\da-f]+|(?:0o|)[0-7]+|\d+)\b', token.Number),
            # Labels
            (r'\S+:', token.Name.Builtin),
            # Whitespace
            (r'\s', token.Whitespace),
            # Other operators
            (r'[,\+\*\-\(\)\\%]', token.Text),
            # Hacks
            (r'(?:SAVE_GP|trap_handler|__switch|LOAD_GP|SAVE_SN|LOAD_SN|__alltraps|__restore)', token.Name.Builtin),
            (r'(?:.trampoline)', token.Name.Function),
            (r'(?:n)', token.Name.Entity),
            (r'(?:x)', token.Text),
        ],
    }

lexers['riscv'] = RVLexer()




