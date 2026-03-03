# CodePen + p5.js Setup Guide

How to handle p5.js in CodePen for the workshop.

---

## Recommended Approach: Starter Pen

**Create a starter pen in advance. Attendees fork it. Zero configuration needed.**

This eliminates the biggest friction point: attendees don't need to know about CDNs, external libraries, or CodePen settings. They fork, paste, and go.

### How to Create the Starter Pen

1. Go to codepen.io and sign in with your account
2. Create a new Pen
3. Click the **Settings** gear icon (top of the editor)
4. Go to the **JS** tab in Settings
5. In **"Add External Scripts/Pens"**, paste:
   ```
   https://cdn.jsdelivr.net/npm/p5@1.11.3/lib/p5.min.js
   ```
6. Click **Save & Close**
7. In the **JS panel**, paste the starter code (see below)
8. **Save** the pen
9. Copy the pen URL — this is your share link

### Starter Code (JS Panel)

```javascript
// Vibe Coding Workshop — Starter Pen
// p5.js is already loaded. Paste AI-generated code here.

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(135, 206, 235); // light blue sky

  // gray ground
  fill(180);
  noStroke();
  rect(0, 340, 600, 60);

  // instructions
  fill(80);
  textSize(18);
  textAlign(CENTER, CENTER);
  text("Replace this code with AI-generated p5.js code", 300, 180);
  textSize(14);
  text("Paste into this JS panel — the preview updates automatically", 300, 210);
}
```

### What to Tell Attendees

> "Open this link: [your starter pen URL]. Click **Fork** in the bottom-right corner to make your own copy. You'll paste code into the **JS panel** — that's the bottom-left panel. The preview on the right updates automatically."

### HTML and CSS Panels

Leave them **empty**. All p5.js code goes in the JS panel. CodePen's default HTML includes a `<body>` tag, which is where p5.js will automatically insert its canvas. No HTML or CSS needed.

---

## Alternative: Walk Through Setup Live

If you prefer not to use a starter pen (or want attendees to understand the configuration), here's the walkthrough:

### During "Setup: CodePen Accounts" (5 min)

1. Everyone creates a free CodePen account at codepen.io
2. Create a new Pen (click "Pen" in the left sidebar)
3. Click **Settings** (gear icon, top of editor)
4. Click the **JS** tab
5. Under "Add External Scripts/Pens" — type `p5` and select **p5.js** from the autocomplete, or paste the CDN URL:
   ```
   https://cdn.jsdelivr.net/npm/p5@1.11.3/lib/p5.min.js
   ```
6. Click **Save & Close**
7. Now they're ready — code goes in the JS panel

### Risks with This Approach

- Takes longer (adds 2–3 min to setup)
- Some attendees will miss a step and get a blank screen
- You'll spend time debugging CodePen settings instead of coding
- Worth it only if "understanding the setup" is a learning objective

---

## Which Panel Does Code Go In?

This is the most common confusion. Be explicit and repeat it:

| Panel | What Goes There | For This Workshop |
|-------|----------------|-------------------|
| **HTML** | HTML markup | Leave empty |
| **CSS** | Stylesheets | Leave empty |
| **JS** | JavaScript code | **All p5.js code goes here** |

p5.js creates a `<canvas>` element automatically — no HTML needed. The canvas appears in the **preview pane** (right side or bottom, depending on layout).

### CodePen Layout Tip

Recommend attendees switch to a layout where the preview is large:

- Click **Change View** (top-left of editor)
- Select the layout with **editor on the left, preview on the right** — this gives the most space to see the canvas

---

## Troubleshooting Common Setup Issues

### Blank preview / nothing shows up

- Is p5.js loaded? Check Settings > JS > External Scripts — should show the p5 CDN URL
- Is code in the **JS** panel (not HTML or CSS)?
- Open browser console (F12 or Cmd+Option+J) — look for red errors
- Most common error: `p5 is not defined` → p5.js not loaded as external script

### "p5 is not defined" error

The external library wasn't added. Go to Settings > JS and add it.

### Canvas shows but it's tiny or cut off

- Check that `createCanvas(600, 400)` is in the `setup()` function
- Make sure the preview pane is large enough (change layout if needed)

### Code works locally but not in CodePen

- CodePen runs in an iframe — some browser APIs behave differently
- `createCanvas()` must be inside `setup()`, not at the top level
- `loadImage()` and `loadSound()` require CORS-compatible URLs

---

## p5.js CDN Details

**Recommended CDN URL:**
```
https://cdn.jsdelivr.net/npm/p5@1.11.3/lib/p5.min.js
```

This pins to version 1.11.3. Using a pinned version prevents breaking changes during the workshop if a new version is released.

**Alternative (latest):**
```
https://cdn.jsdelivr.net/npm/p5/lib/p5.min.js
```

Use the pinned version for the workshop.

---

## Decision: Starter Pen (Recommended)

**The starter pen approach is the clear winner for a general audience:**

1. Eliminates configuration friction (no CDN knowledge needed)
2. Ensures everyone starts from the same baseline
3. Saves 2–3 minutes of setup time
4. Reduces "my screen is blank" support requests
5. Fork operation is one click — intuitive even for non-technical users

**Action item:** Create the starter pen from your CodePen account, paste the starter code above, save it, and include the fork URL in the slides before the workshop.
