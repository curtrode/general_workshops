#!/usr/bin/env python3
"""
Generate a retro-styled index.html gallery page from all *-game.html files
in this directory. Run manually or via GitHub Action.

Usage:
  python build_index.py
"""

from pathlib import Path

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A Human-Centered AI Future — Game Arcade</title>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      background: #0a0a1a;
      color: #e0e0e0;
      font-family: 'Press Start 2P', monospace;
      min-height: 100vh;
      padding: 2rem 1rem;
    }}

    .scanlines {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      pointer-events: none;
      background: repeating-linear-gradient(
        transparent,
        transparent 2px,
        rgba(0, 0, 0, 0.08) 2px,
        rgba(0, 0, 0, 0.08) 4px
      );
      z-index: 1000;
    }}

    header {{
      text-align: center;
      margin-bottom: 3rem;
    }}

    h1 {{
      font-size: clamp(1rem, 3vw, 1.6rem);
      color: #00ffcc;
      text-shadow: 0 0 10px #00ffcc, 0 0 30px #00997a;
      margin-bottom: 0.8rem;
      line-height: 1.6;
    }}

    .subtitle {{
      font-size: clamp(0.5rem, 1.5vw, 0.7rem);
      color: #ff6ec7;
      text-shadow: 0 0 8px #ff6ec7;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.5rem;
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1rem;
    }}

    .card {{
      background: #12122a;
      border: 2px solid #333;
      border-radius: 4px;
      padding: 1.5rem;
      text-align: center;
      transition: all 0.2s;
      text-decoration: none;
      display: block;
    }}

    .card:hover {{
      border-color: #00ffcc;
      box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
      transform: translateY(-3px);
    }}

    .card .player {{
      font-size: 0.75rem;
      color: #ffd700;
      text-shadow: 0 0 6px #ffd700;
      margin-bottom: 0.6rem;
      text-transform: uppercase;
    }}

    .card .play {{
      font-size: 0.6rem;
      color: #00ffcc;
      opacity: 0;
      transition: opacity 0.2s;
    }}

    .card:hover .play {{
      opacity: 1;
    }}

    .empty {{
      text-align: center;
      color: #555;
      font-size: 0.7rem;
      margin-top: 4rem;
      line-height: 2;
    }}

    footer {{
      text-align: center;
      margin-top: 3rem;
      font-size: 0.45rem;
      color: #444;
      line-height: 2;
    }}
  </style>
</head>
<body>
  <div class="scanlines"></div>
  <header>
    <h1>A Human-Centered AI Future</h1>
    <p class="subtitle">Game Arcade</p>
  </header>
  <main>
{content}
  </main>
  <footer>
    <p>Conversation Coding Workshop &mdash; Built with AI</p>
  </footer>
</body>
</html>
"""


def build_card(filename: str) -> str:
    name = filename.replace("-game.html", "").replace("-", " ").title()
    return (
        f'    <a class="card" href="{filename}">\n'
        f'      <div class="player">{name}</div>\n'
        f'      <div class="play">[PRESS START]</div>\n'
        f'    </a>'
    )


def main():
    games_dir = Path(__file__).parent
    game_files = sorted(
        f.name for f in games_dir.glob("*-game.html")
    )

    if game_files:
        cards = "\n".join(build_card(f) for f in game_files)
        content = f'    <div class="grid">\n{cards}\n    </div>'
    else:
        content = '    <div class="empty"><p>No games yet...</p><p>INSERT COIN TO CONTINUE</p></div>'

    html = TEMPLATE.format(content=content)
    output = games_dir / "index.html"
    output.write_text(html, encoding="utf-8")
    print(f"Built index.html with {len(game_files)} game(s)")
    for f in game_files:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
