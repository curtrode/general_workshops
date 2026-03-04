---
theme: apple-basic
title: 'Vibe Coding: Web Development with AI'
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
## Web Development with AI

Dr. Curt Rode · TCU

<div class="abs-br m-6 text-sm opacity-50">
90-Minute Hands-On Workshop · No Coding Experience Required
</div>

<!--
Welcome everyone. This is a hands-on workshop — you'll be building a real website today, not just watching. No coding background needed. If you have a laptop and an internet connection, you're ready.
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
| 5 min | Set up Claude + CodePen |
| 25 min | Codealong: hero → sections → interactivity |
| 25 min | Free experimentation — make it yours |
| 10 min | Wrap-up and discussion |

<!--
Quick overview so everyone knows the arc. First third is concepts, middle third is hands-on together, last third is you experimenting on your own. We'll end with a discussion. By the time we're done, you'll have a personal portfolio website you built with AI.
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

- You **don't** need to know HTML, CSS, or JavaScript
- You **do** need curiosity and a willingness to experiment
- If something breaks, that's part of the process — not a failure
- Today's goal: **build a personal website that didn't exist an hour ago**

</v-clicks>

<!--
I want to be explicit about this because some people hear "web development workshop" and assume it's not for them. If you can describe what you want a website to look like, you can do this.
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

You want a **personal portfolio website**.

How much does AI do?

</div>

<!--
Instead of something abstract, we're using the exact thing you'll build today. Each level shows a different relationship between you and the AI.
-->

---

# The Four Levels

<v-clicks>

### 1. Fundamentals First
You write HTML/CSS yourself. You ask AI: *"How do I center a div?"*
The AI is a **tutor**.

### 2. Collaborative
You sketch the layout: *"I need a hero section with centered text, navy background, white text."*
The AI **implements your design**.

### 3. Vibe Coding ← **We're here today**
You describe the outcome: *"Build me a personal portfolio website."*
The AI **generates everything**. You guide and refine.

### 4. Full Automation
You deploy AI-generated code without reviewing it.
You've **left the driver's seat**. 🚫

</v-clicks>

<!--
Level 3 is where we'll spend the workshop. It's the sweet spot for non-coders: you're describing outcomes, the AI is doing the implementation, but you're actively involved in reviewing and refining. Level 4 is where things go wrong — you lose the ability to understand, explain, or steer what's being built. Deploying a website you've never reviewed? That's Level 4.
-->

---

# The Spectrum Is Not a Ladder

<v-clicks>

Moving "up" is not always better.

- A professional developer might use **Level 1** for critical code and **Level 3** for a quick prototype
- A student learning might stay at **Level 2** to build understanding
- A workshop participant (you!) can start at **Level 3** and dip into **Level 2** when curious

**The key question at every level:**

> Can I explain what this website does and why it looks the way it does?

</v-clicks>

<!--
This is important because people tend to think the "most AI" option is the best option. It's not. It depends on context. Today we're vibe coding intentionally — but the goal is always to stay engaged enough that you could explain your site to someone else.
-->

---

# Good Prompts vs. Bad Prompts

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### ❌ Bad Prompt
*"Make me a website"*

- Vague
- No constraints
- AI has to guess everything

</div>
<div>

### ✅ Good Prompt
*"Build a personal portfolio page with a navy blue hero section, my name in large white text, a subtitle that says 'Computer Science Student at TCU,' and a button that says 'See My Work.' Use clean, modern styling."*

- Specific outcome
- Color and layout details
- Clear content

</div>
</div>

<!--
The difference is night and day. The bad prompt could produce literally anything. The good prompt gives the AI enough to work with while leaving room for creative interpretation. Notice: you don't need to know HTML or CSS to write the good prompt. You just need to describe what you want clearly.
-->

---

# What Makes a Good Prompt?

<v-clicks>

1. **Describe the outcome**, not the process
   - "A hero section with my name" not "create a div with flexbox centering"

