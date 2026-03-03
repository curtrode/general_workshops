---
theme: apple-basic
title: 'Vibe Coding: Making Things with AI'
info: |
  A 90-minute hands-on workshop for a general TCU audience.
  No coding experience required.
author: Dr. Curt Rode
transition: fade-out
mdc: true
---

<script setup>
import { onMounted } from 'vue'
onMounted(() => {
  document.addEventListener('click', (e) => {
    const el = e.target.closest('.select-all')
    if (!el) return
    const text = el.innerText.replace(/^Prompt:\s*/i, '').trim()
    navigator.clipboard.writeText(text).then(() => {
      const orig = el.style.outline
      el.style.outline = '2px solid #22c55e'
      setTimeout(() => { el.style.outline = orig }, 600)
    })
  })
})
</script>

# Vibe Coding
## Making Things with AI

Dr. Curt Rode · TCU

<div class="abs-br m-6 text-sm opacity-50">
90-Minute Hands-On Workshop · No Coding Experience Required
</div>

<!--
Welcome everyone. This is a hands-on workshop — you'll be making things today, not just watching. No coding background needed. If you have a laptop and an internet connection, you're ready.
-->

---
layout: center
---

# What We're Doing Today

| Time | Activity |
|------|----------|
| 15 min | What is vibe coding + the AI coding spectrum |
| 5 min | Good prompts vs. bad prompts |
| 5 min | Write your personal AI guidelines |
| 5 min | Set up CodePen |
| 25 min | Codealong: duck → animation → game |
| 15 min | Free experimentation |
| 10 min | Scraping demo + ethics of AI-generated code |
| 10 min | Wrap-up and discussion |

<!--
Quick overview so everyone knows the arc. First third is concepts, middle third is hands-on together, last third is you experimenting on your own. We'll end with a discussion.
-->

---

# What Is Vibe Coding?

<img src="/karpathy_headshot.jpg" class="absolute top-8 right-12 w-36 rounded-full shadow-lg opacity-90" />

<v-clicks>

The term comes from **Andrej Karpathy** (OpenAI co-founder):

> "You just see stuff, say stuff, run stuff, and copy-paste stuff, and it mostly works."

**Translation:** You describe what you want in plain language. AI writes the code. You guide the process.

This is **not** about becoming a programmer.

It's about using AI as a **creative tool** — like picking up a paintbrush without going to art school.

</v-clicks>

<!--
Karpathy coined this in early 2025. It went viral because it captured something people were already doing — describing things to AI and getting working code back. The key insight: you don't have to understand every line of code to build something real. But you DO have to stay engaged with what's happening.
-->

---

# Who Is This For?

<v-clicks>

- You **don't** need to know how to code
- You **do** need curiosity and a willingness to experiment
- If something breaks, that's part of the process — not a failure
- Today's goal: **make something that didn't exist an hour ago**

</v-clicks>

<!--
I want to be explicit about this because some people hear "coding workshop" and assume it's not for them. If you can describe what you want in a sentence, you can do this.
-->

---
layout: two-cols
layoutClass: gap-8
---

# The AI Coding Spectrum

Four levels of AI involvement — not a ladder, a **spectrum**.

The right level depends on:
- The task
- Your familiarity
- What you're trying to learn

We'll use **one example** to show all four levels.

::right::

<div class="mt-12">

### The Example

You want **a duck riding a skateboard** on your screen.

How much does AI do?

</div>

<!--
I'm reframing this from my classroom version. Instead of a dark mode toggle — which requires web dev context — we'll use something everyone can picture: a duck on a skateboard. Each level shows a different relationship between you and the AI.
-->

---

# The Four Levels

<v-clicks>

### 1. Fundamentals First
You write code yourself. You ask AI: *"How do I draw a circle in p5.js?"*
The AI is a **tutor**.

### 2. Collaborative
You sketch the approach: *"I need a yellow duck made of basic shapes on a gray road."*
The AI **implements your design**.

### 3. Vibe Coding ← **We're here today**
You describe the outcome: *"Make me a duck riding a skateboard."*
The AI **generates everything**. You guide and refine.

### 4. Full Automation
You paste code, it runs, you don't look at it.
You've **left the driver's seat**. 🚫

</v-clicks>

<!--
Level 3 is where we'll spend the workshop. It's the sweet spot for non-coders: you're describing outcomes, the AI is doing the implementation, but you're actively involved in reviewing and refining. Level 4 is where things go wrong — you lose the ability to understand, explain, or steer what's being built.
-->

