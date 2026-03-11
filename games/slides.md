---
theme: apple-basic
title: 'Conversation Coding: Build a Game with AI'
info: |
  Day 2: A hands-on workshop where students build a browser game
  by having a conversation with AI.
  No coding experience required.
author: Dr. Curt Rode
transition: fade-out
mdc: true
---

<script setup>
import { onBeforeUnmount, onMounted } from 'vue'

const flashCopied = (el) => {
  const orig = el.style.outline
  el.style.outline = '2px solid #22c55e'
  setTimeout(() => { el.style.outline = orig }, 600)
}

const copyText = async (text) => {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text)
      return true
    }
  } catch {
    // Fall through to legacy fallback.
  }

  const ta = document.createElement('textarea')
  ta.value = text
  ta.setAttribute('readonly', '')
  ta.style.position = 'fixed'
  ta.style.opacity = '0'
  ta.style.pointerEvents = 'none'
  document.body.appendChild(ta)
  ta.select()

  let copied = false
  try {
    copied = document.execCommand('copy')
  } catch {
    copied = false
  }
  document.body.removeChild(ta)
  return copied
}

const handleSelectAllClick = async (e) => {
  const target = e.target
  if (!(target instanceof Element)) return

  const el = target.closest('.select-all')
  if (!(el instanceof HTMLElement)) return

  const text = el.innerText.replace(/^Prompt:\s*/i, '').trim()
  if (!text) return

  if (await copyText(text)) flashCopied(el)
}

onMounted(() => {
  document.addEventListener('click', handleSelectAllClick)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleSelectAllClick)
})
</script>

# Conversation Coding
## Build a Game with AI

Dr. Curt Rode · TCU

<div class="abs-br m-6 text-sm opacity-50">
Day 2 · Hands-On Workshop · No Coding Experience Required
</div>

<!--
Welcome back. Last time we built websites. Today we're building games — playable browser games — using the same conversation-with-AI approach. Same tools, bigger ambition.
-->

---
layout: center
---

# What We're Doing Today

| Time | Activity |
|------|----------|
| 10 min | Quick recap + what's different today |
| 10 min | Anatomy of the prompt + pick your game |
| 10 min | Setup Phoenix Code + paste and play |
| 10 min | First iteration + manual edit challenge |
| 25 min | Vibe it — personalize your game |
| 15 min | Share + discussion |

<!--
The arc is similar to last time — concepts, then hands-on, then experimentation. But today we start with one big prompt instead of building up gradually. The iteration is where the real learning happens.
-->

---

# Quick Recap: What We Learned

<div class="grid grid-cols-2 gap-4 mt-3">
<v-clicks>

<div class="bg-blue-50 dark:bg-blue-900 rounded-xl p-3 shadow-sm">
  <div class="font-bold mb-1">The AI Coding Spectrum</div>
  <div class="text-sm opacity-80">Level 1 (tutor) → Level 2 (collaborative) → <strong>Level 3 (vibe coding)</strong> → Level 4 (autopilot)</div>
  <div class="text-xs mt-1 opacity-60">The right level depends on the task</div>
</div>

<div class="bg-green-50 dark:bg-green-900 rounded-xl p-3 shadow-sm">
  <div class="font-bold mb-1">The Core Cycle</div>
  <div class="text-sm opacity-80"><strong>Describe</strong> → Generate → <strong>Review</strong> → Refine → Repeat</div>
  <div class="text-xs mt-1 opacity-60">Your prompts are the creative work</div>
</div>

<div class="bg-amber-50 dark:bg-amber-900 rounded-xl p-3 shadow-sm">
  <div class="font-bold mb-1">Good Prompts</div>
  <div class="text-sm opacity-80">Specific outcomes, clear constraints, iterate in small steps</div>
  <div class="text-xs mt-1 opacity-60">Not "make me a website" — describe what you see</div>
</div>

<div class="bg-violet-50 dark:bg-violet-900 rounded-xl p-3 shadow-sm">
  <div class="font-bold mb-1">Your Guidelines</div>
  <div class="text-sm opacity-80">Review before moving on. Understand before publishing.</div>
  <div class="text-xs mt-1 opacity-60">Still applies — maybe even more so with games</div>
</div>

</v-clicks>
</div>

