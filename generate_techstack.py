import re
import urllib.request

# Added missing technologies and extended rows
row1_icons = "python,java,js,ts,html,css,react,nodejs,express,flask,spring,postgresql,supabase,vercel,dotnet,cs,linux,ubuntu,bash"
row2_icons = "mongodb,mysql,docker,git,github,postman,vite,tailwind,sklearn,pandas,numpy,tensorflow,figma,vscode,android,apple,aws,redis,sqlite"

def fetch_and_extract_icons(icons_list):
    url = f"https://skillicons.dev/icons?i={icons_list}&perline=40"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        svg_content = response.read().decode('utf-8')
    
    match = re.search(r'<svg[^>]*>(.*)</svg>', svg_content, re.DOTALL | re.IGNORECASE)
    if match:
        inner = match.group(1)
        return inner
    return ""

row1_svg = fetch_and_extract_icons(row1_icons)
row2_svg = fetch_and_extract_icons(row2_icons)

def get_width(icons_list):
    url = f"https://skillicons.dev/icons?i={icons_list}&perline=40"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        svg_content = response.read().decode('utf-8')
    match = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_content)
    if match:
        return int(match.group(1))
    return 1000

w1 = get_width(row1_icons)
w2 = get_width(row2_icons)

# Fix the gap between copies: the original viewBox ends right at the edge of the last icon.
# To add the normal 44px gap between the end of one copy and start of another:
offset1 = w1 + 44
offset2 = w2 + 44

full_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="150" viewBox="0 0 800 150">
    <style>
        .marquee-left {{
            animation: slide-left 30s linear infinite;
        }}
        .marquee-right {{
            animation: slide-right 30s linear infinite;
        }}
        @keyframes slide-left {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(-{offset1}px); }}
        }}
        @keyframes slide-right {{
            from {{ transform: translateX(-{offset2}px); }}
            to {{ transform: translateX(0); }}
        }}
    </style>

    <!-- Row 1 moving left -->
    <g transform="translate(0, 0) scale(0.2)">
        <g class="marquee-left">
            <g transform="translate(0, 0)">
                {row1_svg}
            </g>
            <g transform="translate({offset1}, 0)">
                {row1_svg}
            </g>
            <g transform="translate({offset1*2}, 0)">
                {row1_svg}
            </g>
        </g>
    </g>

    <!-- Row 2 moving right -->
    <g transform="translate(0, 70) scale(0.2)">
        <g class="marquee-right">
            <g transform="translate(-{offset2}, 0)">
                {row2_svg}
            </g>
            <g transform="translate(0, 0)">
                {row2_svg}
            </g>
            <g transform="translate({offset2}, 0)">
                {row2_svg}
            </g>
        </g>
    </g>
</svg>
"""

with open(r'c:\Users\nayan\OneDrive\Desktop\CV\moving_techstack.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)

print("Generated moving_techstack.svg successfully.")
