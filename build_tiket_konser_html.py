# -*- coding: utf-8 -*-
"""
Generator Script for serkom_tiket_konser_lengkap.html
Builds a standalone, responsive, interactive, searchable HTML guide
with high-contrast VS Code dark theme code blocks, copy-to-clipboard buttons,
ERD visual diagram, MVC lifecycle diagram, interactive checklist, and printable layout.
"""

import os
import re
import html
import subprocess
import pygments
from pygments.token import Token
from pygments.lexers import PhpLexer, SqlLexer, BashLexer
from pygments.lexer import RegexLexer, bygroups, using
from pygments.lexers import JavascriptLexer

class BladeHtmlLexer(RegexLexer):
    """Lexer for Blade template code."""
    name = 'Blade'
    aliases = ['blade']
    filenames = ['*.blade.php']

    tokens = {
        'root': [
            (r'<!DOCTYPE.*?>', pygments.token.Name.Tag),
            (r'<!doctype.*?>', pygments.token.Name.Tag),
            (r'\{\{--', pygments.token.Comment.Multiline, 'blade-comment'),
            (r'\{\{', pygments.token.Punctuation, 'blade-echo'),
            (r'\{!!', pygments.token.Punctuation, 'blade-raw-echo'),
            (r'<!--[\s\S]*?-->', pygments.token.Comment),
            (r'(@[a-zA-Z_]\w*)(\s*)(\()', bygroups(pygments.token.Keyword, pygments.token.Text, pygments.token.Punctuation), 'blade-args'),
            (r'@[a-zA-Z_]\w*', pygments.token.Keyword),
            (r'<script.*?>', pygments.token.Name.Tag, 'script'),
            (r'<style.*?>', pygments.token.Name.Tag, 'style'),
            (r'</?[a-zA-Z0-9_\-:]+', pygments.token.Name.Tag, 'tag'),
            (r'&[a-zA-Z0-9#]+;', pygments.token.Name.Entity),
            (r'[^<@\{&]+', pygments.token.Text),
            (r'.', pygments.token.Text),
        ],
        'blade-comment': [
            (r'[^\-]+', pygments.token.Comment.Multiline),
            (r'--\}\}', pygments.token.Comment.Multiline, '#pop'),
            (r'-', pygments.token.Comment.Multiline),
        ],
        'blade-echo': [
            (r'\s+', pygments.token.Text),
            (r'\}\}', pygments.token.Punctuation, '#pop'),
            (r'\{\{--', pygments.token.Comment.Multiline, 'blade-comment'),
            (r'\b(old|route|session|asset|number_format|strtoupper|strtolower|compact|now|auth|url|back|csrf_token|__)\b', pygments.token.Name.Function),
            (r'\$[a-zA-Z_]\w*', pygments.token.Name.Variable),
            (r'->|::|\?\?|==|!=|<=|>=|===|!==|<|>|\?|:|\+|\-|\*|\/|\%|\.', pygments.token.Operator),
            (r'\'[^\']*\'', pygments.token.String.Single),
            (r'"[^"]*"', pygments.token.String.Double),
            (r'\b\d+(\.\d+)?\b', pygments.token.Number),
            (r'\b(true|false|null)\b', pygments.token.Keyword.Constant),
            (r'[a-zA-Z_]\w*', pygments.token.Name),
            (r'[,()\[\]]', pygments.token.Punctuation),
            (r'.', pygments.token.Text),
        ],
        'blade-raw-echo': [
            (r'\s+', pygments.token.Text),
            (r'!!\}', pygments.token.Punctuation, '#pop'),
            (r'.', pygments.token.Text),
        ],
        'blade-args': [
            (r'\(', pygments.token.Punctuation, '#push'),
            (r'\)', pygments.token.Punctuation, '#pop'),
            (r'\s+', pygments.token.Text),
            (r'\bas\b', pygments.token.Keyword),
            (r'\b(old|route|session|asset|number_format|strtoupper|compact|all|any|has|get|count|empty|selected|checked)\b', pygments.token.Name.Function),
            (r'\$[a-zA-Z_]\w*', pygments.token.Name.Variable),
            (r'->|::|==|!=|<=|>=|===|!==|<|>|\?|:|\.', pygments.token.Operator),
            (r'\'[^\']*\'', pygments.token.String.Single),
            (r'"[^"]*"', pygments.token.String.Double),
            (r'\b\d+\b', pygments.token.Number),
            (r'\b(true|false|null)\b', pygments.token.Keyword.Constant),
            (r'[a-zA-Z_]\w*', pygments.token.Name),
            (r'[,\[\]]', pygments.token.Punctuation),
            (r'.', pygments.token.Text),
        ],
        'tag': [
            (r'\s+', pygments.token.Text),
            (r'\{\{--', pygments.token.Comment.Multiline, 'blade-comment'),
            (r'\{\{', pygments.token.Punctuation, 'blade-echo'),
            (r'\{!!', pygments.token.Punctuation, 'blade-raw-echo'),
            (r'(@[a-zA-Z_]\w*)(\s*)(\()', bygroups(pygments.token.Keyword, pygments.token.Text, pygments.token.Punctuation), 'blade-args'),
            (r'@[a-zA-Z_]\w*', pygments.token.Keyword),
            (r'//.*$', pygments.token.Comment.Single),
            (r'[a-zA-Z0-9_\-:]+', pygments.token.Name.Attribute),
            (r'=', pygments.token.Operator),
            (r'"[^"]*"', pygments.token.String.Double),
            (r'\'[^\']*\'', pygments.token.String.Single),
            (r'/?>', pygments.token.Name.Tag, '#pop'),
            (r'.', pygments.token.Text),
        ],
        'script': [
            (r'</script>', pygments.token.Name.Tag, '#pop'),
            (r'[^<]+', using(JavascriptLexer)),
            (r'<', pygments.token.Operator),
        ],
        'style': [
            (r'</style>', pygments.token.Name.Tag, '#pop'),
            (r'[^<]+', pygments.token.Text),
            (r'<', pygments.token.Text),
        ]
    }