<!--
Quick touch on the key ideas from Day 1. We're not re-teaching these — just activating prior knowledge. The spectrum, the cycle, good prompts, and personal guidelines. All of this carries forward. Today we're applying these same ideas to a harder challenge.
-->

---

# What's Different Today

<div class="space-y-4 mt-4">
<v-clicks>

<div class="bg-blue-50 dark:bg-blue-900 rounded-lg p-4 flex items-start gap-4 shadow-sm">
  <div class="bg-blue-200 dark:bg-blue-700 rounded-full w-10 h-10 flex items-center justify-center flex-shrink-0 text-lg">1</div>
  <div>
    <div class="font-bold">One big prompt instead of building up</div>
    <div class="text-sm opacity-80">Last time: small prompts, one section at a time. Today: one detailed prompt generates a complete game. Then we iterate.</div>
  </div>
</div>

<div class="bg-violet-50 dark:bg-violet-900 rounded-lg p-4 flex items-start gap-4 shadow-sm">
  <div class="bg-violet-200 dark:bg-violet-700 rounded-full w-10 h-10 flex items-center justify-center flex-shrink-0 text-lg">2</div>
  <div>
    <div class="font-bold">Single file — everything stays together</div>
    <div class="text-sm opacity-80">No separate HTML/CSS/JS files. One HTML file with everything inline. Simpler to manage, easier to share.</div>
  </div>
</div>

<div class="bg-green-50 dark:bg-green-900 rounded-lg p-4 flex items-start gap-4 shadow-sm">
  <div class="bg-green-200 dark:bg-green-700 rounded-full w-10 h-10 flex items-center justify-center flex-shrink-0 text-lg">3</div>
  <div>
    <div class="font-bold">p5.js — a creative coding library</div>
    <div class="text-sm opacity-80">A free JavaScript library designed for visual and interactive projects. It handles drawing, animation, and keyboard input — perfect for games.</div>
  </div>
</div>

<div class="bg-amber-50 dark:bg-amber-900 rounded-lg p-4 flex items-start gap-4 shadow-sm">
  <div class="bg-amber-200 dark:bg-amber-700 rounded-full w-10 h-10 flex items-center justify-center flex-shrink-0 text-lg">4</div>
  <div>
    <div class="font-bold">Interactive, not static</div>
    <div class="text-sm opacity-80">Websites sit still. Games respond to you — keyboard input, collision, scoring, game states. Much more logic for the AI to handle.</div>
  </div>
</div>

</v-clicks>
</div>

<!--
Four key differences. The big one: we're front-loading the prompt. Last time we built up piece by piece. Today the first prompt does the heavy lifting, and our follow-ups are about refinement and personalization. Why? Because a game needs all its parts working together from the start — you can't play half a game. Also: single file. No switching between tabs. Everything is in one place, which makes iteration faster. p5.js is doing the heavy lifting under the hood — the AI knows how to use it, and it handles all the drawing and animation.
-->

---
layout: center
class: text-center
---

# Anatomy of the Prompt

### Before we paste it, let's understand what we're asking for

<div class="text-sm opacity-60 mt-4">A good prompt is a blueprint — every section has a purpose</div>

<!--
We're going to look at the prompt piece by piece before anyone pastes it. This is deliberate: understanding what you're asking for is the difference between Level 3 and Level 4 on the spectrum.
-->

---

# The Prompt: Setup & Direction

<div class="space-y-4 mt-4 text-sm">

<div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
  <div class="font-bold text-blue-600 dark:text-blue-400 mb-1">Context & Constraints</div>
  <div class="opacity-80">"I have no coding experience. I want you to build me a complete browser game in a single HTML file using the p5.js library (loaded from CDN)."</div>
  <div class="text-xs opacity-50 mt-2">Tells the AI: keep it simple, self-contained, use this specific tool.</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
  <div class="font-bold text-violet-600 dark:text-violet-400 mb-1">Theme & Narrative</div>
  <div class="opacity-80">"The game's theme is 'A Human-Centered AI Future' — our hero is defending humanity against AI-era threats."</div>
  <div class="text-xs opacity-50 mt-2">Gives the AI a story to build around — not just mechanics, but meaning.</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
  <div class="font-bold text-green-600 dark:text-green-400 mb-1">Game Style (Pick One)</div>
  <div class="opacity-80">Four options: Breakout, Space Invaders, Frogger, Flappy Bird — each described in one sentence.</div>
  <div class="text-xs opacity-50 mt-2">Constrains the genre so the AI has a clear mechanical blueprint.</div>
