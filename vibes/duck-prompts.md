# Duck Skateboard — Codealong Prompt Sequence

Exact prompts for the three codealong steps. Each prompt is designed to be typed
into any AI chat tool (Claude.ai, ChatGPT, Gemini, etc.) and the output pasted
into the JS panel of the Phoenix Code starter pen.

---

## Step 1: Duck on a Skateboard (~10 min)

### The Prompt

> Write p5.js code that draws a duck riding a skateboard. Use simple shapes —
> circles for the body and head, a triangle for the beak, rectangles for the
> skateboard deck. Make the background a light blue sky with a gray ground at
> the bottom. The duck should be yellow with an orange beak. The skateboard
> should be red with dark gray wheels. The canvas should be 600 by 400 pixels.

### Instructor Notes

- Read the prompt aloud before typing it
- After AI responds, copy the entire code block
- In Phoenix Code: select all in the JS panel → paste → the preview pane should update instantly
- Ask the room: "What do you see? Does it look like a duck?"
- It probably won't be perfect — beak might be in the wrong spot, proportions may be off
- That's the point: **first draft, not final product**

### What to Look For in the Output

The AI should produce code with:
- `function setup()` — creates the canvas
- `function draw()` — runs every frame (even though nothing moves yet)
- Shape calls like `ellipse()`, `rect()`, `triangle()`, `fill()`
- Color values (either named colors or RGB)

Don't worry if it looks different from what you expected. Every AI tool will produce slightly different code.

---

## Step 2: Iterative Refinements (~10 min)

Send these **one at a time**. After each, copy the full updated code and paste it into Phoenix Code (replace all).

### Prompt 2a — Spinning Wheels

> Make the wheels spin — rotate them as if the skateboard is moving. Add small
> lines or marks on the wheels so the rotation is visible.

**What changes:** The AI should add `rotate()` and `push()`/`pop()` calls around the wheel drawing code, using `frameCount` to animate the rotation. The wheels should visibly spin.

### Prompt 2b — Bobbing Motion

> Add a little bobbing motion so the duck moves up and down slightly as it
> rides, like it's going over small bumps.

**What changes:** The AI should use `sin(frameCount * something)` to create a subtle vertical oscillation on the duck's y-position. The duck bobs gently.

### Prompt 2c — Helmet

> Add a small blue helmet on the duck's head. It should sit on top of the
> head circle like a dome.

**What changes:** An `arc()` or half-ellipse in blue drawn above the head circle. This is a small visual addition — good for showing that prompts don't have to be complex.

### Prompt 2d — Clouds

> Add two or three clouds that slowly drift across the sky from right to left.
> When a cloud goes off the left edge, it should reappear on the right.

**What changes:** The AI should add cloud objects (likely arrays or objects with x, y positions), drawn with overlapping ellipses, moving leftward each frame with wraparound logic.

### Instructor Notes

- **Don't rush.** Let each change land before moving on.
- If something breaks, model the debugging process live:
  - "The duck disappeared. Let me paste the code back to the AI and say: 'The duck is no longer visible after the last change. Here's my current code: [paste]. Fix it.'"
- Some attendees will be behind. That's fine — they can catch up or just watch.
- Key teaching moment: **"Small, specific follow-up prompts beat rewriting everything."**

---

## Step 3: Make It a Game (~5 min demo)

### The Prompt

> Turn this into a game. The duck should stay on the left side of the screen.
> Scroll the background, ground, and clouds from right to left to create the
> illusion of movement. Add obstacles — rocks or traffic cones — that scroll
> in from the right side at random intervals. The player presses the spacebar
> to make the duck jump over obstacles. Add a score counter in the top-left
> corner that increases by 1 each time an obstacle scrolls past the duck. If
> the duck collides with an obstacle, show "Game Over" and the final score on
> screen. Press R to restart the game. Keep the duck, skateboard, helmet, and
> visual style from before.

### Instructor Notes

- This is the "wow" moment. One prompt turns a drawing into a playable game.
- **Demo this on screen.** Type the prompt, get the response, paste it, play it.
- Try playing for 10–15 seconds. It might have bugs — jump too low, collision detection off, score not counting.
- If it has bugs, debug ONE on screen:
  - "The jump isn't high enough." → send that as a follow-up prompt
  - Or: "Obstacles are moving too fast, slow them down by half."
- **Don't fix everything.** The point is showing the process, not delivering a polished game.
- After the demo, transition: "That's what's possible. Now it's your turn."

### What to Look For in the Output

The AI should produce code with:
- `keyPressed()` function handling spacebar and R key
- Gravity/velocity logic for jumping
- An obstacle array with spawning and scrolling
- Collision detection (usually bounding box)
- Game state management (playing vs. game over)
- Score variable drawn with `text()`

---

## Troubleshooting Prompts

These are useful during free experimentation when attendees get stuck:

### "It's not working at all"

> My Phoenix Code is showing a blank/white screen. Here's the code in my JS panel:
> [paste]. The pen has p5.js loaded as an external library. What's wrong?

### "Part of it disappeared"

> After the last change, the [duck/skateboard/clouds] disappeared. Here's my
> current code: [paste]. Fix it so everything is visible again.

### "The game is too hard / too easy"

> The obstacles come too fast and the jump isn't high enough. Slow down the
> obstacle speed and increase the jump height.

### "I want to start over"

> Give me a clean p5.js sketch that draws a [describe what you want] on a
> 600x400 canvas. Use simple shapes and bright colors.

---

## Notes on AI Variation

Different AI tools will produce different code for the same prompt. This is normal and expected. Common differences:

- **Claude** tends to produce well-organized code with clear variable names
- **ChatGPT** tends to add more comments and sometimes extra features
- **Gemini** varies more between attempts

All of these are fine. The goal is a working visual result, not identical code across the room.
