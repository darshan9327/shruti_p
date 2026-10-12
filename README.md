# SHRUTI — The Creator Edit

Animated React + TypeScript portfolio built with Vite, Tailwind CSS and Motion. Authentic images were retrieved from the public @_.shru_.ti19 Instagram profile at the user's request on October 12, 2026.

## Run locally

Requires Node.js 20.19+ (or 22.12+).

```sh
npm install
npm run dev
```

```sh
npm run build
npm run preview
```

## Content updates

- Edit `src/data.ts` for gallery entries, source links, categories, collaboration formats and contact identity.
- Photos live in `public/images/`. Replace with original high-resolution files when available; current images are optimized copies of public Instagram thumbnails.
- Hero rotates between three authentic photographs, with manual controls and a pause button. The animation responds to reduced-motion preferences.
- Add approved brand names, campaigns and testimonials to the empty arrays in `src/data.ts`; these sections remain unpublished while empty.
- The media kit is `public/shruti-media-kit.pdf`. Its optional regeneration script uses Python ReportLab, Pillow, PyMuPDF and Windows Georgia/Arial fonts.
- Statistics are limited to the brief's 10K+ followers, reels reaching millions of views, and paid/barter experience. Gallery titles are editorial labels, not original Instagram captions.

## Inquiries

The owner selected Instagram DMs. The form validates inputs and prepares a message locally. Visitors explicitly copy and send it on Instagram. No backend, email address, fabricated success confirmation, or automatic DM is used. Inputs are not stored or sent by this site. Instagram may require visitors to sign in before viewing reels or sending a message.

## Accessibility and interactions

Responsive layouts, keyboard navigation, focus-trapped native gallery dialogs, Escape dismissal, mobile menu, category filtering, original Instagram links, count-up stats, scrolling reveals, pause controls, and reduced-motion support are included.

## Deployment

`npm run build` outputs a static site in `dist/`. `.openai/hosting.json` retains the private Sites project identity. It can also run on any static host. The source contains no credentials.
