import json
cat=json.load(open('audit/catalog.json'))
todo={p['t']:p for p in cat['todo']}
def imgs(t,n=6,w=900): return [u+f'?width={w}' for u in todo[t]['imgs'][:n]]
L=[
 dict(key='Chloe Silverado', title='Chloé | Silverado | Red Leather Shoulder Bag', vendor='Chloé', type='Shoulder Bag', sku='B150', tags='chloé, silverado, red leather, braided handles, designer resale, shoulder bag', incl='Chloé dust bag and tags (pictured)'),
 dict(key='Loewe crossbody yellow', title='Loewe | Embossed Logo Flap Crossbody | Mustard Yellow', vendor='Loewe', type='Crossbody Bag', sku='B151', tags='loewe, crossbody, mustard yellow, grained leather, designer resale', incl='Flag for review'),
 dict(key='Hermes yacht canvas yellow tote', title='Hermès | Yachting Canvas Zip Pouch | Yellow', vendor='Hermès', type='Pouch', sku='B152', tags='hermes, canvas, yellow, zip pouch, designer resale', incl='Flag for review'),
 dict(key='Gucci snakeskin gold clutch', title='Gucci | Python Foldover Tassel Clutch | Metallic Gold', vendor='Gucci', type='Clutch', sku='B153', tags='gucci, python, metallic gold, clutch, tassel, exotic leather, designer resale', incl='Flag for review'),
 dict(key='Chanel cloth pouch chain', title='Chanel | Quilted Mini Chain Pouch | Black', vendor='Chanel', type='Mini Bag', sku='B154', tags='chanel, quilted, black, chain strap, cc logo, designer resale', incl='Flag for review'),
]
cards="".join(f'''<div class="card"><div class="ph"><img src="{imgs(l['key'],1,600)[0]}" alt="{l['title']}" loading="lazy"></div><div class="v">{l['vendor'].upper()}</div><div class="t">{l['title']}</div><div class="m">SKU {l['sku']} · {l['type']} · Qty 1</div><div class="flag">Price: from your inventory sheet</div></div>''' for l in L)
ch=imgs('Chloe Silverado',7,900)
gal="".join(f'<img src="{u}" alt="Chloé Silverado, photo {i+2}">' for i,u in enumerate(ch[1:7]))
html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Timeless Collective — listing trial by Andrei Pataleta</title><meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{ --ink:#121212; --mut:#6d6d6d; --line:#e5e5e5; --soft:#f6f6f6; --flag:#fff4cc; --flagink:#7a5a00; --ok:#1f7a3f; }}
  * {{ box-sizing:border-box; }} html {{ scroll-behavior:smooth; }}
  body {{ margin:0; background:#fff; color:var(--ink); font:16px/1.6 "Assistant", -apple-system, sans-serif; }}
  .wrap {{ max-width:1200px; margin:0 auto; padding:0 24px; }}
  .bar {{ background:#fff; border-bottom:1px solid var(--line); text-align:center; font-size:12px; letter-spacing:.14em; text-transform:uppercase; padding:9px; }}
  header.top {{ background:var(--ink); color:#fff; }} header.top .wrap {{ display:flex; align-items:center; justify-content:space-between; height:64px; font-size:13px; letter-spacing:.1em; text-transform:uppercase; }}
  header.top nav a {{ color:#fff; text-decoration:none; margin-left:24px; }}
  .hero {{ padding:60px 0 36px; }}
  .eyebrow {{ font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--mut); }}
  h1 {{ font-weight:300; font-size:52px; line-height:1.08; margin:12px 0 16px; letter-spacing:-.01em; }} h1 b {{ font-weight:600; }}
  .lead {{ font-size:18px; color:#333; max-width:780px; }}
  .stats {{ display:grid; grid-template-columns:repeat(4,1fr); border:1px solid var(--line); margin-top:32px; }} .stat {{ padding:18px 20px; border-left:1px solid var(--line); }} .stat:first-child {{ border-left:0; }}
  .stat b {{ display:block; font-size:34px; font-weight:600; line-height:1; }} .stat span {{ display:block; color:#444; font-size:14px; margin-top:8px; }} .stat small {{ display:block; font-size:12px; letter-spacing:.08em; text-transform:uppercase; margin-top:6px; color:var(--mut); }}
  section {{ padding:56px 0; border-top:1px solid var(--line); }}
  h2 {{ font-weight:600; font-size:30px; letter-spacing:.02em; text-transform:uppercase; margin:0 0 8px; }}
  .sub {{ color:#444; max-width:780px; margin:0 0 26px; font-size:17px; }}
  h4 {{ margin:0 0 12px; font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--mut); }} h4.after {{ color:var(--ink); }}
  .shot {{ border:1px solid var(--line); overflow:hidden; max-width:1000px; margin:0 auto; }} .shot img {{ display:block; width:100%; }}
  .caption {{ font-size:14px; color:var(--mut); margin-top:10px; text-align:center; }}
  .stack .col + .col {{ margin-top:36px; }}
  .grid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:20px; }}
  .card .ph {{ aspect-ratio:1/1; background:var(--soft); overflow:hidden; }} .card .ph img {{ width:100%; height:100%; object-fit:cover; }}
  .card .v {{ font-size:11px; letter-spacing:.14em; color:var(--mut); margin-top:10px; }} .card .t {{ font-size:14px; line-height:1.35; margin:2px 0 4px; }} .card .m {{ font-size:12px; color:var(--mut); }}
  .flag {{ display:inline-block; margin-top:8px; font-size:11px; letter-spacing:.06em; text-transform:uppercase; background:var(--flag); color:var(--flagink); padding:4px 8px; }}
  .pdp {{ display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,1fr); gap:40px; max-width:1120px; margin:0 auto; }}
  .gallery .main img {{ width:100%; display:block; background:var(--soft); }} .gallery .more {{ display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-top:6px; }} .gallery .more img {{ width:100%; aspect-ratio:1/1; object-fit:cover; display:block; background:var(--soft); }}
  .buy .v {{ font-size:11px; letter-spacing:.16em; color:var(--mut); }} .buy h3 {{ font-weight:400; font-size:30px; line-height:1.2; margin:4px 0 8px; }}
  .price {{ font-size:18px; margin-bottom:12px; display:flex; gap:10px; align-items:center; }}
  .btns {{ display:grid; gap:8px; margin:10px 0 18px; max-width:360px; }} .btns a {{ display:block; text-align:center; padding:12px; border:1px solid var(--ink); text-decoration:none; color:var(--ink); font-size:14px; letter-spacing:.06em; }} .btns a.solid {{ background:var(--ink); color:#fff; }}
  .desc p {{ margin:0 0 12px; font-size:15px; color:#333; }} .desc h5 {{ font-size:13px; letter-spacing:.14em; text-transform:uppercase; margin:18px 0 8px; font-weight:700; }} .desc ul {{ margin:0 0 12px; padding-left:18px; font-size:15px; color:#333; }} .desc li {{ margin-bottom:3px; }}
  .fl {{ background:var(--flag); color:var(--flagink); padding:1px 6px; font-size:12px; letter-spacing:.04em; text-transform:uppercase; }}
  .meta {{ border:1px solid var(--line); padding:14px 16px; font-size:13px; margin-top:18px; }} .meta div {{ display:grid; grid-template-columns:120px 1fr; gap:10px; padding:4px 0; }} .meta b {{ color:var(--mut); font-weight:600; letter-spacing:.08em; text-transform:uppercase; font-size:11px; padding-top:3px; }}
  .steps {{ display:grid; grid-template-columns:repeat(4,1fr); gap:18px; }} .step {{ border:1px solid var(--line); padding:20px; }} .step .n {{ font-size:12px; letter-spacing:.14em; color:var(--mut); }} .step h3 {{ font-size:17px; font-weight:600; margin:6px 0 8px; }} .step p {{ margin:0; font-size:14.5px; color:#333; }} .step code {{ font:12.5px Menlo, monospace; background:var(--soft); padding:1px 5px; }}
  .fixes {{ border:1px solid var(--line); max-width:1000px; margin:0 auto; }} .fx {{ display:grid; grid-template-columns:36px 1fr auto; gap:14px; align-items:start; padding:16px 20px; border-top:1px solid var(--line); }} .fx:first-child {{ border-top:0; }}
  .fx .n {{ font-size:18px; font-weight:600; }} .fx b {{ display:block; font-size:16px; }} .fx span {{ color:#444; font-size:15px; }} .fx .h {{ color:var(--mut); font-size:13px; white-space:nowrap; padding-top:4px; }} .fx .h.free {{ color:var(--ok); font-weight:600; }}
  .total {{ display:flex; justify-content:space-between; align-items:center; padding:16px 20px; background:var(--soft); font-size:15px; }} .total b {{ font-size:16px; }}
  .cta {{ background:var(--ink); color:#fff; padding:40px; display:flex; justify-content:space-between; align-items:center; gap:24px; }} .cta h2 {{ color:#fff; margin:0 0 6px; }} .cta p {{ margin:0; max-width:620px; color:#d8d8d8; }} .cta .who {{ text-align:right; font-size:14px; color:#d8d8d8; }} .cta .who b {{ display:block; color:#fff; font-size:17px; }} .cta a {{ color:#fff; }}
  footer {{ padding:28px 0 60px; color:var(--mut); font-size:13px; }}
  @media (max-width:900px) {{ h1 {{ font-size:34px; }} .stats {{ grid-template-columns:1fr 1fr; }} .stat:nth-child(3) {{ border-left:0; }} .stat:nth-child(n+3) {{ border-top:1px solid var(--line); }} .grid {{ grid-template-columns:1fr 1fr; }} .pdp,.steps {{ grid-template-columns:1fr; }} .fx {{ grid-template-columns:28px 1fr; }} .fx .h {{ grid-column:2; padding-top:0; }} .cta {{ flex-direction:column; align-items:flex-start; }} .cta .who {{ text-align:left; }} header.top nav {{ display:none; }} }}
</style></head>
<body>
<div class="bar">✦ Listing trial for Timeless Collective · built from the public store, no access · Andrei Pataleta ✦</div>
<header class="top"><div class="wrap"><div>Timeless Collective · trial</div><nav><a href="#five">The five</a><a href="#listing">One listing</a><a href="#flow">The workflow</a><a href="#plan">Plan</a></nav></div></header>

<div class="wrap hero">
  <div class="eyebrow">Free first hour · November 4, 2026</div>
  <h1><b>26 of your 88 listings</b> are live at $0.00 with no description.<br>Here are five of them, finished in your format.</h1>
  <p class="lead">I read your store from the outside. The 62 finished listings follow a clear, editorial format: Designer | Model | Color, a short intro, The Timeless Detail, Details, Condition, Includes, Authenticity. The other 26 are placeholders that shoppers can see right now on the Handbags page. Below: five of them written in your format from your photos, with the missing facts flagged for your review, the way you asked.</p>
  <div class="stats">
    <div class="stat"><b>88</b><span>products in the store</span><small>62 finished, 26 placeholders</small></div>
    <div class="stat"><b>$0.00</b><span>price on 26 live listings, no SKU, no description, no tags</span><small>Visible on Handbags and Shoes</small></div>
    <div class="stat"><b>40 of 51</b><span>images on the home page without alt text</span><small>No meta description either</small></div>
    <div class="stat"><b>3</b><span>announcement messages rotating above a 12-item menu with two empty collections</span><small>Vintage Jewelry and Sale: 0 products</small></div>
  </div>
</div>

<section id="five"><div class="wrap">
  <h2>Five placeholders, finished</h2>
  <p class="sub">Left: how they look on your Handbags page today. Below: the same five pieces with the title format, designer, type, SKU series and tags you already use. Price and anything not visible in the photos is flagged, not guessed.</p>
  <div class="stack">
    <div class="col"><h4>Before</h4><div class="shot"><img src="before-collection.jpg" alt="Handbags collection today"></div><p class="caption">“Gucci snakeskin gold clutch · $0.00”. A shopper sees this next to a $1,895 Saint Laurent.</p></div>
    <div class="col"><h4 class="after" style="text-align:center">After</h4><div class="grid">{cards}</div></div>
  </div>
</div></section>

<section id="listing"><div class="wrap">
  <h2>One of them, in full</h2>
  <p class="sub">Chloé Silverado, written exactly the way your Hermès and Chanel listings are written. Yellow marks are what I need from your inventory sheet before it goes live.</p>
  <div class="pdp">
    <div class="gallery"><div class="main"><img src="{ch[0]}" alt="Chloé Silverado red leather shoulder bag"></div><div class="more">{gal}</div></div>
    <div class="buy">
      <div class="v">CHLOÉ</div>
      <h3>Chloé | Silverado | Red Leather Shoulder Bag</h3>
      <div class="price"><span class="fl">Price: from your sheet</span><span style="color:var(--mut);font-size:14px">Quantity 1 · one of a kind</span></div>
      <div class="btns"><a class="solid" href="#">Add to cart</a><a href="#">Buy it now</a></div>
      <div class="desc">
        <p>A collector's Chloé from the house's most celebrated era. The Silverado is instantly recognisable by its braided leather handles, antique brass studs and softly slouched, pocketed body, a bag that defined the mid-2000s and still turns heads today.</p>
        <h5>The Timeless Detail</h5>
        <p>The handles are hand-braided strips of leather finished with brass rivets, so no two Silverados wear in quite the same way. The red here has kept its depth, with the leather softened into the relaxed shape the bag was designed for.</p>
        <h5>Details</h5>
        <ul><li>Brand: Chloé</li><li>Model: Silverado</li><li>Color: Red</li><li>Material: Leather</li><li>Hardware: Antique brass-tone studs and rivets</li><li>Braided double handles</li><li>Front flap pockets with stud closures</li><li>Origin: <span class="fl">confirm from tag</span></li><li>Measurements: <span class="fl">from your sheet</span></li></ul>
        <h5>Condition</h5>
        <p>Pre-owned. Leather is supple with the natural softening this model is known for. <span class="fl">Condition grade and notable wear from your sheet</span>. Please review all photographs carefully, as they form part of the item's description.</p>
        <h5>Includes</h5>
        <ul><li>Chloé dust bag (pictured)</li><li>Chloé tags and cards (pictured)</li><li>Certificate of Authenticity: <span class="fl">printed / CheckCheck, confirm</span></li></ul>
        <h5>Authenticity</h5>
        <p>Authenticity is at the heart of everything we do. Every item offered by Timeless Collective is carefully researched, inspected, and authenticated before being listed for sale. This piece is backed by our Timeless Collective Authenticity Guarantee, so you can shop with complete confidence.</p>
      </div>
      <div class="meta"><div><b>Vendor</b>Chloé</div><div><b>Type</b>Shoulder Bag</div><div><b>SKU</b>B150 (your B-series)</div><div><b>Tags</b>chloé, silverado, red leather, braided handles, designer resale, shoulder bag</div><div><b>Collections</b>Handbags · Chloé · New Arrivals</div><div><b>Inventory</b>1, track quantity, show “Sold” when gone</div></div>
    </div>
  </div>
</div></section>

<section id="flow"><div class="wrap">
  <h2>How the other 21 get done</h2>
  <p class="sub">One pass through your spreadsheet and photo folders, then a bulk import into drafts, then a QA pass before anything is published. You see every flag in one list, not in 21 separate messages.</p>
  <div class="steps">
    <div class="step"><div class="n">STEP 1</div><h3>Map your sheet once</h3><p>Your columns to Shopify's: Title, Vendor, Type, Tags, SKU, Price, Qty 1, Condition, Inclusions, Certificate. Condition and Inclusions become metafields so the theme can show them in the same place on every page.</p></div>
    <div class="step"><div class="n">STEP 2</div><h3>Photos by SKU</h3><p>Folder per SKU, files numbered in display order: <code>B150-01.jpg</code>, <code>B150-02.jpg</code>. The import places them in that order, main shot first, dust bag and tags last. Alt text generated from the title.</p></div>
    <div class="step"><div class="n">STEP 3</div><h3>Import to drafts, flag the gaps</h3><p>Bulk CSV import, all as drafts. Anything missing (price, measurements, serial, certificate type) goes into one shared sheet for you to fill, with the product link next to it.</p></div>
    <div class="step"><div class="n">STEP 4</div><h3>QA, then publish</h3><p>Every listing checked on desktop and phone: title format, photo order, price, quantity 1, collections, tags. Published in batches so New Arrivals stays fresh.</p></div>
  </div>
</div></section>

<section id="plan"><div class="wrap">
  <h2>Plan and hours</h2>
  <p class="sub">The five above are the paid trial you described, already done. The rest in order, with a preview before anything goes live.</p>
  <div class="fixes">
    <div class="fx"><div class="n">1</div><div><b>Trial: five listings in your format</b><span>Chloé, Loewe, Hermès, Gucci, Chanel above. I load them into your store the day I get access and your sheet.</span></div><div class="h free">Done, free</div></div>
    <div class="fx"><div class="n">2</div><div><b>The remaining 21 placeholders</b><span>Written, photos ordered, imported as drafts, flags sent in one sheet, published after your review.</span></div><div class="h">≈ 7 h</div></div>
    <div class="fx"><div class="n">3</div><div><b>Shop by designer</b><span>Automatic collections per designer from the Vendor field, a Designers menu, and filters for Designer, Category, Condition and Price.</span></div><div class="h">3 h</div></div>
    <div class="fx"><div class="n">4</div><div><b>Navigation and announcement bar</b><span>One menu instead of 12 items, remove the two empty collections, one announcement message instead of three rotating ones.</span></div><div class="h">1 h</div></div>
    <div class="fx"><div class="n">5</div><div><b>Consistent product pages</b><span>Condition and Includes shown in the same block on every listing from metafields, “Sold” badge instead of hiding one-of-a-kind pieces, same card format everywhere.</span></div><div class="h">3 h</div></div>
    <div class="fx"><div class="n">6</div><div><b>SEO basics</b><span>Meta descriptions, alt text on all images, titles that read “Chloé Silverado Red Leather Shoulder Bag | Timeless Collective”.</span></div><div class="h">2 h</div></div>
    <div class="fx"><div class="n">7</div><div><b>Shipping, inventory and checkout check</b><span>Free shipping rules you announce vs. what checkout actually does, quantity tracking, a test order end to end.</span></div><div class="h">2 h</div></div>
    <div class="fx"><div class="n">8</div><div><b>Handoff</b><span>A CSV template, the photo naming rule, and a short screen recording so you can add future inventory in minutes.</span></div><div class="h">2 h</div></div>
    <div class="total"><span>Two weeks from access, Pacific-hours overlap every day.</span><b>≈ 20 hours after the trial</b></div>
  </div>
</div></section>

<section><div class="wrap"><div class="cta"><div><h2>One evening, no access.</h2><p>Send the inventory sheet and I'll load the five into your store the same day. Then the other 21.</p></div><div class="who"><b>Andrei Pataleta</b>Full-stack engineer, ex-CTO · Miami, online through 6pm Pacific<br><a href="https://andrewpataleta.com">andrewpataleta.com</a></div></div></div></section>
<footer><div class="wrap">Prepared for Timeless Collective from the public store only. Photos belong to Timeless Collective. Model names identified from the photos; anything uncertain is flagged. Not indexed.</div></footer>
</body></html>'''
open('site/index.html','w').write(html); print('built', len(html))