</div>

</div>

<!--
Walk through the first three sections. Context sets the technical constraints — single file, specific library, beginner-level. Theme gives the AI narrative direction — not just "make a game" but a game with meaning. The game style pick is the single most important creative decision they'll make — it determines the entire mechanical structure.
-->

---

# The Prompt: Content & Quality

<div class="space-y-4 mt-4 text-sm">

<div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
  <div class="font-bold text-amber-600 dark:text-amber-400 mb-1">Specific Content</div>
  <div class="opacity-80">Named enemies: Rogue Code, Deepfakes, Bias Bugs, Hallucinations... "Label them visibly."</div>
  <div class="text-xs opacity-50 mt-2">The AI won't guess what "AI threats" means — naming them gets specific, readable results.</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
  <div class="font-bold text-red-600 dark:text-red-400 mb-1">Feature List</div>
  <div class="opacity-80">Start screen, game over, score, lives, particles, retro aesthetic.</div>
  <div class="text-xs opacity-50 mt-2">A checklist the AI will try to hit — keeps the output complete and polished.</div>
</div>

</div>

<v-click>

<div class="mt-6 bg-blue-50 dark:bg-blue-900 rounded-lg p-4">

**The pattern:** Every section of the prompt has a job. Context constrains. Theme directs. Style defines mechanics. Content specifies. Features set the quality bar.

This is what makes a prompt "good" — not length, but **intentionality**.

</div>

</v-click>

<!--
The last two sections. Named enemies prevent vague, generic output — the AI needs concrete strings to render. The feature list is a quality checklist: without it, you might get a game that works but has no start screen or score display. Then the takeaway: every line in the prompt has a purpose. That's the difference between a wall of text and a blueprint.
-->

---

# Pick Your Game

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="bg-blue-50 dark:bg-blue-900 rounded-xl p-5 shadow-sm">
  <div class="text-2xl mb-2">1. Breakout / Arkanoid</div>
  <div class="text-sm opacity-80">Control a paddle at the bottom. Bounce a ball to smash rows of threat-bricks.</div>
  <div class="text-xs opacity-50 mt-2">Classic, satisfying. Good if you like aiming and angles.</div>
</div>

<div class="bg-violet-50 dark:bg-violet-900 rounded-xl p-5 shadow-sm">
  <div class="text-2xl mb-2">2. Space Invaders</div>
  <div class="text-sm opacity-80">You're a defender at the bottom, shooting upward at rows of descending threats.</div>
  <div class="text-xs opacity-50 mt-2">Iconic. Enemies march closer. Tension builds.</div>
</div>

<div class="bg-green-50 dark:bg-green-900 rounded-xl p-5 shadow-sm">
  <div class="text-2xl mb-2">3. Frogger</div>
  <div class="text-sm opacity-80">Guide a human safely across lanes of scrolling AI threats to reach safety.</div>
  <div class="text-xs opacity-50 mt-2">Timing-based. Dodge and weave. Surprisingly strategic.</div>
</div>

<div class="bg-amber-50 dark:bg-amber-900 rounded-xl p-5 shadow-sm">
  <div class="text-2xl mb-2">4. Flappy Bird</div>
  <div class="text-sm opacity-80">Tap to keep your hero aloft, flying through gaps between AI threat-walls.</div>
  <div class="text-xs opacity-50 mt-2">Simple controls, brutally hard. One-tap gameplay.</div>
</div>

</div>

<div class="mt-4 text-center text-sm opacity-60">

Pick whichever sounds fun. You can also freestyle: "I pick #2" or "Make me a Space Invaders-style game" — whatever feels natural.

</div>

<!--
Give them a minute to decide. There's no wrong choice. All four produce great results. If someone can't decide, tell them Breakout or Space Invaders tend to be the most visually impressive. If someone wants to do something completely different — a different genre — that's fine too, but suggest they start with one of these and modify later.
-->

---

# The Full Prompt

<div class="bg-blue-50 dark:bg-blue-900 p-4 rounded-lg mt-2 text-xs leading-relaxed select-all cursor-pointer" title="Click to copy">

**Prompt:**

