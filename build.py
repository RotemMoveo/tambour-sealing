#!/usr/bin/env python3
"""Generates the four category pages from content below, re-using the header/footer of index.html.
Run: python3 build.py   (downloads product/article images on first run)"""
import os, re, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
OLD = "https://old.tambour.co.il"
P = OLD + "/product/"
A = OLD + "/professionals/professional-knowledge/"
UP = OLD + "/wp-content/uploads/"

ART_ALL = dict(title="כל פתרונות האיטום המתקדמים של טמבור - לכל אתגר ומטרה",
               url="article.html", internal=True,
               img="2021/07/The-sealing_350x350px-345x345.jpg")

CATS = [
 dict(slug="surfaces", file="surfaces.html", title="איטום משטחים", hero="cat-surfaces.jpg",
  lead="סילרים המבוססים על סולבנט או על מים, המיועדים לאיטום מגוון רחב של משטחים, בעלי יכולות מתקדמות לדחיית מים ולאיטום סדקים נימיים.",
  body=None,
  products=[
   ("סילר על בסיס מים 750", "%d7%a1%d7%99%d7%9c%d7%a8-%d7%a2%d7%9c-%d7%91%d7%a1%d7%99%d7%a1-%d7%9e%d7%99%d7%9d-750/", "2018/07/750_4L_V5_web-243x200.jpg", None),
   ("סילר מראה רטוב 752", "%d7%a1%d7%99%d7%9c%d7%a8-%d7%9e%d7%a8%d7%90%d7%94-%d7%a8%d7%98%d7%95%d7%91-752/", "2018/07/752_10L_v3_web-243x200.jpg", None),
   ("ננו סילר 755", "%d7%a0%d7%a0%d7%95-%d7%a1%d7%99%d7%9c%d7%a8-755/", "2018/07/755_1L_V3_WEB-1-243x200.jpg", None),
   ("איטום שקוף למשטחים מרוצפים PU 765", "%d7%90%d7%99%d7%98%d7%95%d7%9d-%d7%a9%d7%a7%d7%95%d7%a3-%d7%9c%d7%9e%d7%a9%d7%98%d7%97%d7%99%d7%9d-%d7%9e%d7%a8%d7%95%d7%a6%d7%a4%d7%99%d7%9d-pu-765/", "2024/11/PU765_web-243x200.jpg", None),
  ],
  articles=[ART_ALL]),
 dict(slug="roofs", file="roofs.html", title="איטום גגות", hero="cat-roofs.jpg",
  lead="פתרונות לאיטום יעיל של גגות חדשים וקיימים, לרבות פוליאוריתן טהור, משחות וחומרים אקריליים, בעלי עמידות למים עומדים.",
  body="איטום הגגות של טמבור משלב ותק ואמינות לצד טכנולוגיית פוליאוריתן מתקדמת. מוצרי TAMSEAL ופוליגג גמישים, גשרים על סדקים דינמיים ועומדים בתנאי מזג אוויר קיצוניים. ל-Tamseal 777 ול-PU780 החזרה סולארית גבוהה (הלבנה), המסייעת גם בבידוד תרמי ובחיסכון באנרגיה.",
  products=[
   ("איטום פוליאוריתני לגגות PU780", "pu780_waterproofing/", "2022/11/780_pu_20kg_v3_web-243x200.jpg", None),
   ("פוליאוריתן היברידי לאיטום גגות 777", "%d7%a4%d7%95%d7%9c%d7%99%d7%90%d7%95%d7%a8%d7%99%d7%aa%d7%9f-%d7%94%d7%99%d7%91%d7%a8%d7%99%d7%93%d7%99-%d7%9c%d7%90%d7%99%d7%98%d7%95%d7%9d-%d7%92%d7%92%d7%95%d7%aa-777/", "2018/07/777_polioriten_hybridi_15kg_img_v2_web-243x200.jpg", None),
   ("פוליגג 450", "%d7%a4%d7%95%d7%9c%d7%99%d7%92%d7%92-450/", "2018/07/polygag_450_web-243x200.jpg", None),
   ("פוליגג משוריין", "%d7%a4%d7%95%d7%9c%d7%99%d7%92%d7%92-%d7%9e%d7%a9%d7%95%d7%a8%d7%99%d7%99%d7%9f/", "2018/07/polygag_meshuryan_web-243x200.jpg", None),
  ],
  articles=[
   dict(title="מרוצים עד הגג: איך לייצר איטום מיטבי?", url="article-rain.html", internal=True, img="2020/11/שגיא-345x345.jpg"),
   dict(title="חם, חם, מתקרר: איך גגות לבנים עוזרים להוריד את הטמפרטורה", url="article-white-roofs.html", internal=True, img="2021/10/shutterstock_257429302-1-345x345.jpg"),
   ART_ALL]),
 dict(slug="wet-rooms", file="wet-rooms.html", title="איטום חדרים רטובים", hero="cat-wet.jpg",
  lead="מגוון פתרונות לאיטום חדרים רטובים, מרפסות ושימוש תת-קרקעי, שנועדו לשמור על עמידות החדר ללחות ורטיבות לאורך זמן.",
  body=None,
  products=[
   ("איטום אלסטי חד-רכיבי 700", "%d7%90%d7%99%d7%98%d7%95%d7%9d-%d7%90%d7%9c%d7%a1%d7%98%d7%99-%d7%97%d7%93-%d7%a8%d7%9b%d7%99%d7%91%d7%99-700/", "2018/07/700_web1-243x200.jpg", "תו ירוק"),
   ("פוליאוריתן ביטומן 707 PB", "polyurethane-bitumen-707-pb/", "2021/02/707_pb_23kg_v2_web-243x200.jpg", None),
   ("ביטומן פולימרי לאיטום 722", "%d7%91%d7%99%d7%98%d7%95%d7%9e%d7%9f-%d7%a4%d7%95%d7%9c%d7%99%d7%9e%d7%a8%d7%99-%d7%9c%d7%90%d7%99%d7%98%d7%95%d7%9d-722/", "2023/02/722_web-243x200.jpg", None),
   ("איטום ביטומני רב עובי 724", "%d7%90%d7%99%d7%98%d7%95%d7%9d-%d7%91%d7%99%d7%98%d7%95%d7%9e%d7%a0%d7%99-%d7%a8%d7%91-%d7%a2%d7%95%d7%91%d7%99-724/", "2020/12/724_web-243x200.jpg", None),
   ("משחה ביטומנית לאיטום 720", "%d7%9e%d7%a9%d7%97%d7%94-%d7%91%d7%99%d7%98%d7%95%d7%9e%d7%a0%d7%99%d7%aa-%d7%9c%d7%90%d7%99%d7%98%d7%95%d7%9d-720/", "2018/07/720_web-243x200.jpg", None),
   ("איטום חד-רכיבי 790", "%d7%90%d7%99%d7%98%d7%95%d7%9d-%d7%97%d7%93-%d7%a8%d7%9b%d7%99%d7%91%d7%99-790/", "2018/07/790_gray_web-243x200.jpg", "תו ירוק"),
  ],
  articles=[ART_ALL]),
 dict(slug="joints", file="joints.html", title="איטום מישקים", hero="cat-joints.jpg",
  lead="פתרונות סיליקון לאיטום מישקים, המאופיינים בעמידות גבוהה ומונעים חדירת רטיבות ולחות.",
  body=None,
  products=[
   ("סיליקון צבעוני 100%", "%d7%a1%d7%99%d7%9c%d7%99%d7%a7%d7%95%d7%9f-%d7%a6%d7%91%d7%a2%d7%95%d7%a0%d7%99-rtv/", "2018/09/rtv_group_v3_web-243x200.jpg", None),
   ("סופר 8 HIGH TACK", "super-8-high-tack/", "2018/09/super_8_high_tack_white_web-243x200.jpg", None),
   ("סופר 8 HYBRID", "%d7%a1%d7%95%d7%a4%d7%a8-8-hybrid/", "2018/07/3-גוונים-W-243x200.jpg", None),
  ],
  articles=[ART_ALL]),
]