CONTROL_WORDS = {
    'return', 'if', 'else', 'elseif', 'foreach', 'endforeach', 'for', 'endfor',
    'while', 'endwhile', 'switch', 'case', 'break', 'continue', 'default',
    'try', 'catch', 'finally', 'throw', 'yield',
    '@if', '@else', '@elseif', '@endif', '@foreach', '@endforeach',
    '@forelse', '@empty', '@endforelse', '@csrf', '@method', '@include',
    '@extends', '@section', '@endsection', '@push', '@endpush'
}

PHP_FUNCTIONS = {
    'compact', 'now', 'view', 'redirect', 'route', 'session', 'asset', 'number_format',
    'strtoupper', 'strtolower', 'old', 'back', 'response', 'abort', 'csrf_token',
    'array_filter', 'array_map', 'array_merge', 'in_array', 'count', 'empty', 'isset',
    'latest', 'paginate', 'all', 'get', 'first', 'find', 'findOrFail', 'where', 'whereBetween',
    'create', 'update', 'delete', 'destroy', 'save', 'validate', 'hasFile', 'file',
    'store', 'exists', 'beginTransaction', 'commit', 'rollBack', 'transaction',
    'hasMany', 'belongsTo', 'belongsToMany', 'hasOne', 'decrement', 'increment', '__'
}

MARKERS = {
    '[TAMBAHKAN]': 'marker-tambahkan',
    '[UBAH]': 'marker-ubah',
    '[WAJIB]': 'marker-wajib',
    '[KUNCI]': 'marker-kunci',
}