---

# The Spectrum Is Not a Ladder

<v-clicks>

Moving "up" is not always better.

- A professional developer might use **Level 1** for critical code and **Level 3** for a quick prototype
- A student learning might stay at **Level 2** to build understanding
- A workshop participant (you!) can start at **Level 3** and dip into **Level 2** when curious

**The key question at every level:**

> Can I explain what this code does?

</v-clicks>

<!--
This is important because people tend to think the "most AI" option is the best option. It's not. It depends on context. Today we're vibe coding intentionally — but the goal is always to stay engaged enough that you could explain what your code does to someone else.
-->

---

# Good Prompts vs. Bad Prompts

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### ❌ Bad Prompt
*"Make me something cool with code"*

- Vague
- No constraints
- AI has to guess everything

</div>
<div>

### ✅ Good Prompt
*"Write p5.js code that draws a yellow duck riding a skateboard on a gray road against a light blue sky. Use simple shapes — circles, rectangles, triangles."*

- Specific outcome
- Named technology
- Visual constraints

</div>
</div>

<!--
The difference is night and day. The bad prompt could produce literally anything. The good prompt gives the AI enough to work with while leaving room for creative interpretation. Notice: you don't need to know how p5.js works to write the good prompt. You just need to describe what you want clearly.
-->

---

# What Makes a Good Prompt?

<v-clicks>

1. **Describe the outcome**, not the process
   - "Draw a duck" not "use a for loop to render pixels"

2. **Be specific about what matters**
   - Colors, shapes, behavior, layout

3. **Name your constraints**
   - "Use p5.js" · "Simple shapes only" · "Fit on one screen"

4. **Iterate with small follow-ups**
   - Don't rewrite the whole prompt — ask for one change at a time

</v-clicks>

<!--
This is the core skill of vibe coding. You're not learning syntax — you're learning to communicate clearly with an AI. These same principles work whether you're generating code, writing emails, or creating images.
-->

---
layout: center
---

# Writing Your Guidelines

Before you start prompting, decide your rules.

Think of it like **writing instructions for your AI before you begin** — a personal set of standards.

<div class="mt-8 text-lg">

**Take 2 minutes.** Write 3–5 personal guidelines for how you'll use AI today.

</div>

<div class="mt-4 opacity-70 text-sm">

Examples:
- *"I'll read the code before I run it."*
- *"If I don't understand something, I'll ask the AI to explain it."*
- *"I won't paste output I can't describe in my own words."*
- *"I'll try changing one thing manually before asking AI to change it."*

</div>

<!--
This maps to the CLAUDE.md concept from professional AI-assisted development. Developers write a file of instructions that the AI reads before it starts working. You're doing the same thing — setting your own standards. In browser-based tools like ChatGPT or Claude, you'd put this in "custom instructions" or as your first message. The point: decide your rules BEFORE you start, not after. Give them 2 full minutes. Play music if you want.
-->

---

# Setup: Claude

<img src="/claude-logo.svg" class="absolute top-8 right-12 w-48 opacity-80" />

<v-clicks>

### Step 1 — Go to claude.ai
Open **claude.ai** in your browser

### Step 2 — Create a free account
Click **"Sign up"** — you can use Google, email, or Apple

### Step 3 — Start a conversation
You should see a chat interface. Type anything to test it.

<div class="mt-4 text-sm opacity-70">

Already have ChatGPT, Gemini, or another AI tool? That works too — use whatever you're comfortable with.

</div>

</v-clicks>

<!--
Give them a couple minutes to get signed up. Some will already have accounts. Common issues: institutional email blocks, needing to verify email, phone verification. If someone can't get Claude working, ChatGPT or Gemini are fine alternatives. The prompts we'll use work with any major AI chat tool.
-->

---

# Setup: CodePen

<img src="/codepen-logo.svg" class="absolute top-8 right-12 w-36 opacity-80" />

<v-clicks>

### Step 1 — Create a free account
Go to **codepen.io** → Sign Up (free)

### Step 2 — Fork the starter pen
Open this link:

<div class="text-2xl font-mono bg-gray-100 dark:bg-gray-800 p-4 rounded my-4 text-center">