SITE = "https://tambour.co.il/product/"
MEDIA = "https://b2b.tambour.co.il/sfsites/c/cms/delivery/media/"
# (name, live product slug, media id, short description) - all from tambour.co.il/קטלוג-מוצרים/מוצרי-בנייה/איטום/
PROD = {
 "surfaces": [
  ("סילר 750", "סילר-750", "MC73ZWV3EH4RDWXAORCSPXB77KRE", "סילר על בסיס מים שקוף-מט לאיטום אבן סופגת, קירות ובטון טיח"),
  ("סילר 752", "סילר-752", "MCL54E4YFDG5G7XFYU3KDKAGYW5Y", "סילר לאיטום משטחים סופגים, מבליט את הגוון הטבעי של התשתית"),
  ("סילר 755", "סילר-755", "MCIRUEPDRMF5D7HEWBQKDDYT5SGU", "סילר בטכנולוגית ננו מתקדמת, דוחה מים, בגימור שקוף מט למגוון תשתיות סופגות"),
  ("TAMSEAL PU765 איטום שקוף למשטחים מרוצפים", "tamseal-pu765-איטום-שקוף-למשטחים-מרוצפים", "MCIXL4O74CZRFRHEINHIN6WW7GLM", "פוליאוריתן חד-רכיבי שקוף לאיטום בפני מים ועמיד בקרינת UV"),
 ],
 "roofs": [
  ("PU 780 - איטום פוליאוריתני לגגות", "pu-780-איטום-פוליאוריתני-לגגות", "MCB6NW5EXPIRCM7NSLSHQ5JGSVCI", "חומר איטום פוליאוריתני טהור חד-רכיבי, חזק וגמיש לאיטום גגות"),
  ("פוליאוריתן היברידי לגגות 777 TAMSEAL", "פוליאוריתן-היברידי-לגגות-777-tamseal", "MCED2XWKQ4LZCEBCHBUAMNRFWLIQ", "חומר איטום פוליאוריתני היברידי על בסיס מים לאיטום גגות בעל עמידות משופרת בפני מים עומדים ונזקי מזג אוויר"),
  ("פוליגג 450", "פוליגג-450", "MCDVF3D5ZFJBBODOMVC7UW55PTUI", "ציפוי אקרילי משוריין לאיטום והלבנת גגות, עם סיבים פולימריים המחזקים את הכושר האלסטי והעמידות המכנית"),
  ("פוליגג משוריין", "פוליגג-משוריין", "MC2GDNGXMTDRFOJM45KO4XGRIBGM", "ציפוי אקרילי משוריין לאיטום והלבנת גגות, עם סיבים פולימריים המחזקים את הכושר האלסטי והעמידות המכנית"),
 ],
 "wet-rooms": [
  ("פוליאוריתן ביטומן חד רכיבי TAMSEAL PB707", "פוליאוריתן-ביטומן-חד-רכיבי-tamseal-pb707", "MC44WK46TSDJDAFHCT2KGABML7JU", "חומר איטום חד-רכיבי על בסיס פוליאוריתן וביטומן לאיטום רצפות חדרים רטובים, מרפסות, קירות מרתף וכלונסאות"),
  ("ביטומן פולימרי לאיטום 722 TAMSEAL", "ביטומן-פולימרי-לאיטום-722-tamseal", "MC767TMD3CRZE7FP6TDMPZU7OBAA", "איטום ביטומני בתוספת פולימר בעל גמישות גבוהה"),
  ("איטום ביטומני רב עובי 724 TAMSEAL", "איטום-ביטומני-רב-עובי-724-tamseal", "MCGYK6K6WC7ZGI7H7H62FKZUEETY", "חומר איטום ביטומני מועשר בפולימרים ליישום רב עובי בשכבה אחת"),
  ("משחה ביטומנית לאיטום 720", "משחה-ביטומנית-לאיטום-720", "MCEBS6ZGLIANCSVB2XB2IEE6XCOI", "חומר מועשר בפולימרים לאיטום חדרים רטובים ומגוון שימושים"),
 ],
 "joints": [
  ("סיליקון צבעוני 100%", "סיליקון-צבעוני-100", "MC666GDEVRRJCB5H5GJ35NXJJDRU", "סיליקון צבעוני - 100% סיליקון, מתאים במיוחד לשימוש באמבטיות ומקלחונים"),
  ("סופר 8 היי-טאק", "סופר-8-היי-טאק", "MC3RA4A5I3DNAC7LGCCJ6ADZFBXQ", "חומר איטום והדבקה להדבקה מיידית ועוצמתית במיוחד"),
 ],
}
# products come from the old mini-site tiles (old.tambour.co.il/professionals/עונת-האיטום-25/...): name, link and full-size image

