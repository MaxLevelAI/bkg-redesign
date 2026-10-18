# BKG redesign — research and Webflow handoff

The direction is an immersive BKG storefront: deep navy, muted purple, warm beige, generous spacing, and the existing BKG bottle artwork. Peptide Foundry supplies the interaction and layout inspiration; BKG supplies the products, brand, prices, policies, and business information. The preview is a design implementation for review, not a confirmation that the production Webflow site has changed.

## What the reference does well

Contact sheets covering the complete reference recording, from 0 through 80 seconds, show a clear sequence: cinematic bottle hero; quick category entry points; featured products; a bottle that separates and reassembles while the visitor scrolls through successive claims; educational entry cards; an animated packaging section; FAQs; and a substantial footer. The ISO 5 and cGMP journeys use large laboratory scenes, changing text panels, and short comparison sections. Later footage shows the contact page, brand story, bundle builder, and full catalog. These are observations from the recording and supplied reference pages, not a claim about its original author or development tools. [Reference site](https://peptidefoundry.com)

The BKG recording, sampled throughout 0–46 seconds, already has strong bottle imagery and a recognizable palette. Its experience is dominated by a banner, signup form, category list, product grid, and footer. The redesign should connect these pieces with a clearer story, stronger navigation, more legible product cards, and useful destinations for the laboratory and affiliate content. [Current BKG site](https://www.bkgperformancepartners.com)

## Recommended experience

- **Home:** concise introduction, existing BKG hero media, featured catalog, scroll-driven bottle chapter, laboratory entry, shipping guidance, FAQs, and affiliate invitation.
- **Bottle chapter:** keep a BKG vial visible while three short sections explain the catalog, research context, and access to product details. Move and rotate the original artwork gently with scrolling. A true exploded assembly needs separate, accurate BKG cap, stopper, and vial assets; a single image should not masquerade as a fully modeled bottle.
- **Laboratory experience:** build an immersive, clearly labeled visual experience from existing BKG media, with restrained camera movement and layered information. The media does not establish that the pictured space is BKG's own facility. Do not transfer the reference's ISO 5, cGMP, or U.S. synthesis claims to BKG.
- **Catalog:** searchable, categorized cards using BKG's existing names, bottle images, prices, and links. Show a useful empty state and preserve product access on small screens. Inventory and checkout should remain connected to the actual store rather than simulated as successful purchases.
- **Affiliate page:** translate the supplied PDF into a readable program overview and application, with the original PDF available to download.

## Affiliate details to preserve

The PDF describes an application-based, commission-only program with **15% on eligible product revenue after discounts**, excluding tax, shipping, canceled orders, and refunded amounts. Recruitment alone earns no commission. BKG confirms eligibility, attribution, self-purchase rules, payout timing, and payment details in the affiliate agreement before activation.

The journey is application → BKG review → approval and onboarding → sharing through an assigned code or link. Approval is not guaranteed. Preserve all application questions, the requirement to disclose the affiliate relationship, research-only product presentation, and the Brian Gay non-endorsement statement. The form should prepare an email to **Sales@BKGPerformance.com** with subject **BKG Affiliate Application**, as the PDF permits answers in the email body. Label that action accurately: preparing an email is not submitting an application or sending data silently.

## Source discrepancies to resolve

| Source issue | Treatment |
| --- | --- |
| BPC capsule title says “500mgc.” | Flag the apparent unit typo for BKG confirmation; do not guess a strength. [Product](https://www.bkgperformancepartners.com/product/bpc-157-500mgc-capsules) |
| Standalone CJC-1295 No DAC 5mg uses the same CJC/Ipamorelin image as the blend. | Request the correct existing BKG artwork; do not invent a label. [Product](https://www.bkgperformancepartners.com/product/cjc-1295-no-dac-5mg) |
| Product template says shipping in 1–2 business days; shipping policy says processing in 1–3. | Use the policy: processing 1–3 business days; estimated delivery 2–7 business days after shipment, without a guarantee. [Policy](https://www.bkgperformancepartners.com/shipping-policy), [product template](https://www.bkgperformancepartners.com/product/bpc-157-10mg) |
| Several product URLs contain older strengths than their displayed titles. | Preserve URLs and current visible titles; never derive displayed strength from the URL alone. |

## Webflow implementation and quality

Map the design into reusable Webflow sections and bind catalog content to existing products. Keep pricing, availability, cart, and checkout in the production commerce system. A connected, authorized Webflow project is required to inspect and update the real site; a local preview or separately hosted preview does not accomplish that step.

For advanced motion, GSAP ScrollTrigger supports pinned sections and timelines synchronized to scrolling. Animate children inside the pinned container to preserve measurements. Use `gsap.matchMedia()` to rebuild the appropriate desktop, mobile, and reduced-motion behavior. [ScrollTrigger documentation](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), [matchMedia documentation](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/)

Respect reduced-motion settings with static bottle states and readable stacked content. Provide keyboard controls, visible focus, sufficient contrast, and pause controls for moving backgrounds. [Reduced-motion guidance](https://web.dev/articles/prefers-reduced-motion)

Compress bottle imagery, use responsive image sizes, defer nonessential media, supply video posters, and reserve media dimensions. Verify the complete journey on mobile and desktop, including search, empty states, product links, motion preferences, application email preparation, and the real checkout connection before publication.