[codepen.io/curtrode/pen/yyaYLeV](https://codepen.io/curtrode/pen/yyaYLeV)

</div>

Click **"Fork"** (bottom-right) to make your own copy.

### Step 3 — You're ready
The starter pen has **p5.js already loaded**. You'll paste code into the **JS panel** (bottom-left).

</v-clicks>

<!--
The starter pen eliminates the configuration step. p5.js is added as an external library in the pen's JS settings — attendees don't need to know about CDNs or script tags. They fork it, and they're ready to paste code. Walk the room and make sure everyone has their pen forked. Common issues: people not signed in (can't fork), people pasting into the wrong panel (must be JS, not HTML or CSS).
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 1: Duck on a Skateboard

<div class="text-sm opacity-60 mt-4">Open your AI tool — Claude.ai, ChatGPT, Gemini, or whatever you have</div>

<!--
Transition to the hands-on portion. I'll drive the AI on screen. Everyone follows along.
-->

---

# Step 1: The Prompt

I'm typing this into the AI on screen. You can follow along with your own AI tool.

<div class="bg-blue-50 dark:bg-blue-900 p-6 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to select, then copy">

**Prompt:**

Write p5.js code that draws a duck riding a skateboard. Use simple shapes — circles for the body and head, a triangle for the beak, rectangles for the skateboard. Make the background a light blue sky with a gray ground at the bottom. The duck should be yellow with an orange beak. The skateboard should be red with dark gray wheels.

</div>

<div class="mt-4 text-sm opacity-70">

After AI responds → copy the code → paste into your CodePen JS panel → see what appears

</div>

<!--
Read the prompt aloud. Emphasize: we didn't write any code. We described a picture. Now let's see what the AI gives us. Paste into CodePen, see the result. It won't be perfect — and that's the point. Ask the room: "What do you think? What would you change?"
-->

---

# Step 1: What We Got

<div class="grid grid-cols-2 gap-8">
<div>

### Review together:
- Does it look like a duck?
- Is it on a skateboard?
- Are the colors right?
- What would you change?

### The process:
1. We **described** what we wanted
2. AI **generated** the code
3. We **reviewed** the result
4. Now we **refine**

</div>
<div class="flex items-center justify-center">

<div class="text-8xl">🛹🦆</div>

<div class="text-sm opacity-50 mt-2">(Your actual result will appear in CodePen)</div>

</div>
</div>

<!--
Take a moment to look at the code in the JS panel. You don't need to understand every line, but notice the structure: there's a setup() function and a draw() function. setup runs once, draw runs over and over. That's all of p5.js in a nutshell. Now let's make it better.
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 2: Refinements

<div class="text-sm opacity-60 mt-4">Small, specific follow-up prompts beat rewriting everything</div>

---

# Step 2: Iterative Refinement

Send these **one at a time** to your AI. Paste each updated version into CodePen.

<div class="space-y-4 mt-4">

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 1:** *"Make the wheels spin — rotate them as if the skateboard is moving."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 2:** *"Add a little bobbing motion so the duck moves up and down slightly as it rides."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 3:** *"Add a small blue helmet on the duck's head."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 4:** *"Add two or three clouds that slowly drift across the sky in the background."*

</div>

</div>

<!--
Each prompt is one change. This is key — if you ask for five things at once and something breaks, you don't know which change caused it. One at a time. Paste, check, move on. If something breaks, tell the AI what went wrong. "The wheels aren't spinning" or "the duck disappeared" — that's your debugging prompt. Give them time here. Walk the room. Some people will be ahead, some behind. That's fine.
-->

---

# What's Happening Here

<v-clicks>

- Each prompt is **small and specific**
- You **see the result** after each change
- If something breaks, you tell the AI: *"The duck disappeared after the last change. Here's my current code: [paste]. Fix it."*
- **Troubleshooting is part of the process, not a failure**

This cycle is the core of vibe coding:

### Describe → Generate → Review → Refine → Repeat

</v-clicks>

<!--
Reinforce: this iterative loop is the skill. It's not about getting perfect code on the first try. Professional developers using AI work the same way — describe, generate, review, refine. The only difference is they can read the code more deeply. But the process is identical.
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 3: Make It a Game

<div class="text-sm opacity-60 mt-4">One prompt. Big transformation.</div>

---

# Step 3: The Game Prompt

This is a bigger prompt. I'll type it on screen — watch what happens.

<div class="bg-purple-50 dark:bg-purple-900 p-5 rounded-lg mt-4 select-all cursor-pointer" title="Click to select, then copy">

**Prompt:**

Turn this into a game. The duck should move forward automatically (scroll the background from right to left). Add obstacles — rocks or traffic cones — that scroll in from the right side. The player presses the spacebar to make the duck jump over obstacles. Add a score counter in the top-left corner that goes up by 1 each time an obstacle is passed. If the duck hits an obstacle, show "Game Over" and the final score. Press R to restart. Keep the duck, skateboard, and visual style from before.