def q(u):
    return urllib.parse.quote(u, safe=":/%?=&")

def local(rel, kind):
    return "assets/img/%s/%s" % (kind, os.path.basename(rel))

def fetch(rel, kind):
    dst = os.path.join(ROOT, local(rel, kind))
    if os.path.exists(dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        req = urllib.request.Request(q(UP + rel), headers={"User-Agent": "Mozilla/5.0"})
        open(dst, "wb").write(urllib.request.urlopen(req, timeout=30).read())
    except Exception as e:
        print("WARN image", rel, e)

ARROW = '<svg aria-hidden="true"><use href="#arrow"/></svg>'

def fetch_media(mid):
    dst = os.path.join(ROOT, "assets/img/products", mid + ".jpg")
    if os.path.exists(dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        req = urllib.request.Request(MEDIA + mid, headers={"User-Agent": "Mozilla/5.0"})
        open(dst, "wb").write(urllib.request.urlopen(req, timeout=30).read())
    except Exception as e:
        print("WARN media", mid, e)

LIVE_PRODUCT = "https://tambour.co.il/product/"
# old-site product slug -> slug of the same product's page on tambour.co.il (only products that really exist there)
LIVE_SLUG = {
 "סילר-על-בסיס-מים-750": "סילר-750", "סילר-מראה-רטוב-752": "סילר-752", "ננו-סילר-755": "סילר-755",
 "איטום-שקוף-למשטחים-מרוצפים-pu-765": "tamseal-pu765-איטום-שקוף-למשטחים-מרוצפים",
 "pu780_waterproofing": "pu-780-איטום-פוליאוריתני-לגגות",
 "פוליאוריתן-היברידי-לאיטום-גגות-777": "פוליאוריתן-היברידי-לגגות-777-tamseal",
 "פוליגג-450": "פוליגג-450", "פוליגג-משוריין": "פוליגג-משוריין",
 "polyurethane-bitumen-707-pb": "פוליאוריתן-ביטומן-חד-רכיבי-tamseal-pb707",
 "ביטומן-פולימרי-לאיטום-722": "ביטומן-פולימרי-לאיטום-722-tamseal",
 "איטום-ביטומני-רב-עובי-724": "איטום-ביטומני-רב-עובי-724-tamseal",
 "משחה-ביטומנית-לאיטום-720": "משחה-ביטומנית-לאיטום-720",
 "סיליקון-צבעוני-rtv": "סיליקון-צבעוני-100", "super-8-high-tack": "סופר-8-היי-טאק",
}
# products with no page on tambour.co.il: we build the page (product_page below), content from the old site
LOCAL_PAGE = {"איטום-אלסטי-חד-רכיבי-700": "product-700.html", "איטום-חד-רכיבי-790": "product-790.html", "סופר-8-hybrid": "product-super-8-hybrid.html"}

def product_card(name, slug, path, tag=None):
    orig = path.replace("-243x200", "")
    key = urllib.parse.unquote(slug).strip("/")
    if key in LOCAL_PAGE:
        href, attrs = LOCAL_PAGE[key], ""
    else:
        href, attrs = LIVE_PRODUCT + urllib.parse.quote(LIVE_SLUG[key]) + "/", ' target="_blank" rel="noopener"'
    gtag = '<span class="gtag"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14M5 19c2-5 5-8 9-10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>בנייה ירוקה</span>' if tag else ""
    return ('<a class="pcard" href="%s"%s>' + gtag +
            '<div class="ph"><img src="%s" alt=""></div>'
            '<div class="pt"><h3><span class="t">%s</span><span class="parr" aria-hidden="true"><svg viewBox="0 0 25 24" fill="none"><path d="M16.78 8l-9 9" stroke="currentColor" stroke-width="2" stroke-linecap="square" stroke-linejoin="round"/><path d="M15.78 18h-9V9" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg></span></h3></div></a>') % (href, attrs, local(orig, "products"), name)

CAT_URL = OLD + "/ecatalogs/sealing-products-catalog/"

CARD_TAGS = {}

def article_card(a):
    tags = "".join('<span class="pill">%s</span>' % t for t in ["טיפים והשראה"])
    ext = a.get("internal") is not True
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return ('<a class="acard" href="%s"%s><div class="ph"><img src="%s" alt="" loading="lazy"></div>'
            '<div class="txt"><span class="pills">%s</span><h3 class="h4">%s</h3>'
            '<span class="link%s">קראו עוד%s</span></div></a>') % (a["url"], attrs, local(a["img"], "articles"), tags, a["title"], " ext" if ext else "", ARROW)

# real videos from the old Tambour site (old.tambour.co.il/professionals/עונת-האיטום-25/...), by category
VIDEOS = {
    "roofs": [
        ("777.mp4", "TAMSEAL 777 - פוליאוריתן היברידי לאיטום גגות", "ציפוי פוליאוריתני היברידי עם הידבקות טובה, עמיד במים ובפני קרינת UV, ומחזיר את קרני השמש להפחתת הטמפרטורה של המבנה."),
        ("poligag.mp4", "פוליגג - איטום גגות", ""),
    ],
    "wet-rooms": [("707.mov", "פוליאוריתן ביטומן 707 PB", "")],
    "joints": [("pu-flex-80.mp4", "PU FLEX 80", "")],
}

def video_card(v):
    f, title, desc = v
    return ('<button class="vcard" type="button" data-src="assets/video/%s">'
            '<span class="thumb"><img src="assets/video/%s.jpg" alt="" loading="lazy"><span class="play"><svg aria-hidden="true"><use href="#play"/></svg></span></span>'
            '<span class="h4">%s</span>%s</button>') % (f, f.rsplit(".", 1)[0], title, '<span class="vdesc">%s</span>' % desc if desc else "")

def related_card(c, num):
    return ('<a class="acard" href="%s"><div class="ph"><img src="assets/img/%s" alt="" loading="lazy"></div>'
            '<div class="txt"><span class="pills"><span class="pill">עולם האיטום</span></span><h3 class="h4">%s</h3>'
            '<span class="link">לקטגוריה%s</span></div></a>') % (c["file"], c["hero"].replace("cat-", "hero-"), c["title"], ARROW)

def cols_for(n):
    # columns on desktop: as many as products up to 4; 3 for 6 or 9 products
    return 4

def fillers(n):
    # empty cells keep the hairline grid closed (desktop: cols_for(n); tablet/mobile: 2 columns)
    cols = cols_for(n)
    return "".join('<div class="pfill%s" aria-hidden="true"></div>' % (" f2" if k < (-n) % 2 else "") for k in range((-n) % cols))

def main_for(i, c):
    n = len(c["products"])
    body = '<p class="body-text">%s</p>' % c["body"] if c["body"] else ""
    nxt = CATS[(i + 1) % 4]
    others = [(CATS.index(o) + 1, o) for o in CATS if o is not c]
    # videos only where the old site has them (surfaces/joints/wet-rooms pages have none we can show)
    vids = VIDEOS.get(c["slug"], [])
    videos_html = ('''  <section class="section videos" id="videos">
    <div class="wrap frame">
      <div class="sec-head"><h2 class="h2">סרטונים</h2></div>
      <div class="vgrid">%s</div>
    </div>
  </section>

''' % "".join(video_card(v) for v in vids)) if vids else ""
    return f'''<main id="main">
  <section class="hero cat-hero">
    <div class="wrap frame">
      <div class="hero-copy">
        <div class="crumbs"><a href="https://tambour.co.il/">עמוד הבית</a> › <a href="https://tambour.co.il/%D7%A7%D7%98%D7%9C%D7%95%D7%92-%D7%9E%D7%95%D7%A6%D7%A8%D7%99%D7%9D/">קטלוג מוצרים</a> › <a href="https://tambour.co.il/%D7%A7%D7%98%D7%9C%D7%95%D7%92-%D7%9E%D7%95%D7%A6%D7%A8%D7%99%D7%9D/%D7%9E%D7%95%D7%A6%D7%A8%D7%99-%D7%91%D7%A0%D7%99%D7%99%D7%94/">מוצרי בנייה</a> › <a href="index.html">עולם האיטום</a> › <b>{c["title"]}</b></div>
        <h1 class="h1">{c["title"]}</h1>
        <p class="lead">{c["lead"]}</p>
        {body}
      </div>
      <div class="hero-img" aria-hidden="true"><img src="assets/img/{c["hero"].replace("cat-","hero-")}" alt=""><i class="c0"></i><i class="c1"></i><i class="c2"></i></div>
    </div>
  </section>

  <section class="section" id="products">
    <div class="wrap">
      <div class="sec-head"><h2 class="h2">מוצרי האיטום של טמבור</h2></div>
      <div class="pgrid" style="--cols:{cols_for(n)}">{"".join(product_card(*p) for p in c["products"])}{fillers(n)}</div>
      <div class="pmore"><a class="link" href="{CAT_URL}" target="_blank" rel="noopener">לכל המוצרים{ARROW}</a></div>
    </div>
  </section>

{videos_html}
  <section class="section" id="articles">
    <div class="wrap frame">
      <div class="sec-head"><h2 class="h2">כתבות</h2></div>
      <div class="alist">{"".join(article_card(a) for a in c["articles"])}</div>
    </div>
  </section>

  <section class="section related">
    <div class="wrap">
      <div class="sec-head"><h2 class="h2">עוד פתרונות איטום</h2>
        <a class="btn" href="{nxt["file"]}"><svg aria-hidden="true"><use href="#arrow"/></svg>לקטגוריה הבאה: {nxt["title"]}</a></div>
      <div class="agrid n3">{"".join(related_card(o, k) for k, o in others)}</div>
    </div>
  </section>

  <section class="news rule">
    <div class="wrap">
      <div><h2>רוצים להיות מעודכנים בכל מה שחדש בטמבור?</h2><p>נרשמים לניוזלטר ונשארים מעודכנים בכל מה שחדש, מעניין ומעורר השראה בטמבור</p></div>
      <a class="btn" href="#"><svg aria-hidden="true"><use href="#arrow"/></svg>להרשמה</a>
    </div>
  </section>
</main>'''

LOGO_A = '<a class="logo" href="index.html" aria-label="טמבור - עמוד הבית"><svg viewBox="0 0 627 120" role="img" aria-label="טמבור"><use href="#logo"/></svg></a>'
SYMS = ('<symbol id="logo" viewBox="0 0 627 120"><path d="M0 119.791H69.8225C97.2878 119.791 119.625 97.2884 119.625 69.6578V0.000652889H40.5372V39.5446H80.4118V80.2471H39.7092V40.7032H0V119.791Z"/>'
        '<path d="M462.063 108.368C494.823 108.864 510.211 92.1536 510.211 57.9043C510.211 26.4671 495.981 11.4111 465.868 11.4111H406.47V108.203H439.892V41.5244H476.458V78.0896H451.804V108.203L462.063 108.368ZM211.066 108.203H244.489V47.9763C244.489 25.3097 229.929 11.4111 208.089 11.4111H157.625V41.5244H211.066V108.203ZM258.057 108.203H291.81V11.4111H258.057V108.203ZM305.046 108.203H394.556V78.0896H381.816V47.811C381.816 25.3097 367.422 11.4111 345.582 11.4111H305.046V41.5244H348.395V78.0896H305.046V108.203ZM522.785 108.368H585.824C607.995 108.368 626.194 90.1682 626.194 67.831V11.4111H568.12V41.5244H592.773V78.0896H556.207V11.4111H522.785V108.368Z"/></symbol>')

def shell(src, main, title, current):
    src = re.sub(r'<div class="crumbbar">.*?</div></div></div>\n?', '', src, flags=re.S)
    h = re.sub(r'<a class="logo" href="[^"]*"[^>]*>(?:טמבור<i></i>|<svg.*?</svg>)</a>', LOGO_A, src, flags=re.S)
    if 'id="logo"' not in h:
        h = h.replace('<symbol id="arrow"', SYMS + '<symbol id="arrow"', 1)
    h = re.sub(r'<main id="main">.*?</main>', lambda m: main, h, flags=re.S)
    h = re.sub(r'<title>.*?</title>', '<title>%s | טמבור</title>' % title, h)
    # breadcrumbs sit above the inner (sub) nav, like on the live site
    cm = re.search(r'<div class="crumbs">.*?</div>', main, flags=re.S)
    if cm:
        h = h.replace(cm.group(0), "", 1)
        h = h.replace('<nav class="subnav"', '<div class="crumbbar"><div class="wrap frame">%s</div></div>\n<nav class="subnav"' % cm.group(0), 1)
    h = h.replace(' aria-current="page">', '>', 99) if False else h
    h = re.sub(r'(<a class="t" href=")([^"]+)(")( aria-current="page")?', lambda m: m.group(1) + m.group(2) + m.group(3) + (' aria-current="page"' if m.group(2) == current else ''), h)
    # vertical grid lines run the full page height: one wrapper from the crumbs to the end of <main>
    h = h.replace('<div class="pagegrid">', '').replace('</main></div><!--/pagegrid-->', '</main>')
    if 'js/video.js' not in h:
        h = h.replace('<script src="js/site.js"></script>', '<script src="js/site.js"></script>\n<script src="js/video.js"></script>')
    return h

import article_content as AC
import articles_more as AM

# old-site product links inside the article -> live tambour.co.il product pages where the product exists there
LIVE = {
 "פוליגג-450": "פוליגג-450", "פוליגג-משוריין": "פוליגג-משוריין", "pu780_waterproofing": "pu-780-איטום-פוליאוריתני-לגגות",
 "פוליאוריתן-היברידי-לאיטום-גגות-777": "פוליאוריתן-היברידי-לגגות-777-tamseal",
 "polyurethane-bitumen-707-pb": "פוליאוריתן-ביטומן-חד-רכיבי-tamseal-pb707", "ננו-סילר-755": "סילר-755",
 "ביטומן-פולימרי-לאיטום-722": "ביטומן-פולימרי-לאיטום-722-tamseal", "איטום-ביטומני-רב-עובי-724": "איטום-ביטומני-רב-עובי-724-tamseal",
 "סיליקון-צבעוני-rtv-100-760": "סיליקון-צבעוני-100", "super-8-high-tack": "סופר-8-היי-טאק",
 "אוטם-פוליאוריתני-pu-flex-80": "pu-פלקס-80", "סיליקון-slf77": "סיליקון-slf-77",
}

def fix_links(html):
    def r(m):
        slug = urllib.parse.unquote(m.group(1))
        if slug in LIVE:
            return 'href="%s%s/" target="_blank" rel="noopener"' % (SITE, urllib.parse.quote(LIVE[slug]))
        return 'href="%s/product/%s/" target="_blank" rel="noopener"' % (OLD, urllib.parse.quote(slug))
    html = re.sub(r'href="https://old\.tambour\.co\.il/product/([^"/]+)/"', r, html)
    return re.sub(r'href="(https://old\.tambour\.co\.il/ecatalogs[^"]*)"', r'href="\1" target="_blank" rel="noopener"', html)

def fetch_art(rel, name):
    dst = os.path.join(ROOT, "assets/img/article", name)
    if os.path.exists(dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        req = urllib.request.Request(q(UP + rel), headers={"User-Agent": "Mozilla/5.0"})
        open(dst, "wb").write(urllib.request.urlopen(req, timeout=40).read())
    except Exception as e:
        print("WARN article image", rel, e)

def article_main(title, tags, hero, blocks, pre="", lead=None, gather=False, cur=None):
    """pre = file prefix for downloaded images; blocks as in article_content.py, plus ('video', youtube id)"""
    hero_name = (pre + "hero.jpg")
    fetch_art(hero, hero_name)
    out, n, col, gal, gpos = [], 0, [], [], None
    def flush():
        if col:
            out.append('<div class="art-col">%s</div>' % "".join(col))
            col.clear()
    def endgal():
        nonlocal gal
        if gal and not gather:
            out.append('<div class="art-gallery n%d">%s</div>' % (len(gal), "".join(gal)))
            gal = []
    if lead:
        col.append('<p class="art-lead"><b>%s</b></p>' % lead)
    for blk in blocks:
        k = blk[0]
        if k != "img":
            endgal()
        if k == "p":
            col.append("<p>%s</p>" % fix_links(blk[1]))
        elif k == "h2":
            col.append('<h2 class="art-h2">%s</h2>' % blk[1])
        elif k == "h3":
            col.append('<h3 class="art-h3">%s</h3>' % blk[1])
        elif k == "cta":
            col.append('<p><a class="link" href="%s" target="_blank" rel="noopener">%s<svg aria-hidden="true"><use href="#arrow"/></svg></a></p>' % (AC.CATALOG, blk[1]))
        elif k == "video":
            col.append('<div class="art-video"><iframe src="https://www.youtube-nocookie.com/embed/%s%s" title="סרטון" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>' % (blk[1], "?start=%d" % blk[2] if len(blk) > 2 else ""))
        elif k == "img":
            flush()
            n += 1
            fetch_art(blk[1], "%simg%d.jpg" % (pre, n))
            cap = blk[2] if len(blk) > 2 else ""
            capt = '<figcaption>%s</figcaption>' % cap if cap else ""
            fig = '<figure><img src="assets/img/article/%simg%d.jpg" alt="%s" loading="lazy">%s</figure>' % (pre, n, cap, capt)
            if gather:
                if gpos is None:
                    gpos = len(out); out.append("")
                gal.append(fig)
            else:
                if not gal:
                    flush()
                gal.append(fig)
    flush()
    endgal()
    if gather and gpos is not None:
        out[gpos] = '<div class="art-gallery n%d">%s</div>' % (len(gal), "".join(gal))
    tagh = "".join('<span class="pill">%s</span>' % t for t in tags)
    related = [a for a in CATS[1]["articles"] if a["url"] != cur]
    for a in related:
        if not a.get("internal"):
            fetch(a["img"], "articles")
    return f'''<main id="main">
  <article>
    <header class="art-head">
      <div class="wrap">
        <div class="crumbs"><a href="https://tambour.co.il/">עמוד הבית</a> › <a href="index.html">עולם האיטום</a> › <b>{title}</b></div>
        <div class="pills">{tagh}</div>
        <div class="art-titlerow">
          <h1 class="art-h1">{title}</h1>
          <div class="art-meta"><button class="share" type="button" data-share><img src="assets/icons/share.svg" alt="">שיתוף</button></div>
        </div>
      </div>
    </header>
    <div class="art-hero"><div class="wrap frame"><div class="hero-grid"><img src="assets/img/article/{hero_name}" alt=""><i></i></div></div></div>
    <div class="wrap frame art-body">{"".join(out)}</div>
  </article>
  <section class="section related-art">
    <div class="wrap frame">
      <div class="sec-head"><h2 class="h2">כתבות קשורות</h2><a class="link" href="roofs.html#articles">כל הכתבות{ARROW}</a></div>
      <div class="agrid n{len(related)}">{"".join(article_card(a) for a in related)}</div>
    </div>
  </section>
  <section class="news rule">
    <div class="wrap">
      <div><h2>רוצים להיות מעודכנים בכל מה שחדש בטמבור?</h2><p>נרשמים לניוזלטר ונשארים מעודכנים בכל מה שחדש, מעניין ומעורר השראה בטמבור</p></div>
      <a class="btn" href="#"><svg aria-hidden="true"><use href="#arrow"/></svg>להרשמה</a>
    </div>
  </section>
</main>'''

LAND_CRUMBS = '<div class="crumbs"><a href="https://tambour.co.il/">עמוד הבית</a> › <a href="https://tambour.co.il/%D7%A7%D7%98%D7%9C%D7%95%D7%92-%D7%9E%D7%95%D7%A6%D7%A8%D7%99%D7%9D/">קטלוג מוצרים</a> › <a href="https://tambour.co.il/%D7%A7%D7%98%D7%9C%D7%95%D7%92-%D7%9E%D7%95%D7%A6%D7%A8%D7%99%D7%9D/%D7%9E%D7%95%D7%A6%D7%A8%D7%99-%D7%91%D7%A0%D7%99%D7%99%D7%94/">מוצרי בנייה</a> › <b>עולם האיטום</b></div>'

def land_hero(h):
    # Figma 9386:14527 - big title + lead, then the wide photo with a 7-column grid (sub-nav stays above the hero)
    if 'land-hero' in h:
        return h
    photo = re.search(r'<div class="hero-photo".*?</div>', h, flags=re.S).group(0)
    lead = re.search(r'<p class="lead">(.*?)</p>', re.search(r'<section class="hero">.*?</section>', h, flags=re.S).group(0), flags=re.S).group(1)
    photo = photo.replace('<i class="fr"></i>', '<i class="fr"></i><i class="fr2"></i>')
    new = ('<section class="hero land-hero"><div class="wrap frame"><h1 class="h1">עולם האיטום</h1>'
           '<p class="lead">%s</p></div></section>\n<section class="land-photo"><div class="wrap frame">%s</div></section>' % (lead, photo))
    return re.sub(r'<section class="hero">.*?</section>', lambda m: new, h, count=1, flags=re.S)


UPL = OLD + "/wp-content/uploads/"
PRODUCT_PAGES = [
 dict(file="product-700.html", title="איטום אלסטי חד-רכיבי 700", img="2018/07/700_web1.jpg",
      sub="חומר איטום חד-רכיבי גמיש במיוחד על בסיס צמנט, לאיטום קירות ורצפות",
      uses="איטום קירות, רצפות, יסודות של מבנים, מרפסות, חדרים רטובים, ברכות שחיה, אדניות ותעלות ניקוז. מתאים לתשתיות מינרליות סופגות מסוג טיח צמנטי, בטון, בלוק גבס ולוח גבס (על גבי תשתית גבס חובה ליישם פריימר לחציצה בין הגבס לצמנט).",
      specs=[("מק\"ט", "67051x202500"), ("תצרוכת", "1ק״ג/מ״ר לשכבה (סה״כ 2 ק״ג למ״ר בעובי 2 מ״מ)"), ("מגיע בגוונים", "אפור / לבן"), ("גדלים", "קילוגרם")],
      docs=[("דף טכני", UPL + "2018/07/" + urllib.parse.quote("איטום-אלסטי-חד-רכיבי-700-TAMSEAL.pdf")),
            ("אישור איכות אוויר VOC", UPL + "2018/07/59249.A004.Tambour-700-LEED-AgB.en_.pdf")]),
 dict(file="product-790.html", title="איטום חד-רכיבי 790", img="2018/07/790_gray_web.jpg",
      sub="חומר איטום צמנטי חד-רכיבי, לאיטום קירות ורצפות בפני חדירת רטיבות. לשימוש פנימי וחיצוני",
      uses="איטום קירות בטון וטיח צמנטי, לרבות קירות בחדרים רטובים ואיטום ב״שיטת ברנוביץ׳״. מתאים לתשתיות מינראליות סופגות: בטון וטיח צמנטי. לשימוש פנימי וחיצוני.",
      specs=[("מק\"ט", "67050x202500"), ("תצרוכת", "2.5 ק״ג/מ״ר סה״כ ב-2 שכבות (1.5 ק״ג לשכבה ראשונה ו-1.0 ק״ג לשכבה שנייה)"), ("מגיע בגוונים", "אפור / לבן"), ("גדלים", "קילוגרם")],
      docs=[("דף טכני", UPL + "2018/07/" + urllib.parse.quote("איטום-חד-רכיבי-790-TAMSEAL.pdf"))]),
 dict(file="product-super-8-hybrid.html", title="סופר 8 HYBRID", img="2018/07/3-גוונים-W.jpg",
      sub="חומר הדבקה ואיטום למגוון רחב של חומרים, ניתן לצביעה. לשימוש פנימי וחיצוני",
      uses="איטום והדבקת פנלים, פסי גמר, משקופים, מראות וחומרי בידוד. להדבקת חומרים כמו בלוקים, מתכת, אלומיניום, זכוכית, פלסטיק, קרמיקה ועץ זה לזה. איטום זכוכית ביטחון. איטום פוגות במבנים (עד 25 מ\"מ). לאיטום בחדרי אמבטיה, שירותים ומטבחים. למילוי סדקים וחריצים. ניתן ליישום על משטחים סופגים ובלתי סופגים. ניתן ליישום על תשתיות לחות.",
      specs=[("מק\"ט", "98393XXX"), ("זמן פתוח", "5-10 דקות"), ("מגיע בגוונים", "שקוף ולבן"), ("גדלים", "גרם נטו")],
      docs=[("דף טכני", UPL + "2018/07/" + urllib.parse.quote("דף-טכני-סופר-8-היברידי-1-1.pdf"))]),
]

DOC_ICON = '<svg class="ic" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 2.5h8.5L19 7v14.5H6z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M14.5 2.5V7H19" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
DL_ICON = '<svg class="ic" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3v12m0 0-4.5-4.5M12 15l4.5-4.5M4 20h16" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg>'
EYE_ICON = '<svg class="ic" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M1.5 12S5.5 5 12 5s10.5 7 10.5 7-4 7-10.5 7S1.5 12 1.5 12z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.8"/></svg>'

def product_main(pp):
    imgf = local(pp["img"], "products")
    rows = "".join('<div class="trow"><span class="k">%s</span><span class="v">%s</span></div>' % kv for kv in pp["specs"])
    docs = "".join('<div class="drow"><a class="dn" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a><span class="da"><a href="%s" target="_blank" rel="noopener" aria-label="צפייה">%s</a><a href="%s" target="_blank" rel="noopener" download aria-label="הורדה">%s</a></span></div>'
                   % (u, DOC_ICON, n, u, EYE_ICON, u, DL_ICON) for n, u in pp["docs"])
    arts = "".join(article_card(a) for a in [ART_ALL, dict(title="מרוצים עד הגג: איך לייצר איטום מיטבי?", url="article-rain.html", internal=True, img="2020/11/שגיא-345x345.jpg"), dict(title="חם, חם, מתקרר: איך גגות לבנים עוזרים להוריד את הטמפרטורה", url="article-white-roofs.html", internal=True, img="2021/10/shutterstock_257429302-1-345x345.jpg")])
    return f'''<main id="main">
  <div class="crumbs"><a href="https://tambour.co.il/">עמוד הבית</a> › <a href="https://tambour.co.il/%D7%A7%D7%98%D7%9C%D7%95%D7%92-%D7%9E%D7%95%D7%A6%D7%A8%D7%99%D7%9D/">קטלוג מוצרים</a> › <b>{pp["title"]}</b></div>
  <section class="prod">
    <div class="wrap frame prod-grid">
      <div class="prod-media"><img src="{imgf}" alt="{pp["title"]}"></div>
      <div class="prod-info">
        <h1 class="prod-h1">{pp["title"]}</h1>
        <p class="prod-sub">{pp["sub"]}</p>
      </div>
    </div>
    <div class="wrap frame prod-grid prod-body">
      <div class="prod-empty" aria-hidden="true"></div>
      <div class="prod-col">
        <div class="ptabs"><a class="on" href="#tech">מידע טכני</a><a href="#docs">מסמכים ותווים</a></div>
        <div class="pbox" id="tech">
          <h2 class="ph2">תכונות המוצר</h2>
          <h3 class="ph3">שימושים</h3>
          <p class="puse">{pp["uses"]}</p>
          <h3 class="ph3">מידע טכני</h3>
          <div class="ttable">{rows}</div>
        </div>
        <div class="pbox" id="docs">
          <h2 class="ph2">מסמכים להורדה</h2>
          <h3 class="ph3">מפרטים טכניים</h3>
          <div class="dtable">{docs}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section pr-arts" id="articles">
    <div class="wrap frame">
      <div class="sec-head"><h2 class="h2">מאמרים קשורים</h2></div>
      <div class="alist">{arts}</div>
    </div>
  </section>

  <section class="news rule">
    <div class="wrap">
      <div><h2>רוצים להיות מעודכנים בכל מה שחדש בטמבור?</h2><p>נרשמים לניוזלטר ונשארים מעודכנים בכל מה שחדש, מעניין ומעורר השראה בטמבור</p></div>
      <a class="btn" href="#"><svg aria-hidden="true"><use href="#arrow"/></svg>להרשמה</a>
    </div>
  </section>
</main>'''

def lobby_html():
    # "כדאי להכיר" style products lobby (Figma 9386:19): title, category tabs, 4-column product cards, "all products" row
    tabs = "".join('<button type="button" class="lt%s" role="tab" data-t="%d">%s</button>' % (" on" if i == 0 else "", i, c["title"]) for i, c in enumerate(CATS))
    panels = "".join('<div class="lp%s" data-p="%d"><div class="pgrid" style="--cols:%d">%s%s</div></div>' % ("" if i == 0 else " off", i, cols_for(len(c["products"])), "".join(product_card(*p) for p in c["products"]), fillers(len(c["products"]))) for i, c in enumerate(CATS))
    return ('''<section class="section lobby" id="products">
    <div class="wrap frame">
      <div class="sec-head"><h2 class="h2">כדאי להכיר</h2></div>
      <div class="ltabs" role="tablist">%s</div>
      %s
      <div class="pmore"><a class="link" href="%s" target="_blank" rel="noopener">לכל המוצרים%s</a></div>
    </div>
  </section>

  ''' % (tabs, panels, CAT_URL, ARROW))

def main():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf8").read()
    for c in CATS:
        for p in c["products"]:
            fetch(p[2].replace("-243x200", ""), "products")
        for a in c["articles"]:
            fetch(a["img"], "articles")
    if 'land-hero' in src:  # source was already built: put the sub-nav back above <main>
        nv = re.search(r'<nav class="subnav".*?</nav>\n?', src, flags=re.S).group(0)
        src = src.replace(nv, "", 1).replace('<main id="main">', nv + '\n<main id="main">', 1)
    land = re.search(r'<main id="main">.*?</main>', src, flags=re.S).group(0)
    if 'class="crumbs"' not in land:
        land = land.replace('<div class="hero-copy">', '<div class="hero-copy">' + LAND_CRUMBS, 1) if 'land-hero' not in land else land.replace('<section class="hero land-hero">', '<section class="hero land-hero">' + LAND_CRUMBS, 1)
    land = re.sub(r'<section class="section lobby" id="products">.*?</section>\s*', '', land, flags=re.S)
    land = land.replace('<section class="section" id="featured">', lobby_html() + '<section class="section" id="featured">', 1)
    html = shell(src, land, "עולם האיטום", "index.html")
    html = land_hero(html)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf8").write(html)
    for i, c in enumerate(CATS):
        open(os.path.join(ROOT, c["file"]), "w", encoding="utf8").write(shell(src, main_for(i, c), c["title"], c["file"]))
    open(os.path.join(ROOT, "article.html"), "w", encoding="utf8").write(shell(src, article_main(AC.TITLE, AC.TAGS, AC.HERO, AC.BLOCKS, gather=True, cur="article.html"), AC.TITLE, ""))
    for a in AM.ARTICLES:
        pre = a["slug"].replace("article-", "").replace(".html", "") + "-"
        open(os.path.join(ROOT, a["slug"]), "w", encoding="utf8").write(shell(src, article_main(a["title"], a["tags"], a["hero"], a["blocks"], pre=pre, lead=a["lead"], cur=a["slug"]), a["title"], ""))
    for pp in PRODUCT_PAGES:
        fetch(pp["img"], "products")
        ph = shell(src, product_main(pp), pp["title"], "")
        ph = re.sub(r'<nav class="subnav".*?</nav>\n?', '', ph, count=1, flags=re.S)
        open(os.path.join(ROOT, pp["file"]), "w", encoding="utf8").write(ph)
    print("built", [c["file"] for c in CATS] + ["article.html"] + [a["slug"] for a in AM.ARTICLES])

main()