2. **Be specific about what matters**
   - Colors, layout, content, tone

3. **Name your constraints**
   - "Clean and modern" · "Mobile-friendly" · "Dark color scheme"

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
- *"I'll review what AI generates before moving on."*
- *"If I don't understand a design choice, I'll ask the AI to explain it."*
- *"I won't publish anything I can't describe in my own words."*
- *"I'll try changing one thing manually before asking AI to redo it."*

</div>

<!--
This maps to the CLAUDE.md concept from professional AI-assisted development. Developers write a file of instructions that the AI reads before it starts working. You're doing the same thing — setting your own standards. The point: decide your rules BEFORE you start, not after. Give them 2 full minutes.
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

Claude will **generate the HTML, CSS, and JavaScript** for your website as separate code blocks. You can also use ChatGPT or Gemini.

</div>

</v-clicks>

<!--
Give them a couple minutes to get signed up. Some will already have accounts. Common issues: institutional email blocks, needing to verify email, phone verification. If someone can't get Claude working, ChatGPT or Gemini are fine alternatives.
-->

---

# Claude + Browser: Level 3

<v-clicks>

You could stop here. Ask Claude for a complete HTML file, save it, open it in your browser — done.

But there's a catch. Remember the spectrum?

**Want to change the button color?** → Re-prompt Claude.
**Want to fix a typo?** → Re-prompt Claude.
**Want to tweak spacing?** → Re-prompt Claude.

This is **pure Level 3** — the AI generates everything. Prompting is your only tool.

What if we added a little **Level 2** — where you can make small changes yourself?

</v-clicks>

<!--
This is a quick framing slide — don't linger. The callback to the spectrum is the key moment: they already know Level 3 means "AI generates everything, you guide." Now we're showing the practical limitation of that. The next slide introduces CodePen as the way to blend Level 2 and Level 3 — vibe code the big stuff, hand-edit the small stuff. That's the spectrum in action: choosing the right level for the task.
-->

---

# Setup: CodePen

<img src="/codepen-logo.svg" class="absolute top-8 right-12 w-36 opacity-80" />

<v-clicks>

### Step 1 — Create a free account
Go to **codepen.io** → Sign Up (free)

### Step 2 — Create a new Pen
Click **"Pen"** in the top-left to create a blank pen

### Step 3 — You're ready
You'll see three panels: **HTML**, **CSS**, and **JS**. We'll paste AI-generated code into each matching panel.

<div class="mt-4 text-sm opacity-70">

**Level 3 + Level 2:** Vibe code the big stuff with Claude. Tweak colors, text, or spacing directly in the code yourself. Move between levels as needed.

</div>

</v-clicks>

<!--
Walk the room and make sure everyone has a blank pen open. This is the key framing: CodePen isn't just a viewer — it's an editor. They can vibe code with Claude for the heavy lifting, but also reach in and change a color value or fix a typo themselves. That's the bridge between Level 3 and Level 2 on the spectrum. Common issues: people pasting CSS into the HTML panel, or putting everything in one panel. Make sure they understand: HTML goes in HTML, CSS goes in CSS, JS goes in JS. If someone's confused, just help them match the blocks.
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 1: Your Portfolio — The Hero Section

<div class="text-sm opacity-60 mt-4">Open Claude and CodePen side by side — we're building your first website</div>

<!--
Transition to the hands-on portion. I'll drive Claude on screen and paste into CodePen. Everyone follows along.
-->

---

# Step 1: The Prompt

I'm typing this into Claude on screen. Follow along in your own Claude tab.

<div class="bg-blue-50 dark:bg-blue-900 p-6 rounded-lg mt-4 text-lg select-all cursor-pointer" title="Click to copy">

**Prompt:**