</div>

<div class="mt-4 text-sm opacity-70">

Copy the full code AI gives you → replace everything in your CodePen JS panel → test it

</div>

<!--
This is the "wow" moment. One prompt takes us from a static drawing to a playable game. Don't rush this — let the room react. After pasting, try playing it on screen. It might have bugs. That's fine. If it does, debug live: "The jump isn't working" or "obstacles are moving too fast." Model the process.
-->

---

# What Just Happened?

<v-clicks>

We went from **a drawing** → **an animation** → **a playable game**

Lines of code we wrote by hand: **zero**

Prompts we wrote: **~6**

The AI did the coding.
**We did the thinking.**

- We decided what to build
- We decided what to change
- We decided when something was wrong
- We decided when it was done

</v-clicks>

<!--
This is the key takeaway slide. Pause here. Let it sink in. The prompts were the creative work. Deciding what the duck looks like, how it moves, what makes it a game — those are design decisions. The AI translated them into code. Ask the room: "At any point did you feel like you weren't in control?"
-->

---
layout: center
---

# Free Experimentation
## 20 Minutes — Make Something Your Own

<div class="text-sm opacity-60">Use your own AI tool. Ask me if you get stuck.</div>

---

# Challenge Ideas

Pick one, combine a few, or invent your own:

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Modify the game
- Change the duck to a different animal
- Add power-ups (speed boost, shield)
- Add a high-score tracker
- Make obstacles move faster over time
- Add a second player

</div>
<div>

### Start fresh
- Bouncing ball that changes color on click
- Fireworks that launch on mouse click
- Pong game with two paddles
- Drawing app (mouse draws, keyboard changes color)
- Falling snowflakes / rain simulation

</div>
</div>

<div class="mt-6 text-sm opacity-70">

**Stuck?** Try: *"I want to [describe what you see in your head]. Write p5.js code for it."*

</div>

<!--
Let them go. Walk the room. Help people who are stuck by asking "what do you want it to do?" and helping them turn that into a prompt. Don't write prompts for them — coach them to describe what they see. Some people will go deep on the duck game. Others will start fresh. Both are fine. If someone's AI gives them broken code, help them debug by pasting the error message back to the AI.
-->

---

# When Things Break

<v-clicks>

This **will** happen. It's not a failure — it's the process.

### Your debugging toolkit:

1. **Describe the symptom:** *"The duck jumps but doesn't come back down."*

2. **Share the error:** Copy any red text from the console → paste to AI

3. **Share your code:** *"Here's my current code: [paste]. The score counter isn't showing up. Fix it."*

4. **Start smaller:** If it's totally broken, ask AI: *"Simplify this — just show me a duck that jumps when I press spacebar."*

</v-clicks>

<!--
Normalize this. Every professional developer's workflow includes things breaking. The difference between frustration and progress is knowing how to describe the problem. That's a skill you're practicing right now.
-->

---

# Discussion

<v-clicks>

- What **surprised** you?
- What made you **uncomfortable**?
- Did you look at the code at all — or just the result?
- How is this different from using a template or a tool like Canva?
- Would you trust AI-generated code for something important?

</v-clicks>

<!--
Open it up. These questions don't have right answers. Some people will be excited, some will be skeptical. Both reactions are valid. If someone says "I never looked at the code" — that's honest, and it's worth exploring. If someone says "I don't trust it" — ask why, and what it would take to build trust. These are the questions that matter more than the duck.
-->

---
layout: center
class: text-center
---

# One More Demo

### Vibe Coding Beyond Visuals: Python + Real Data

<div class="text-sm opacity-60 mt-4">What happens when the code interacts with the real world?</div>

<!--
Transition: everything we've built so far runs in a sandbox — your CodePen, your browser, your screen. But vibe coding can produce code that reaches out into the world. Let's see what that looks like — and why it matters. We'll vibe-code three short Python scripts live.
-->

---

# Demo 1: Who Lets You In?

Not every server welcomes your code. Let's find out who says yes and who says no.

<div class="bg-blue-50 dark:bg-blue-900 p-6 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to select, then copy">

**Prompt:**

Write Python that uses the requests library to check if two URLs are accessible. Print the status code for each. Use Open-Meteo's forecast API and a LinkedIn profile page.

</div>

<div class="mt-4 text-sm opacity-70">

