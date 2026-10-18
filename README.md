# BKG Performance Partners — private redesign preview

This is a complete static frontend preview, built from BKG’s existing product images, product names, prices, categories, media, and the supplied affiliate PDF. It does not replace the production Webflow site.

## Pages
- index.html — cinematic bottle hero, curated products, scroll-driven bottle assembly, lab invitation, affiliate introduction, FAQ.
- shop.html — all 39 BKG products, 11 existing categories, search, price sorting, and quick views.
- product.html?item=... — original product image, price, and published product details when available; opens the current BKG store for ordering.
- lab.html — three-chapter scroll experience using BKG’s existing video assets.
- affiliate.html — 15% program, application workflow, downloadable original PDF, and locally prepared email draft.
- about.html and contact.html — brand introduction and contact email preparation.

## Run locally
Serve the dist folder over HTTP. With Python installed, run `python -m http.server 8765 --directory dist` and open http://localhost:8765. Fetching the product catalog requires HTTP; opening the HTML directly as a file is insufficient.

## Webflow implementation
The user chose to finish this preview before live implementation. The Webflow connection authenticated, but returned zero accessible sites; an explicit read of BKG’s published site ID also returned 404. No live Webflow data was changed.

After authorized site access is available, inspect site-specific instructions and create a staged design for review. Preserve existing ecommerce products, SKU bindings, inventory, cart, checkout, age gate, form handling, URLs, redirects, and legal pages. Translate these frontend layouts into Webflow components/classes or supported custom-code sections; do not replace the live ecommerce workflow with the preview’s catalog snapshot. Wire product cards to the current Webflow collections. No CMS synchronization or payment backend is included in this package.

Use styles.css and app.js as the visual and interaction reference. GSAP and ScrollTrigger are bundled locally. Fonts, optimized WebP images, and compressed videos are local. products.json records original source URLs. Never use a product slug to infer its strength; several original URLs retain old strengths. Product descriptions and prices are a snapshot, not a live inventory feed.

## Functional boundaries
Product buttons lead to BKG’s existing product pages. Affiliate and contact forms validate and prepare a mailto draft or downloadable text; they never send or store an application. The visitor reviews and sends from their email app. The affiliate commission terms are copied from the supplied BKG PDF. The lab visuals are brand imagery, not evidence of a specific facility or certifications. No reference-brand product claims, bottle artwork, or orange/white color system were imported.

## Validation
Verified local HTTP serving, all seven page routes, 39 product images, internal file references, JavaScript syntax, search results/empty state/reset, category filtering, ascending price sorting, quick view, mobile navigation, and email-draft preparation without sending. Inspected desktop and phone layouts and the bottle-scroll chapter transition. CSS and animation setup include operating-system reduced-motion behavior. See BKG-redesign-notes.md for detailed research and content discrepancies.
