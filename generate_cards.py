import base64
import os

projects = [
    {
        "id": "teamvx",
        "name": "TeamVx",
        "icon_file": "assets/projects/teamvx.png",
        "link": "https://play.google.com/store/apps/details?id=com.teamvx.app",
        "font_size": 12
    },
    {
        "id": "music-player",
        "name": "Music Player",
        "icon_file": "assets/projects/music-player.png",
        "link": "https://play.google.com/store/apps/details?id=com.music_player.music_player",
        "font_size": 12
    },
    {
        "id": "onespect",
        "name": "Onespect",
        "icon_file": "assets/projects/onespect.png",
        "link": "https://play.google.com/store/apps/details?id=in.onespect.onespect_flutter_mobile_app",
        "font_size": 12
    },
    {
        "id": "quickbazaria",
        "name": "QuickBazaria",
        "icon_file": "assets/projects/quickbazaria.png",
        "link": "https://play.google.com/store/apps/details?id=com.quickbazaria.app",
        "font_size": 11.5
    },
    {
        "id": "dblite",
        "name": "DB Lite",
        "icon_file": "assets/projects/dblite.png",
        "link": "https://www.indusappstore.com/apps/productivity/db-lite/me.ankit.dblite?page=details&id=me.ankit.dblite",
        "font_size": 12
    },
    {
        "id": "my-notes",
        "name": "My Notes",
        "icon_file": "assets/projects/my-notes.png",
        "link": "https://www.indusappstore.com/apps/productivity/my-notes/io.github.ankitdotdev.my_notes?page=details&id=io.github.ankitdotdev.my_notes",
        "font_size": 12
    },
    {
        "id": "color-blind",
        "name": "Color Blind Assist",
        "icon_file": "assets/projects/color-blind.png",
        "link": "https://www.indusappstore.com/apps/health-and-fitness/are-you-colorblind/com.ankitm05.are_you_colorblind/?page=details&id=com.ankitm05.are_you_colorblind",
        "font_size": 10.5
    }
]

def generate_svg(p):
    with open(p["icon_file"], "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="124" viewBox="0 0 100 124" fill="none">
  <defs>
    <clipPath id="squircle-{p["id"]}">
      <rect x="12" y="6" width="76" height="76" rx="17" ry="17" />
    </clipPath>
    <filter id="shadow-{p["id"]}" x="6" y="2" width="88" height="88" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
    <style>
      .app-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: {p["font_size"]}px;
        font-weight: 600;
        fill: #1F2328;
      }}
      .app-border {{
        stroke: rgba(0, 0, 0, 0.08);
      }}
      @media (prefers-color-scheme: dark) {{
        .app-title {{
          fill: #F0F6FC;
        }}
        .app-border {{
          stroke: rgba(255, 255, 255, 0.15);
        }}
      }}
    </style>
  </defs>

  <!-- Drop Shadow Base -->
  <rect x="12" y="6" width="76" height="76" rx="17" ry="17" fill="#FFFFFF" filter="url(#shadow-{p["id"]})"/>

  <!-- Icon Image -->
  <image href="data:image/png;base64,{b64}" x="12" y="6" width="76" height="76" clip-path="url(#squircle-{p["id"]})" preserveAspectRatio="xMidYMid slice" />

  <!-- Subtle Border Ring -->
  <rect x="12" y="6" width="76" height="76" rx="17" ry="17" fill="none" class="app-border" stroke-width="1"/>

  <!-- App Label -->
  <text x="50" y="106" text-anchor="middle" class="app-title">{p["name"]}</text>
</svg>'''
    
    out_path = f"assets/projects/{p['id']}.svg"
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(svg)
    print(f"Generated {out_path}")

for p in projects:
    generate_svg(p)
print("All SVGs generated successfully!")
