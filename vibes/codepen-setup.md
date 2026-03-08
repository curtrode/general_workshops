# Phoenix Code + p5.js Setup Guide

How to handle p5.js in Phoenix Code for the workshop.

---

## Recommended Approach: Starter Project

**Create a starter project with the p5.js script tag already included. Attendees open Phoenix Code and paste into the same file structure. Zero configuration needed.**

This eliminates the biggest friction point: attendees don't need to know about CDNs or external libraries. They open Phoenix Code, create the files, and go.

### How to Set Up

1. Go to **phcode.dev** and click **"Start Coding"** (no account needed)
2. Create a new file called **index.html**
3. Paste the starter HTML (see below) — it includes the p5.js CDN script tag
4. Create a new file called **sketch.js**
5. Paste the starter JS code (see below)
6. Click the **Live Preview** button (lightning bolt icon) to see the canvas

### Starter HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibe Coding Workshop</title>
  <script src="https://cdn.jsdelivr.net/npm/p5@1.11.3/lib/p5.min.js"></script>
</head>
<body>
  <script src="sketch.js"></script>
</body>
</html>
```

### Starter Code (sketch.js)

```javascript
// Vibe Coding Workshop — Starter Project
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
  text("Paste into sketch.js — Live Preview updates automatically", 300, 210);
}
```

### What to Tell Attendees

> "Go to phcode.dev and click Start Coding — no account needed. Create two files: index.html and sketch.js. Paste the starter code I'll share into each file. Click the lightning bolt icon for Live Preview. You'll paste AI-generated code into **sketch.js** — the preview updates automatically."

### index.html

The HTML file just loads p5.js from CDN and includes sketch.js. Attendees should **not** modify index.html — all p5.js code goes in sketch.js.

---

## Which File Does Code Go In?

This is the most common confusion. Be explicit and repeat it:

| File | What Goes There | For This Workshop |
|------|----------------|-------------------|
| **index.html** | HTML + script tags | Don't modify — already set up |
| **sketch.js** | JavaScript / p5.js code | **All p5.js code goes here** |

p5.js creates a `<canvas>` element automatically — no extra HTML needed. The canvas appears in the **Live Preview** panel.

### Phoenix Code Layout Tip

The Live Preview opens in a panel on the right side of the editor. If the preview is too small:

- Drag the divider between the editor and preview to give more space to the preview
- Or click the "Open in browser" icon to see the preview in a full browser tab

---

## Troubleshooting Common Setup Issues

### Blank preview / nothing shows up

- Is p5.js loaded? Check that index.html has the `<script src="https://cdn.jsdelivr.net/npm/p5@1.11.3/lib/p5.min.js"></script>` tag
- Is code in **sketch.js** (not index.html)?
- Is index.html referencing sketch.js with `<script src="sketch.js"></script>`?
- Open browser console (F12 or Cmd+Option+J) — look for red errors
- Most common error: `p5 is not defined` → the CDN script tag is missing from index.html

### "p5 is not defined" error

The CDN script tag is missing or misspelled in index.html. Make sure the `<script>` tag loading p5.js appears **before** the `<script src="sketch.js">` tag.

### Canvas shows but it's tiny or cut off

- Check that `createCanvas(600, 400)` is in the `setup()` function
- Make sure the Live Preview panel is large enough (drag the divider or open in browser)

### Live Preview not updating

- Make sure you've saved the file (Ctrl+S / Cmd+S)
- Phoenix Code's Live Preview should auto-refresh on save
- Try closing and reopening Live Preview (click the lightning bolt icon again)

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

## Why Phoenix Code?

**Phoenix Code is a great choice for a general audience:**

1. **No account needed** — go to phcode.dev and start coding immediately
2. Eliminates signup friction (no email, no password, no verification)
3. Real code editor experience with syntax highlighting and Live Preview
4. Files are organized naturally (index.html, sketch.js) — mirrors real web development
5. Free and open source

**Action item:** Test the setup flow on phcode.dev before the workshop. Create index.html and sketch.js with the starter code above, verify Live Preview works, and prepare to walk attendees through the same steps.
