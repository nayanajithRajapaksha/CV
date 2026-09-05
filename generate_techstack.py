import re
import urllib.request

# Line 1: Languages and Frameworks
row1_icons = "python,java,js,ts,html,css,cs,kotlin,dart,react,nextjs,vue,tailwind,nodejs,express,fastapi,flask,spring,dotnet,flutter,sklearn,tensorflow"
# Line 2: Software, Tools, Databases, and Platforms
row2_icons = "postgresql,mysql,mongodb,sqlite,redis,supabase,firebase,docker,git,github,postman,vite,figma,vscode,vercel,linux,ubuntu,bash,apple,aws"

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
