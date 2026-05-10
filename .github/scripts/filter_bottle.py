import re, sys

pkg = sys.argv[1]
with open(f'/tmp/{pkg}.rb', 'r') as f:
    content = f.read()

def replace_bottle(m):
    lines = m.group(0).split('\n')
    ventura_line = next((l for l in lines if 'ventura:' in l and 'arm64' not in l), None)
    if ventura_line:
        return f'  bottle do\n{ventura_line}\n  end'
    return m.group(0)

content = re.sub(r'  bottle do.*?  end', replace_bottle, content, flags=re.DOTALL)
with open(f'/tmp/{pkg}.rb', 'w') as f:
    f.write(content)
print(f'OK: {pkg}')