I have no coding experience. I want you to build me a complete browser game in a single HTML file using the p5.js library (loaded from CDN). The game's theme is "A Human-Centered AI Future" — our hero is defending humanity against AI-era threats.

I'd like to make a: [PICK ONE]
1. Breakout/Arkanoid — I control a paddle at the bottom and bounce a ball to smash rows of threat-bricks
2. Space Invaders — I'm a defender at the bottom shooting upward at rows of descending threats
3. Frogger — I guide a human safely across lanes of scrolling AI threats to reach safety
4. Flappy Bird — I tap to keep my hero aloft, flying through gaps between AI threat-walls

The enemies/obstacles should be AI-era threats like: Rogue Code, Network Outages, Creative Outsourcing, Data Breaches, Bias Bugs, Deepfakes, Hallucinations, Surveillance, Misinformation, and Algorithmic Bias. Label them visibly so the player can read what they're smashing/dodging.

Include: A start screen with the title "A Human-Centered AI Future" and simple instructions; A game over screen with the final score and "press enter to retry"; A score counter and lives display; Fun particle effects when threats are destroyed; A retro pixel-art aesthetic with a dark background and bright colors.

</div>

<div class="mt-3 text-sm">

**Before you paste:** delete the game options you *don't* want, or just add "I pick #2" at the end.

</div>

<!--
This is the moment. Have them copy the full prompt, make their game choice, and paste it into Claude. While Claude generates, remind them: this is one prompt. It's detailed because we designed it to be. Every piece we just walked through is in there. Give Claude a minute to generate — the response will be long. That's normal.
-->

---

# Setup: Phoenix Code

<v-clicks>

### Step 1 — Open Phoenix Code
Go to **phcode.dev** — click **"Start Coding"** (no account needed)

### Step 2 — Create a new file
**File → New** (or Ctrl/Cmd + N). Save it as **game.html**

### Step 3 — Paste your code
Copy the entire code block from Claude and paste it into **game.html**

### Step 4 — Live Preview
Click the **lightning bolt icon** (or **File → Live Preview**) to see your game running

<div class="mt-4 bg-amber-50 dark:bg-amber-900 p-3 rounded-lg text-sm">

**Why Phoenix Code?** It gives you syntax highlighting, line numbers, and instant live preview — much better than pasting into a plain text file. And it's free with no account required.

</div>

</v-clicks>

<!--
If students already have Phoenix Code from Day 1, they can skip to Step 2. No GitHub Import needed this time — we're just creating a single file. Make sure everyone saves as game.html, not game.txt. The Live Preview should show the game running immediately. Walk the room and help anyone whose preview isn't loading. Common issue: if they accidentally copied only part of the code block from Claude, the file will be incomplete. Have them go back and copy the whole thing.
-->

---
layout: center
class: text-center
---

# Play Your Game

### Take 2 minutes. Try it out.

<div class="text-sm opacity-60 mt-4">Does it work? Is it fun? What would you change?</div>

<!--
Let them play. This is the payoff moment. Walk the room, look at screens, react to what they built. Some games will work perfectly. Some will have bugs — enemies off-screen, collisions not detecting, score not updating. That's fine. Let them experience it before we start fixing things. After 2 minutes, bring them back together.
-->

---

# Review Together

<v-clicks>

### What did you get?

- Does the start screen show up?
- Can you actually play it?
- Do the enemy labels appear?
- Does game over work?

### What's different about everyone's?

Even with the same prompt, Claude generates **different code each time**. Different layouts, different colors, different interpretations. Your game is already unique.

### If it's broken:
That's data, not failure. We'll fix it.

</v-clicks>

<!--
Quick group check-in. Show of hands: whose game works? Whose is partially broken? Whose won't load at all? Normalize all of these outcomes. The point isn't that AI gives you perfect code — it's that you now have something to work with. A broken game is closer to a working game than no game at all. If anyone's is completely broken, have them tell Claude: "The game won't load. Here's the error I see in the console." Or just ask Claude to try again.
-->

---
layout: center
class: text-center
---

# First Iteration

### Make the code readable

<div class="text-sm opacity-60 mt-4">Before we change anything, let's understand what we have</div>

---

# Add Section Comments

Send this follow-up to Claude:

<div class="bg-green-50 dark:bg-green-900 p-5 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to copy">

**Prompt:**