def get_lexer(lang_or_file, code):
    low = lang_or_file.lower()
    if '.blade.php' in low or 'blade' in low:
        return BladeHtmlLexer()
    elif 'sql' in low:
        return SqlLexer()
    elif 'bash' in low or 'terminal' in low or 'sh' in low:
        return BashLexer()
    elif '.php' in low or 'php' in low:
        if '<?php' in code:
            return PhpLexer()
        else:
            return PhpLexer(startinline=True)
    return PhpLexer(startinline=True)

def classify_token(ttype, text):
    stripped = text.strip()
    if ttype in Token.Keyword:
        if stripped in CONTROL_WORDS or stripped.startswith('@'):
            return 'tok-ctrl'
        return 'tok-kw'
    if ttype in (Token.Name.Class, Token.Keyword.Type):
        return 'tok-class'
    if ttype in (Token.Name.Function,):
        return 'tok-fn'
    if stripped in PHP_FUNCTIONS:
        return 'tok-fn'
    if ttype in (Token.Name.Variable, Token.Name.Variable.Instance, Token.Name.Variable.Class):
        return 'tok-var'
    if ttype in Token.Literal.String:
        return 'tok-str'
    if ttype in Token.Literal.Number:
        return 'tok-num'
    if ttype in Token.Comment:
        return 'tok-cm'
    if ttype in (Token.Name.Tag, Token.Name.Entity):
        return 'tok-tag'
    if ttype in (Token.Name.Attribute,):
        return 'tok-attr'
    if ttype in (Token.Operator,):
        return 'tok-op'
    if ttype in (Token.Punctuation,):
        return 'tok-punc'
    if stripped and stripped[0].isupper():
        return 'tok-class'
    return None

def highlight_code(code, lang_or_file):
    lexer = get_lexer(lang_or_file, code)
    tokens = list(lexer.get_tokens(code))
    out = []
    
    marker_pattern = '(' + '|'.join(re.escape(m) for m in MARKERS.keys()) + ')'
    
    for ttype, text in tokens:
        escaped = html.escape(text)
        if ttype in Token.Comment and any(m in text for m in MARKERS):
            parts = re.split(marker_pattern, text)
            for part in parts:
                if not part:
                    continue
                if part in MARKERS:
                    out.append(f'<span class="{MARKERS[part]}">{html.escape(part)}</span>')
                else:
                    out.append(f'<span class="tok-cm">{html.escape(part)}</span>')
            continue
            
        cls = classify_token(ttype, text)
        if cls:
            out.append(f'<span class="{cls}">{escaped}</span>')
        else:
            out.append(escaped)
            
    return "".join(out)

def render_code_box(code, file_path, lang="php", label=None):
    code_clean = code.strip()
    highlighted = highlight_code(code_clean, file_path if file_path else lang)
    
    lang_badge = lang.upper()
    if 'blade' in file_path.lower():
        lang_badge = 'BLADE'
    elif '.php' in file_path.lower():
        lang_badge = 'PHP'
    elif 'sql' in lang.lower():
        lang_badge = 'SQL'
    elif 'bash' in lang.lower() or 'terminal' in lang.lower():
        lang_badge = 'TERMINAL'
        
    lbl_html = f'<span class="code-label">{html.escape(label)}</span>' if label else ''
    
    # Raw code for clipboard copy (cleaned for JS)
    escaped_raw = html.escape(code_clean, quote=True)
    
    return f"""
    <div class="code-container">
        <div class="code-header">
            <div class="code-file-info">
                <span class="file-icon">📄</span>
                <span class="file-path">{html.escape(file_path)}</span>
                {lbl_html}
            </div>
            <div class="code-actions">
                <span class="lang-badge">{lang_badge}</span>
                <button class="copy-btn" onclick="copyCode(this)" data-code="{escaped_raw}">
                    <span class="copy-icon">📋</span> Salin
                </button>
            </div>
        </div>
        <pre class="code-body"><code>{highlighted}</code></pre>
    </div>
    """

print("Writing full HTML generator...")