Build a personal portfolio website with a hero section that has a large heading with my name, a subtitle with my role or major, and a call-to-action button that says "See My Work." Use a clean, modern design with a navy blue and white color scheme. Make it look professional. Give me the HTML, CSS, and JavaScript as three separate code blocks so I can paste each into CodePen.

</div>

<div class="mt-4 text-sm opacity-70">

Replace "my name" and "my role or major" with your actual info — or use a fake name for fun.

After Claude responds → paste the HTML block into the **HTML panel**, the CSS into the **CSS panel**, and the JS into the **JS panel**.

</div>

<!--
Read the prompt aloud. Emphasize: we didn't write any code. We described what we want to see. The key phrase is "three separate code blocks so I can paste each into CodePen" — that ensures Claude gives them properly separated code. Now let's see what Claude gives us. Paste each block into the matching panel, see the result. It won't be perfect — and that's the point. Ask the room: "What do you think? What would you change?"
-->

---

# Step 1: What We Got

<v-clicks>

### Review together:
- Does it look professional?
- Are the colors right?
- Is the text readable?
- What would you change?

### The process so far:

1. We **described** what we wanted
2. AI **generated** the code
3. We **pasted** into CodePen and **reviewed** the result
4. Now we **refine** →

</v-clicks>

<!--
Take a moment to look at what Claude generated. Everyone's will look slightly different — that's expected. The AI interprets your prompt in its own way. Notice: you got a full website with styling, layout, and responsive design — from one prompt. Now let's make it better.
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 2: Adding Content Sections

<div class="text-sm opacity-60 mt-4">Small, specific follow-up prompts beat rewriting everything</div>

---

# Step 2: Build Out the Page

Send these **one at a time** to Claude. Paste each updated set of blocks into CodePen.

<div class="space-y-4 mt-4">

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 1:** *"Add an About Me section below the hero with a placeholder photo on the left and a short bio paragraph on the right. Give me the updated HTML, CSS, and JS as three separate code blocks."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 2:** *"Add a Skills section that displays 6 skills as cards in a grid. Use simple icons or emoji for each skill. Pick skills that a college student might have."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 3:** *"Add a Contact section at the bottom with a simple form — name, email, and message fields with a Send button."*

</div>

<div class="bg-green-50 dark:bg-green-900 p-4 rounded select-all cursor-pointer">

**Prompt 4:** *"Add a footer with links to GitHub, LinkedIn, and Twitter using icons. Include a copyright line."*

</div>

</div>

<!--
Each prompt is one section. This is key — if you ask for five things at once and something breaks, you don't know which change caused it. One at a time. After each response, replace the contents of all three CodePen panels with the updated code. If something breaks, tell Claude what went wrong: "The about section is overlapping the hero" or "the skills cards aren't aligned." The first prompt asks for three separate code blocks — after that, Claude will keep giving separated blocks in the same conversation. Give them time here. Walk the room. Some people will be ahead, some behind. That's fine.
-->

---

# What's Happening Here

<v-clicks>

- Each prompt is **small and specific**
- You **see the result** after each change
- If something breaks, you tell Claude: *"The skills section looks weird — the cards are stacking vertically instead of in a grid. Fix it."*
- **Troubleshooting is part of the process, not a failure**

This cycle is the core of vibe coding:

<div class="flex items-center justify-center gap-3 mt-6">
  <div class="bg-blue-100 dark:bg-blue-900 px-4 py-3 rounded-lg text-center shadow-sm">
    <ph-chat-text class="text-2xl mb-1 mx-auto text-blue-600" /><br/>
    <span class="text-sm font-bold">Describe</span>
  </div>
  <ph-arrow-right class="text-xl text-gray-400" />
  <div class="bg-violet-100 dark:bg-violet-900 px-4 py-3 rounded-lg text-center shadow-sm">
    <ph-magic-wand class="text-2xl mb-1 mx-auto text-violet-600" /><br/>
    <span class="text-sm font-bold">Generate</span>
  </div>
  <ph-arrow-right class="text-xl text-gray-400" />
  <div class="bg-amber-100 dark:bg-amber-900 px-4 py-3 rounded-lg text-center shadow-sm">
    <ph-magnifying-glass class="text-2xl mb-1 mx-auto text-amber-600" /><br/>
    <span class="text-sm font-bold">Review</span>
  </div>
  <ph-arrow-right class="text-xl text-gray-400" />
  <div class="bg-green-100 dark:bg-green-900 px-4 py-3 rounded-lg text-center shadow-sm">
    <ph-wrench class="text-2xl mb-1 mx-auto text-green-600" /><br/>
    <span class="text-sm font-bold">Refine</span>
  </div>
  <ph-arrow-right class="text-xl text-gray-400" />
  <div class="bg-gray-100 dark:bg-gray-800 px-4 py-3 rounded-lg text-center shadow-sm">
    <ph-arrows-clockwise class="text-2xl mb-1 mx-auto text-gray-500" /><br/>
    <span class="text-sm font-bold">Repeat</span>
  </div>
</div>

</v-clicks>

<!--
Reinforce: this iterative loop is the skill. It's not about getting perfect code on the first try. Professional developers using AI work the same way — describe, generate, review, refine. The only difference is they can read the code more deeply. But the process is identical.
-->

---
layout: center
class: text-center
---

# Codealong Time

### Step 3: Polish & Interactivity

<div class="text-sm opacity-60 mt-4">Turn a static page into something that feels alive</div>

---

# Step 3: Make It Interactive

These prompts add the polish that makes a site feel professional.

<div class="space-y-4 mt-4">

<div class="bg-purple-50 dark:bg-purple-900 p-4 rounded select-all cursor-pointer">

**Prompt 1:** *"Add a navigation bar at the top that links to each section. When I click a link, it should smooth-scroll to that section."*

</div>

<div class="bg-purple-50 dark:bg-purple-900 p-4 rounded select-all cursor-pointer">

**Prompt 2:** *"Add a dark mode toggle button in the top-right corner of the nav bar. It should switch all colors to a dark theme and back."*

</div>

<div class="bg-purple-50 dark:bg-purple-900 p-4 rounded select-all cursor-pointer">

**Prompt 3:** *"Add subtle hover animations — skill cards should lift up slightly when hovered, and the CTA button should glow."*

</div>

</div>

<div class="mt-6 text-sm opacity-70">

These are all **JavaScript behaviors** — interactivity you described in English, and Claude implemented for you.

</div>

<!--
This is the "wow" moment. One prompt gives us smooth scrolling. Another gives us dark mode. These are real front-end development features that would take a beginner hours to implement manually. Don't rush this — let the room react. If something doesn't work, debug live: "The dark mode toggle isn't switching the background color." Model the process. Remind them to replace all three panels each time.
-->

---

# What Just Happened?

<v-clicks>

<div class="flex items-center justify-center gap-4 mt-8 text-lg">
  <div class="bg-blue-100 dark:bg-blue-900 px-6 py-4 rounded-xl text-center font-bold shadow">
    <ph-layout class="text-3xl mb-1 mx-auto" /><br/>Layout
  </div>
  <ph-arrow-right class="text-3xl text-gray-400" />
  <div class="bg-amber-100 dark:bg-amber-900 px-6 py-4 rounded-xl text-center font-bold shadow">
    <ph-text-columns class="text-3xl mb-1 mx-auto" /><br/>Content
  </div>
  <ph-arrow-right class="text-3xl text-gray-400" />
  <div class="bg-green-100 dark:bg-green-900 px-6 py-4 rounded-xl text-center font-bold shadow">
    <ph-cursor-click class="text-3xl mb-1 mx-auto" /><br/>Interactive
  </div>
</div>

<div class="grid grid-cols-2 gap-8 mt-10">
<div class="text-center">
  <div class="text-5xl font-bold text-gray-400">0</div>
  <div class="text-sm opacity-70 mt-1">lines written by hand</div>