Watch the status codes. One server says **200** (welcome). The other says **999** (go away).

</div>

<!--
Run this live. The Open-Meteo API returns 200 — it's a free public API that expects automated requests. LinkedIn returns 999 — a custom "not even a real HTTP code" rejection. They invented their own status code just to block scrapers. The AI wrote code for both without distinguishing between them. That's the point: the AI doesn't know (or care) whether a server wants to be accessed programmatically. Ask the room: "Did the AI warn us that LinkedIn might block us?" No. It just wrote the code.
-->

---

# What's a Status Code?

<v-clicks>

When your code contacts a server, the server responds with a number:

| Code | Meaning | Translation |
|------|---------|-------------|
| **200** | OK | "Here's what you asked for" |
| **403** | Forbidden | "I know what you want, but **no**" |
| **404** | Not Found | "That doesn't exist" |
| **429** | Too Many Requests | "Slow down" |
| **999** | ??? | LinkedIn made this up — "we **really** don't want you here" |

The AI wrote code that **reached out to two servers**. One welcomed us. One rejected us.

**The AI didn't warn us about the difference.**

</v-clicks>

<!--
Keep this brief — just enough so the status codes make sense. The point isn't to teach HTTP. The point is: your code went out into the world, knocked on two doors, and got two different answers. The AI treated both requests identically. The judgment about which servers are appropriate to contact? That's yours.
-->

---

# Demo 2: Fetch Weather Data

Now let's get something useful. Fort Worth's 7-day forecast — from a server that **wants** us to use it.

<div class="bg-blue-50 dark:bg-blue-900 p-6 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to select, then copy">

**Prompt:**

Write Python that fetches the 7-day weather forecast for Fort Worth, TX from the Open-Meteo API. Get the date, high temp, and low temp for each day. Save the results to a CSV file called forecast.csv.

</div>

<div class="mt-4 text-sm opacity-70">

This code reaches across the internet, pulls live data, and saves it to your machine.

</div>

<!--
Run this live. Show the printed forecast, then open forecast.csv. This is a legitimate use of a public API — no API key, no auth, no terms of service violation. Open-Meteo is designed for exactly this kind of use. But emphasize: this code left your computer, contacted a server in Europe, and pulled data back. The AI made that happen in seconds. How do you know this server is okay to contact? Because you checked — not because the AI told you.
-->

---

# Demo 3: Analyze the Data

Now the data stays local. Let's ask questions about it.

<div class="bg-blue-50 dark:bg-blue-900 p-6 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to select, then copy">

**Prompt:**

Write Python that loads forecast.csv with pandas. It has columns: date, high_f, low_f. Print the warmest day, the coolest night, and the average high temperature for the week.

</div>

<div class="mt-4 text-sm opacity-70">

This code **never leaves your machine**. It reads a local file and does math.

</div>

<!--
Run this live. The output is simple and satisfying — warmest day, coolest night, average high. Point out the contrast: Demo 2 reached across the internet. Demo 3 stayed entirely local. Both were vibe-coded. Both worked. But they have very different risk profiles. One touches someone else's server. The other only touches your own files. That distinction matters.
-->

---

# Wait — What Did We Just Do?

<v-clicks>

Three scripts. All vibe-coded. Very different risk profiles.

| Script | What it did | Where it reached |
|--------|------------|-----------------|
| Access check | Contacted two servers | Out to the internet |
| Fetch weather | Downloaded live data | Out to an API, saved locally |
| Analyze forecast | Read a local file, did math | **Never left your machine** |

### The AI treated all three the same.

It didn't warn us that LinkedIn blocks scripts. It didn't check if Open-Meteo allows automated access. It didn't distinguish between code that stays local and code that reaches out.

**That judgment is yours.**

</v-clicks>

<!--
This is the pivot. We've spent the whole workshop celebrating what AI can build. Now we're asking: just because AI can write it, should you run it? The duck game was harmless — it ran locally in your browser. The access check knocked on a door that said "go away." The weather fetch worked because we chose a server that welcomes automated access. The AI didn't make any of those distinctions for us.
-->

---

# The Ethics of Automated Access

<v-clicks>

### It's not always wrong — but it's never simple.

**Legitimate uses:**
- Public APIs designed for programmatic access (Open-Meteo, government data)
- Academic research with proper methodology
- Accessing data you have permission to use

