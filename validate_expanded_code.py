import json
import re
import subprocess
import tempfile
import os

with open("serkom-laravel.code-snippets", "r", encoding="utf-8") as f:
    snippets = json.load(f)

def expand_snippet(body_lines):
    expanded = []
    for line in body_lines:
        # VS Code expansion simulation:
        # ${1:default} -> default
        l = re.sub(r'\$\{[0-9]+:([^}]+)\}', r'\1', line)
        # $1, $2, $0 -> ""
        l = re.sub(r'\$[0-9]+', '', l)
        # \$ -> $
        l = l.replace(r'\$', '$')
        l = l.replace(r'\\', '\\')
        expanded.append(l)
    return "\n".join(expanded)

php_snippets_to_test = []
blade_snippets_to_test = []
sql_snippets_to_test = []

for name, data in snippets.items():
    prefix = data.get("prefix", "")
    body = data.get("body", [])
    expanded = expand_snippet(body)
    
    if prefix.startswith(("model-", "ctrl-", "mid-", "seeder-", "route-")):
        php_snippets_to_test.append((name, prefix, expanded))
    elif prefix.startswith("blade-"):
        blade_snippets_to_test.append((name, prefix, expanded))
    elif prefix.startswith("sql-"):
        sql_snippets_to_test.append((name, prefix, expanded))

print(f"PHP snippets to test: {len(php_snippets_to_test)}")
print(f"Blade snippets to test: {len(blade_snippets_to_test)}")
print(f"SQL snippets to test: {len(sql_snippets_to_test)}")

# Test PHP syntax with php -l if php is installed
php_available = False
try:
    res = subprocess.run(["php", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        php_available = True
        print("PHP CLI detected:", res.stdout.decode().splitlines()[0])
except Exception as e:
    print("PHP CLI not available:", e)

if php_available:
    for name, prefix, code in php_snippets_to_test:
        # Wrap if doesn't start with <?php
        test_code = code
        if not test_code.strip().startswith("<?php"):
            test_code = "<?php\n" + test_code
        
        with tempfile.NamedTemporaryFile("w", suffix=".php", delete=False, encoding="utf-8") as tf:
            tf.write(test_code)
            tf_path = tf.name
            
        try:
            res = subprocess.run(["php", "-l", tf_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if res.returncode != 0:
                print(f"PHP LINT ERROR in {prefix} ({name}):\n{res.stderr or res.stdout}")
            else:
                print(f"  [OK] {prefix} linted successfully")
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)
    print("PHP linting completed!")