Add clear comments throughout the code labeling each major section — like // GAME SETTINGS, // PLAYER CONTROLS, // ENEMY BEHAVIOR, // COLLISION DETECTION, // SCORE AND LIVES, // PARTICLE EFFECTS, // SCREENS (start/game over). Keep the game exactly the same, just add the comments.

</div>

<v-clicks>

<div class="mt-4 text-sm">

**Then:** Copy the updated code and replace everything in your **game.html** file in Phoenix Code.

Compare: scroll through the code now vs. before. Notice how much easier it is to find things?

</div>

</v-clicks>

<!--
This is a deliberately low-risk first iteration. Nothing changes about the game — it just becomes readable. When they paste the new version, they should see the same game in Live Preview but much clearer code in the editor. This sets up the next step: if you can find a section, you can change a value in it. Walk the room and make sure everyone has commented code before moving on.
-->

---
layout: center
class: text-center
---

# Manual Edit Challenge

### No AI allowed for this one

<div class="text-sm opacity-60 mt-4">Find a value in the code. Change it yourself. See what happens.</div>

---

# Find It, Change It

Use **Ctrl+F** (or **Cmd+F** on Mac) to search in Phoenix Code.

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="bg-blue-50 dark:bg-blue-900 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2">Easy</div>
  <div class="text-sm opacity-80">
    Search for a color value (like <code>#ff</code> or <code>rgb</code>) and change it<br/>
    <span class="text-xs opacity-50">Watch the game's appearance shift</span>
  </div>
</div>

<div class="bg-green-50 dark:bg-green-900 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2">Medium</div>
  <div class="text-sm opacity-80">
    Find the variable that controls game speed and double it<br/>
    <span class="text-xs opacity-50">Look near GAME SETTINGS or ENEMY BEHAVIOR</span>
  </div>
</div>

<div class="bg-amber-50 dark:bg-amber-900 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2">Spicy</div>
  <div class="text-sm opacity-80">
    Find the lives count and change it to 99<br/>
    <span class="text-xs opacity-50">Search for "lives" near GAME SETTINGS</span>
  </div>
</div>

<div class="bg-red-50 dark:bg-red-900 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2">Boss Mode</div>
  <div class="text-sm opacity-80">
    Find an enemy label string and change it to something custom<br/>
    <span class="text-xs opacity-50">Search for "Deepfakes" or "Rogue Code"</span>
  </div>
</div>

</div>

<div class="mt-4 text-sm opacity-70 text-center">

**Live Preview updates instantly.** Change a number, save, see the result. That's Level 2 in action.

</div>

<!--
This is the key pedagogical moment. They're editing code — real code — by hand. No AI. They searched for a variable, changed a value, and saw the result. That's the bridge between "I can only prompt" and "I can also tinker." Some will change a color and get excited. Some will break something — which is also great, because they can Ctrl+Z to undo. Give them 3-5 minutes here. The section comments from the last step make this possible.
-->

---
layout: center
class: text-center
---

# Vibe It

### 25 Minutes — Make It Yours

<div class="text-sm opacity-60 mt-4">Keep the conversation going with Claude. Paste updates into Phoenix Code.</div>

---

# Iteration Ideas

<div class="grid grid-cols-3 gap-4 mt-4 text-sm">

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2 text-blue-600 dark:text-blue-400">Gameplay</div>
  <div class="opacity-80 space-y-1">
    <div>"Make enemies get faster each level"</div>
    <div>"Add a boss enemy every 5th wave"</div>
    <div>"Add power-ups that drop randomly"</div>
    <div>"Make the paddle/player wider when I get a power-up"</div>
  </div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2 text-green-600 dark:text-green-400">Visual</div>
  <div class="opacity-80 space-y-1">
    <div>"Make explosions bigger and more colorful"</div>
    <div>"Add a scrolling star field background"</div>
    <div>"Make the player character flash when hit"</div>
    <div>"Add screen shake when you lose a life"</div>
  </div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 shadow-sm">
  <div class="font-bold mb-2 text-amber-600 dark:text-amber-400">Polish</div>
  <div class="opacity-80 space-y-1">
    <div>"Add a high score that persists"</div>
    <div>"Add sound effects" (experimental!)</div>
    <div>"Show a combo counter for rapid kills"</div>
    <div>"Add a pause button"</div>
  </div>
</div>

</div>

<div class="mt-4 text-sm opacity-60 text-center">

Or describe something completely different: *"Turn the enemies into falling math equations I have to solve."*

</div>

<!--
Let them go. Walk the room. Help people who are stuck by asking "what do you wish your game did?" and helping them turn that into a prompt. Remind them of the cycle: describe, generate, review, refine. If something breaks, tell Claude what went wrong. If it's really broken, they can always paste their last working version back in. Encourage wild ideas — the point is to explore what's possible through conversation.
-->

---

# When It Breaks (It Will)

<v-clicks>

### Debugging by conversation:

1. **Describe the symptom, not the fix**
   *"Enemies fly off the left side of the screen and never come back"*

2. **Reference the sections**
   *"I think the issue is in the ENEMY BEHAVIOR section — they're not bouncing at the edges"*

3. **Ask for a targeted fix**
   *"Don't rewrite the whole game — just fix the enemy movement"*

4. **Nuclear option: start fresh**
   *"The game is too broken to fix. Generate a new version from scratch with these changes: ..."*

</v-clicks>

<!--
Games break in more interesting ways than websites. Enemies that teleport. Scores that go negative. Collisions that don't detect. Normalize all of this. The debugging prompts matter: "fix the enemy movement" is better than "it's broken." Referencing section comments gives Claude a specific place to look. If something is truly unfixable after 2-3 tries, starting over is fine — that's not failure, it's a fresh conversation with better context.
-->

---

# Discussion

<v-clicks>

- How did building a **game** feel different from building a **website**?
- When you edited code by hand — what was that like?
- Did you read the code, or just the game?
- What was the hardest part to describe to AI?
- Did anyone's game do something **unexpected** that turned out cool?

</v-clicks>

<!--
Open discussion. The game-vs-website question usually surfaces interesting insights: games have state, logic, timing — things that are harder to describe in words. The manual edit question gets at the Level 2/3 boundary. "Hardest to describe" reveals the limits of natural language for programming. And unexpected results are the best stories — sometimes bugs become features.
-->

---

# What You Practiced Today

<v-clicks>

1. **Reading a complex prompt** — understanding what each part does before using it
2. **The one-big-prompt approach** — front-loading detail, then iterating
3. **Code navigation** — using comments and search to find what matters
4. **Manual editing** — changing values directly, no AI needed
5. **Conversational debugging** — describing symptoms, not guessing at fixes
6. **Creative iteration** — making something generic into something personal

</v-clicks>

<v-click>

<div class="mt-6 text-center text-lg">

Last time: *"I can describe a website and AI builds it."*

Today: *"I can describe a game, understand its structure, and shape it myself."*

</div>

</v-click>

<!--
The progression from Day 1 to Day 2 is real. They went from "paste and preview" to "paste, read, find, edit, iterate." They're not programmers — but they can navigate code, find the parts that matter, and make targeted changes. That's a genuinely useful skill regardless of whether they ever write code from scratch.
-->

---

# Keep Going

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### Tools from today
- **Claude.ai** — AI assistant
- **Phoenix Code** — phcode.dev (free, no account)
- **p5.js** — p5js.org (creative coding library)
- **p5.js Web Editor** — editor.p5js.org (alternative to Phoenix)

### What to try next
- Remix your game with a completely different theme
- Build a game from scratch with your own prompt
- Try the **p5.js examples gallery** for inspiration
- Explore **Scratch** (scratch.mit.edu) for visual game building

</div>
<div>

### The prompt pattern (games edition)
1. Set context + constraints (single file, library)
2. Define the theme and narrative
3. Choose the game mechanics
4. Name specific content (enemies, labels)
5. List required features (screens, scoring)
6. Iterate: comments → manual edits → vibed changes

### Your guidelines still apply
Review. Understand. Make it yours before sharing it.

</div>
</div>

<!--
Leave resources up. p5.js Web Editor is a great alternative to Phoenix Code specifically for p5.js projects. Scratch is a good suggestion for anyone who wants to explore game design more visually. The prompt pattern summary is the real takeaway — they can use this structure to generate any kind of game.
-->

---
layout: center
class: text-center
---

# Thank You

**Dr. Curt Rode** · TCU

<div class="mt-8 opacity-60">

Today's slides and prompt are available at:

[curtrode.github.io/general_workshops/games/slides](https://curtrode.github.io/general_workshops/games/slides/)

</div>