**Where it gets risky:**
- Ignoring terms of service (like LinkedIn's)
- Scraping personal data (FERPA, GDPR, CCPA)
- Overloading someone's server (accidental DDoS)
- Accessing data behind authentication without authorization

**The AI won't warn you.** It writes the code. You decide if it's appropriate to run.

</v-clicks>

<!--
The AI treats all requests the same. "Fetch data from this URL" gets a technically correct answer regardless of whether it's ethical, legal, or wise. That's the fundamental limitation: AI is a capability amplifier, not a judgment engine. The judgment is yours. We saw this live — the AI happily wrote code to hit LinkedIn even though LinkedIn returned 999.
-->

---

# Broader Security: Building Apps Naively

<v-clicks>

Automated access is one example of a bigger pattern:

**AI-generated code can introduce real security risks.**

- **Hardcoded credentials** — AI might put API keys directly in the code
- **No input validation** — code that trusts everything a user types
- **SQL injection** — AI-written database queries that are exploitable
- **Over-permissive access** — code that asks for more permissions than it needs
- **No rate limiting** — your "quick script" accidentally hammers a server

### The pattern:
AI optimizes for **"does it work?"** — not **"is it safe?"**

</v-clicks>

<!--
This connects directly to Level 4 on the spectrum — full automation. If you paste AI code and run it without reading it, you're shipping security vulnerabilities you don't know about. This isn't hypothetical. Researchers have found that AI-generated code is more likely to contain certain categories of vulnerabilities than human-written code. Not because the AI is malicious, but because security requires the kind of contextual judgment AI doesn't have.
-->

---

# What Does "Driver's Seat" Mean Now?

<v-clicks>

For the duck game, "driver's seat" meant:
- Deciding what it looks like
- Knowing when something is broken
- Iterating toward your vision

For code that touches the real world, it also means:
- **Understanding what the code accesses** (network, files, APIs)
- **Checking legal and ethical boundaries** before running it
- **Reading the security-relevant parts** even if you skip the rest
- **Asking: "What's the worst this could do?"**

</v-clicks>

<!--
This is the deeper version of the spectrum conversation. When the stakes are a picture of a duck, understanding is a nice-to-have. When the stakes include other people's data, other people's servers, and legal liability, understanding is mandatory. That doesn't mean you can't use AI. It means the "driver's seat" gets more serious.
-->

---
layout: center
---

# The Big Question

<div class="text-3xl mt-8 leading-relaxed">

The question isn't *"Should I use AI?"*

It's **"How do I use AI while staying in the driver's seat?"**

</div>

<div class="mt-8 text-lg opacity-70">

And the harder version:

**"Am I still in the driver's seat when the code leaves my machine?"**

</div>

<!--
This is the closing message. We started with a duck and ended with real-world consequences. Both are vibe coding. The difference is stakes. Everything today — the spectrum, the guidelines, the prompting, the debugging, and now the ethics — is about answering this question honestly.
-->

---

# Your Takeaways

<v-clicks>

1. **Vibe coding** is describing outcomes and guiding AI — not writing syntax
2. **Good prompts** are specific, constrained, and iterate in small steps
3. **The spectrum** helps you choose how much AI involvement fits the task
4. **Your guidelines** keep you in the driver's seat
5. **Breaking things** is debugging, not failing
6. The **creative decisions** are still yours — AI is the tool, not the designer
7. **AI doesn't evaluate ethics or security** — that responsibility is yours

</v-clicks>

<!--
Quick recap. We added a seventh takeaway because the scraping demo changes the conversation. The first six are about capability. The seventh is about responsibility.
-->

---

# Keep Going

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### Tools from today
- **CodePen** — codepen.io (free)
- **p5.js** — p5js.org (creative coding library)
- **Claude.ai** / **ChatGPT** / **Gemini** — AI chat tools

### What to try next
- p5.js examples gallery: p5js.org/examples
- The Coding Train (YouTube) — creative coding tutorials
- Remix other people's pens on CodePen

</div>
<div>

### The prompt pattern
1. Describe what you want to see
2. Name the technology (p5.js)
3. Be specific about details that matter
4. Iterate with small follow-ups
5. Debug by describing symptoms

### Your guidelines
Keep them. Revisit them. Update them as you learn.

</div>
</div>

<!--
Leave these resources up while people pack up. The p5.js examples gallery and The Coding Train are both excellent for continuing to explore creative coding with AI assistance.
-->

---
layout: center
class: text-center
---

# Thank You

**Dr. Curt Rode** · TCU

<div class="mt-8 opacity-60">

Today's starter pen, prompts, and slides are available at:

[ repository link ]

</div>