</div>
<div class="text-center">
  <div class="text-5xl font-bold">~8</div>
  <div class="text-sm opacity-70 mt-1">prompts written</div>
</div>
</div>

<div class="mt-8 text-center text-xl">

The AI wrote the HTML, CSS, and JavaScript. **We made the decisions.**

</div>

</v-clicks>

<!--
This is the key takeaway slide. Pause here. Let it sink in. The prompts were the creative work. Deciding the color scheme, the layout, what sections to include, what interactivity to add — those are design decisions. The AI translated them into code. Ask the room: "At any point did you feel like you weren't in control?"
-->

---
layout: center
---

# Free Experimentation
## 25 Minutes — Make It Yours

<div class="text-sm opacity-60">Keep prompting Claude — paste into CodePen to see your results. Ask me if you get stuck.</div>

---

# Challenge Ideas

Pick one, combine a few, or invent your own:

<div class="grid grid-cols-4 gap-4 mt-6">

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-palette class="text-3xl mb-2 mx-auto text-violet-500" />
  <div class="text-sm font-bold">Custom Theme</div>
  <div class="text-xs opacity-60 mt-1">New colors & fonts</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-briefcase class="text-3xl mb-2 mx-auto text-blue-600" />
  <div class="text-sm font-bold">Projects</div>
  <div class="text-xs opacity-60 mt-1">Add a portfolio gallery</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-device-mobile class="text-3xl mb-2 mx-auto text-green-600" />
  <div class="text-sm font-bold">Mobile-First</div>
  <div class="text-xs opacity-60 mt-1">Optimize for phones</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-sparkle class="text-3xl mb-2 mx-auto text-amber-500" />
  <div class="text-sm font-bold">Animations</div>
  <div class="text-xs opacity-60 mt-1">Scroll effects & transitions</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-article class="text-3xl mb-2 mx-auto text-pink-500" />
  <div class="text-sm font-bold">Blog Section</div>
  <div class="text-xs opacity-60 mt-1">Posts or articles page</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-quotes class="text-3xl mb-2 mx-auto text-cyan-500" />
  <div class="text-sm font-bold">Testimonials</div>
  <div class="text-xs opacity-60 mt-1">Quotes carousel</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-file-text class="text-3xl mb-2 mx-auto text-red-500" />
  <div class="text-sm font-bold">Resume Page</div>
  <div class="text-xs opacity-60 mt-1">Separate CV / resume</div>
</div>

<div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 text-center shadow-sm hover:shadow-md transition-shadow">
  <ph-egg-crack class="text-3xl mb-2 mx-auto text-lime-500" />
  <div class="text-sm font-bold">Easter Egg</div>
  <div class="text-xs opacity-60 mt-1">Hidden feature or secret</div>
</div>

</div>

<div class="mt-4 text-sm opacity-70 text-center">

**Stuck?** Try: *"I want my portfolio to have [describe what you see in your head]."*

</div>

<!--
Let them go. Walk the room. Help people who are stuck by asking "what do you want your site to look like?" and helping them turn that into a prompt. Don't write prompts for them — coach them to describe what they see. Some people will go deep on their portfolio. Others will start a completely different site. Both are fine. Remind anyone who's stuck to include "Give me the updated HTML, CSS, and JS as three separate code blocks" in their prompt so Claude gives them properly separated code to paste.
-->

---

# When Things Break

<v-clicks>

This **will** happen. It's not a failure — it's the process.

### Your debugging toolkit:

1. **Describe the symptom:** *"The nav links don't scroll to the right sections."*

2. **Share a screenshot:** If the preview looks wrong, describe exactly what's off

3. **Ask for a redo:** *"The Skills section doesn't match the rest of the design. Rebuild it to match the style of the About section."*

4. **Start smaller:** If it's totally broken, ask: *"Simplify — just show me a clean hero section with a nav bar."*

