import re
with open('data/external/opencity_dataset_page.html', encoding='utf-8', errors='ignore') as f:
    content = f.read()
links = re.findall(r'href=[\"\'](.*?download.*?)[\"\']', content)
for l in links:
    print(l)
