import os

learning_card_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="340" viewBox="0 0 800 340">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1e1e" />
      <stop offset="100%" stop-color="#121212" />
    </linearGradient>

    <!-- Drop Shadow -->
    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="15" stdDeviation="20" flood-opacity="0.5" />
    </filter>
  </defs>

  <!-- Outer container with shadow and rounded corners -->
  <rect x="20" y="20" width="760" height="300" rx="16" ry="16" fill="url(#bgGrad)" filter="url(#dropShadow)" />
  
  <!-- Inner thin border (glass effect) -->
  <rect x="21" y="21" width="758" height="298" rx="15" ry="15" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>

  <!-- MacOS Window Buttons -->
  <circle cx="50" cy="45" r="7" fill="#ff5f56" />
  <circle cx="75" cy="45" r="7" fill="#ffbd2e" />
  <circle cx="100" cy="45" r="7" fill="#27c93f" />

  <!-- Window Title -->
  <text x="400" y="50" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" fill="#8b949e" text-anchor="middle" font-weight="600">learning.py — VS Code</text>

  <!-- Code Background -->
  <rect x="40" y="75" width="720" height="225" rx="8" fill="#0d1117" />
  <rect x="41" y="76" width="718" height="223" rx="7" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>

  <!-- Code Text -->
  <g font-family="'Fira Code', Consolas, Monaco, 'Courier New', Courier, monospace" font-size="15" font-weight="500">
    <!-- Line numbers -->
    <text x="65" y="110" fill="#484f58" text-anchor="end">1</text>
    <text x="65" y="135" fill="#484f58" text-anchor="end">2</text>
    <text x="65" y="160" fill="#484f58" text-anchor="end">3</text>
    <text x="65" y="185" fill="#484f58" text-anchor="end">4</text>
    <text x="65" y="210" fill="#484f58" text-anchor="end">5</text>
    <text x="65" y="235" fill="#484f58" text-anchor="end">6</text>
    <text x="65" y="260" fill="#484f58" text-anchor="end">7</text>
    
    <!-- Code Content -->
    <!-- Line 1: nayanajith = { -->
    <text x="90" y="110" fill="#79c0ff">nayanajith</text>
    <text x="180" y="110" fill="#c9d1d9"> = {</text>

    <!-- Line 2: "currently_learning": [ -->
    <text x="120" y="135" fill="#a5d6ff">"currently_learning"</text>
    <text x="300" y="135" fill="#c9d1d9">: [</text>

    <!-- Line 3: Array elements -->
    <text x="150" y="160" fill="#ff7b72">"</text><text x="159" y="160" fill="#a5d6ff">Agentic AI &amp; LLM Fine-tuning</text><text x="382" y="160" fill="#ff7b72">"</text><text x="390" y="160" fill="#c9d1d9">,</text>
    <text x="410" y="160" fill="#ff7b72">"</text><text x="419" y="160" fill="#a5d6ff">Next.js &amp; TS</text><text x="526" y="160" fill="#ff7b72">"</text><text x="534" y="160" fill="#c9d1d9">,</text>
    <text x="554" y="160" fill="#ff7b72">"</text><text x="563" y="160" fill="#a5d6ff">Docker &amp; CI/CD</text><text x="690" y="160" fill="#ff7b72">"</text>

    <!-- Line 4: ], -->
    <text x="120" y="185" fill="#c9d1d9">],</text>

    <!-- Line 5: "building" -->
    <text x="120" y="210" fill="#79c0ff">"building"</text>
    <text x="200" y="210" fill="#c9d1d9">         : </text>
    <text x="310" y="210" fill="#a5d6ff">"AI-powered products that solve real problems"</text>
    <text x="695" y="210" fill="#c9d1d9">,</text>

    <!-- Line 6: "open_to" -->
    <text x="120" y="235" fill="#79c0ff">"open_to"</text>
    <text x="190" y="235" fill="#c9d1d9">          : </text>
    <text x="310" y="235" fill="#a5d6ff">"Internships · Collaborations · Open Source"</text>
    <text x="668" y="235" fill="#c9d1d9">,</text>

    <!-- Line 7: "fun_fact" -->
    <text x="120" y="260" fill="#79c0ff">"fun_fact"</text>
    <text x="200" y="260" fill="#c9d1d9">         : </text>
    <text x="310" y="260" fill="#a5d6ff">"I debug ML models at 2am — and enjoy it 🤖"</text>
    
    <!-- Line 8: } -->
    <text x="90" y="285" fill="#c9d1d9">}</text>
  </g>
</svg>
"""

with open(r'c:\Users\nayan\OneDrive\Desktop\CV\learning_card.svg', 'w', encoding='utf-8') as f:
    f.write(learning_card_svg)

print("Generated learning_card.svg successfully.")
