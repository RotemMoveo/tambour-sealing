# Tambour Waterproofing Mini-Site - design notes

Local HTML project, RTL Hebrew. Separate from the Compass site.

## Sources
- Style guide (Figma, read-only): https://www.figma.com/design/75zHsEov6cMIsCrNPEy01u/Tambour---Website-2025?node-id=2150-53333
- Old mini-site (content): https://old.tambour.co.il/professionals/עונת-האיטום-25/
- Figma file ngOng47ANtfNk6NJBGW3Au (Tambour-Dev): not readable via the MCP (needs a node selected in the desktop app)

## Tokens (from the style guide)
Colors: red-main #db0032, red-dark/hover #c2002c, red-80 #e2335b, red-70 #e64d70, red-30 #f4b2c1, red-20 #f8ccd6, red-10 #fbe5ea,
black-main #333032, System/Black #1F2227, black-hover #1f1e1f, green-main #1a3b3a, System/BG #EDEEEF, grey line #d9d9d9,
Gray/200 #898F98, Black 10-80: #e5e5e5 #ccc #b2b2b2 #999 #808080 #666 #4d4d4d #333, White Grid #ffffff4d.
Shadows: S 0 2 4 #0000000D; card 0 4 12 #0000001A; BIG 0 15 40 #0000001F.

Type: font "Simpler" (custom, Black 900 / Bold / Regular), fallback needed. Body in Inter in a few places.
Desktop: H1 90/0.96 Black, H2 44/0.96 Black, H2-S 35/1.1 Black, H3 30/1.2 Regular, H4 22/28 Black, Body 22/1.3, Body 18/1.3, Body 16/1.2, Legal 12, Link 16 Bold, Link 16 on Black.
Mobile: H1 54, H2 34, H2-S 30, H3 25, H4 20/24, Body L 17, Body M 16, Links 16.

Button main: height 52, radius 4, padding 12/20 (RTL), gap 8, red-main; hover and click #c2002c; disabled #999. Text Link 16 Bold white. Icon arrow-down-left 24 in a 32 box.
Secondary/link: red text with arrow icon. Tabs: red underline when active, chevron.