</v-clicks>

<!--
Normalize this. Every professional developer's workflow includes things breaking. The difference between frustration and progress is knowing how to describe the problem. That's a skill you're practicing right now.
-->

---

# Discussion

<v-clicks>

- What **surprised** you about the process?
- What made you **uncomfortable**?
- Did you look at the generated code — or just the preview?
- How is this different from using Squarespace, Wix, or Canva?
- Would you trust this for a site that represents you professionally?

</v-clicks>

<!--
Open it up. These questions don't have right answers. Some people will be excited, some will be skeptical. Both reactions are valid. If someone says "I never looked at the code" — that's honest, and it's worth exploring. If someone asks about Squarespace/Wix — great question. The difference: those give you templates. This gives you anything you can describe. The trade-off is you need to be more intentional about what you're asking for.
-->

---

# A Word on Responsibility

<v-clicks>

AI-generated web code can introduce real issues if you deploy it without review:

- **Exposed secrets** — AI might put API keys directly in client-side JavaScript
- **No input validation** — that contact form might accept anything
- **Accessibility gaps** — AI doesn't always generate screen-reader-friendly HTML
- **Copy-paste content** — AI-written bios and descriptions can sound generic or contain errors

### The pattern:
AI optimizes for **"does it look right?"** — not **"is it production-ready?"**

**For a portfolio you'll actually publish:** review the content, test the form, check it on mobile.

</v-clicks>

<!--
Brief but important. We're not going deep on security today, but this needs to be said. If you take what you built today and put it on the internet, run through it once as a visitor would. Does the form actually work? Is the content accurate? Does it look right on your phone? The AI got you 90% there — the last 10% is yours.
-->

---

# Your Takeaways

<v-clicks>

1. **Vibe coding** is describing outcomes and guiding AI — not writing syntax
2. **Good prompts** are specific, constrained, and iterate in small steps
3. **The spectrum** helps you choose how much AI involvement fits the task
4. **Your guidelines** keep you in the driver's seat
5. **Breaking things** is debugging, not failing
6. The **design decisions** are still yours — AI is the tool, not the designer
7. **Review before you publish** — AI gets you there fast, but the last mile is yours

</v-clicks>

<!--
Quick recap. Seven takeaways that capture the whole workshop. The first six are about capability. The seventh is about responsibility. You built a real website today. Whether you publish it, iterate on it, or start something completely new — you now know the process.
-->

---

# Keep Going

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### Tools from today
- **Claude.ai** / **ChatGPT** / **Gemini** — AI assistants
- **CodePen** — codepen.io (free, instant preview)
- **Export your work:** In CodePen, click **Export → Export .zip** to download your HTML, CSS, and JS files

### What to try next
- Build a site for a club, event, or side project
- Try **bolt.new** — AI web builder (generates full projects)
- Try **v0.dev** — AI web builder by Vercel
- Explore **Lovable** (lovable.dev) — AI full-stack apps
- Learn HTML/CSS basics on **freeCodeCamp**

</div>
<div>

### The prompt pattern
1. Describe what you want to see
2. Be specific about design and content
3. Iterate with small follow-ups
4. Debug by describing symptoms
5. Review before publishing

### Your guidelines
Keep them. Revisit them. Update them as you learn.

</div>
</div>

<!--
Leave these resources up while people pack up. bolt.new, v0.dev, and Lovable are AI-powered web development tools worth trying at home — they generate full projects but have usage limits on free tiers. freeCodeCamp is excellent if anyone wants to learn the fundamentals behind what the AI is generating. And CodePen is a great sandbox for experimenting.
-->

---
layout: center
class: text-center
---

# Thank You

**Dr. Curt Rode** · TCU

<div class="mt-8 opacity-60">

Today's slides and prompts are available at:

[curtrode.github.io/general_workshops/vibes](https://curtrode.github.io/general_workshops/vibes/)

</div>
