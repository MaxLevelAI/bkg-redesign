"""Refresh dist/products.json with the full copy from each BKG product page.

Run: python scrape_products.py
"""
import html, json, re, time, urllib.request
from pathlib import Path

PATH = Path(__file__).parent / 'dist' / 'products.json'

def text(fragment):
    t = html.unescape(re.sub(r'<[^>]+>', ' ', fragment)).replace('‍', '')
    return re.sub(r'\s+', ' ', t).strip()

def parse(page):
    block = re.search(r'class="rich-text-block w-richtext">(.*?)</div>', page, re.S)
    if not block:
        raise ValueError('product copy block not found')
    # The source pages are hand-edited and inconsistent (headings glued onto paragraphs, bullets as
    # "•" text or <li>), so flatten to one stream and re-split on the known markers.
    stream = '\n'.join(('• ' if tag == 'li' else '') + text(body)
                       for tag, body in re.findall(r'<(p|li)[^>]*>(.*?)</\1>', block.group(1), re.S))
    for marker in ('Research Material', 'Product Details', 'Research Context', 'All references are presented',
                   'At BKG Performance LAB', 'This product is intended strictly', '•'):
        stream = stream.replace(marker, '\n' + marker)
    segs = [re.sub(r'^Research Material\s*', '', re.sub(r'^•\s*', '• ', s.strip())) for s in stream.split('\n')]
    segs = [s for s in segs if s and s != '•' and s != 'Research Material']
    label = segs.pop(0) if segs and len(segs[0]) < 60 and 'Product Details' in stream else ''
    intro, details, context, disclaimer, section = [], [], [], [], 'intro'
    for s in segs:
        if s.startswith('This product is intended strictly'):
            section = 'disclaimer'
        if section == 'disclaimer':
            disclaimer.append(s)
            continue
        for head, name in (('Product Details', 'details'), ('Research Context', 'context')):
            if s.startswith(head):
                section, s = name, s[len(head):].strip()
        if not s:
            continue
        if section == 'details':
            k, _, v = s.lstrip('• ').partition(':')
            row = f'{k.strip()}: {v.strip()}'
            if v and row not in details:
                details.append(row)
        else:
            (intro if section == 'intro' else context).append(s)
    price = re.search(r'class="heading-16">\s*\$\s*([\d,.]+)', page)
    return {'label': label, 'intro': intro, 'details': details, 'context': context, 'disclaimer': disclaimer,
            'price': float(price.group(1).replace(',', '')) if price else None}

def fix_joined_words(products):
    """The source copy lost spaces at its line wraps ("studiedfor"). Split a word only where the
    same two words appear correctly spaced somewhere else in the catalog ("studied for")."""
    fields = [(p, k, i) for p in products for k in ('intro', 'context') for i in range(len(p.get(k, [])))]
    # Also split a rare word (shared copy repeats it at most twice) into two longer words that each recur elsewhere ("tissuerecovery").
    pairs, words = set(), {}
    for p, k, i in fields:
        ws = re.findall(r'[A-Za-z]+', p[k][i])
        pairs.update(zip(ws, ws[1:]))
        for w in ws:
            words[w] = words.get(w, 0) + 1
    def split(m):
        w = m.group(0)
        for cut in range(1, len(w)):
            a, b = w[:cut], w[cut:]
            if (a, b) in pairs or (words.get(w, 0) <= 2 and len(a) > 2 and len(b) > 2
                                   and words.get(a, 0) > 1 and words.get(b, 0) > 1):
                return f'{a} {b}'
        return w
    for p, k, i in fields:
        t = re.sub(r'[A-Za-z]{5,}', split, p[k][i])
        for joined in MANUAL_JOINS:  # leftovers whose halves never appear on their own
            t = t.replace(joined, MANUAL_JOINS[joined])
        p[k][i] = t

MANUAL_JOINS = {
    'allowingresearchers': 'allowing researchers', 'beenresearched': 'been researched',
    'byfacilitating': 'by facilitating', 'dermatologicalfunction': 'dermatological function',
    'exploringdermatological': 'exploring dermatological', 'extendedstimulation': 'extended stimulation',
    'instimulating': 'in stimulating', 'melaninproduction': 'melanin production',
    'particularlyin': 'particularly in', 'sleepquality': 'sleep quality', 'repairprocesses': 'repair processes',
    'mimicthe': 'mimic the',
}

def main():
    products = json.loads(PATH.read_text(encoding='utf8'))
    for p in products:
        req = urllib.request.Request(p['url'], headers={'User-Agent': 'Mozilla/5.0'})
        try:
            page = urllib.request.urlopen(req, timeout=30).read().decode('utf8', 'replace')
            data = parse(page)
        except Exception as e:  # keep the existing entry rather than lose data
            print('SKIP', p['slug'], e)
            continue
        price = data.pop('price')
        if price:
            p['price'] = price
        # a few BKG pages carry another product's label (copy-paste on the source site); drop those
        if data['label'].split(' ')[0].split('/')[0] not in p['name']:
            data['label'] = ''
        p.update(label=data['label'], intro=data['intro'], context=data['context'], disclaimer=data['disclaimer'])
        if data['details']:
            p['details'] = data['details']
        p['sourceRetrieved'] = time.strftime('%Y-%m-%d')
        print('ok', p['slug'], len(p.get('context', [])), 'context paragraphs')
        time.sleep(0.5)
    fix_joined_words(products)
    PATH.write_text(json.dumps(products, indent=2, ensure_ascii=False), encoding='utf8')

if __name__ == '__main__':
    main()