## Patterns seen in the live site screenshots
- Header: dark top bar (#333032) with search, utility icons, contact; white main nav with red logo, nav items, red "מניפת הגוונים" link with arrow; pink hairline under it.
- Page grid: thin pink (red-30) vertical/horizontal hairlines dividing cards; sections framed by lines.
- Product card: centered product image, bold name, small grey description, optional green tag "בנייה ירוקה" (dark green #1a3b3a/#255f4f), "לכל המוצרים" link with arrow at section bottom.
- Footer: dark #333032, logo, 5 link columns, newsletter band above (white, big heading, red button).

## Content
Content lives in `build.py` (CATS list), extracted from the old mini-site. `python3 build.py` regenerates surfaces/roofs/wet-rooms/joints.html from it (header/footer/landing main are taken from index.html) and downloads product/article images. Edit products, articles and videos there, not in the HTML.
- Videos: the old pages have a "סרטונים" anchor but no video found. The page shows 2 labelled placeholder cards; to add a real video, add its YouTube id to `data-yt` (js/video.js opens it in a dialog).
- Roofs body paragraph is a paraphrase of the old page summary - verify the wording.
- Product/article links point to old.tambour.co.il (as found); switch to tambour.co.il URLs before launch.
- Serve: `python3 -m http.server 3700` from this folder.

## Style guide page (style-guide.html)
Static RTL Hebrew page, open via the local server (`tambour-site` in .claude/launch.json, port 3700) at /style-guide.html. No build step; swatches, alias table, icons, type scale, button matrix and spacing table are rendered by the inline script from data arrays at the bottom of the file.

Structure follows the template PDF (~/Downloads/desktop.pdf, exported from Figma): chip nav, then per section a black label block + white doc pages (title, description, hr, content, footer).
- Colors: "Global" by palette group (Brand Primary, Brand Secondary, Brand Accent, Neutral, Positive, Negative, Warning, Neutral Alpha, White, Black) + "Alias" tables (Style Name / Global / Token / Use case) for Content, Surface, Border, Action.
- Icons: size 24 grid + anatomy.
- Typography: "Font" (Font Family, Font Size with px+rem, Font Weight, Line height, Decoration) + "Typography" table (Style / Font / Weight / Size / Line Height / Letter Spacing / Sample), desktop and mobile.
- Borders: Border Radius, Border Width, Shadows. Buttons: Buttons Radius, variants (Main-Primary / Secondary / Tertiary x Default / Hover / Focus / Disabled / Active), icon button, tabs, tag. Spaces: spacing scale, layout, breakpoints.
Positive / Negative / Warning are shown as "not defined" placeholders, same as the empty block in the template.

Added after review of the live site and the Figma brand book (canvas "Brand Style guide"; slides are the "Screenshot ..." rectangles, e.g. 311:21540 logo, 311:21543 colors, 311:21546 stamp, 311:21545/21537 graphic elements, 79:1412 applications):
- Logo section: vector logo/mark copied from the live site header (inline SVG symbols `#logo`, `#mark`; mark is on the LEFT of the wordmark, read RTL). Color versions, clear space (= mark height on every side), min size 20mm print, tagline lockups ("הצבע של ישראל"), colorless on photos, stamp (textPath arcs, Hebrew string reversed with bidi-override).
- Icons: redrawn from the site's SVG files (32px canvas, stroke 1.35, square caps, miter joins; arrows stroke 2). Top bar preview shows the RTL order (cart, heart, user, industry, text).
- Imagery + Graphics sections: photo rules, treatments (single rounded corner, hairline grid, cube crop), color swatch tile (Latin names in Nexa Black tracking 20, codes Nexa Heavy tracking 60), 3x3 module of the mark, cube compositions (upper cube right, lower cube left), poster applications, hero with grid. Photos are the low-res files in assets/img.
- Brand color specs (Pantone/CMYK/RGB/HEX for Red, White(black), Green) are from the brand book.
- Imagery palette (Desert Brown #7e482e, Land Brown #ad6e3b, Land Yellow #d58a3d, Balloon Yellow #e9a95b, Forest Green #657937, Wild Green #586e26, Deep Blue #0f253d) was SAMPLED from pixels of the brand-book slides; the book itself only shows a placeholder Pantone 0982P. Confirm with design.
- Nexa is not in the project; --latin falls back to Montserrat/Arial Black.
- Known gap: index.html/css/styles.css still draw the logo with a CSS approximation (.logo); swap in the SVG symbol when the mini-site is next touched.

Sources: tokens from this file and css/styles.css; brand red checked against the Figma brand book (file 75zHsEov6cMIsCrNPEy01u, canvas "Brand Style guide", node 2-349: Red DB0032, Black 000000, Green 1A3B3A). That canvas is mostly screenshots and has no Figma variables, so it gave no extra token values.

Assumptions, not from an official source - confirm with design:
- Token names (text-primary, border-grid, action-primary-hover, space-1..24) and Global names (Red/Main, Black/Main...) were invented for this page.
- Spacing scale is derived from values used in css/styles.css.
- Red/Press #a80027 (from the .btn:active rule) and Green/Tag #255f4f (from the screenshots) are not in the official guide.
- Icons are redrawn to match the live site (stroke 2, 24px in a 32px box), not the official icon library.
- Not covered: logo usage rules, the stamp/graphic motifs and photography from the brand book, tone of voice.


## Article page
Only article.html follows the live tambour.co.il article template (breadcrumb, pink chips, 44px red title, share, 1225x352 hero between pink lines, 673px text column, 22px/1.3). The rest of the mini-site keeps its original styling.
