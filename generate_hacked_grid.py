import random

# Konfigurasi SVG
WIDTH = 800
HEIGHT = 150
VIEWBOX = f"0 0 {WIDTH} {HEIGHT}"
RECT_SIZE = 11
RECT_GAP = 3
GRID_TRANSLATE_X = 20
GRID_TRANSLATE_Y = 20

# Teks Hacked
TEXT_ELEMENTS = [
    '<text x="200" y="110" style="animation: pulse-flicker 2s infinite alternate;">CRITICAL_BREACH_DETECTED</text>',
    '<text x="500" y="110" style="animation: pulse-flicker 2.5s infinite alternate 1s;">DATAFRAME://CORRUPTED</text>',
    '<text x="10" y="130" style="animation: pulse-flicker 3s infinite alternate 2s;">MIRZU://HACKED</text>'
]

# Style & Animasi
STYLE = """
<style>
  text {
    font-family: 'Consolas', 'Courier New', Courier, monospace;
    font-size: 10px;
    fill: #39FF14;
  }
  
  .contribution-grid rect {
    width: 11px;
    height: 11px;
    rx: 1.5;
    ry: 1.5;
    opacity: 1;
    transition: fill 0.1s ease-in-out;
  }
  
  .level-0 { fill: #0d1117; }
  .level-1 { fill: #102e1a; }
  .level-2 { fill: #1d5635; }
  .level-3 { fill: #2d8f58; }
  .level-4 { fill: #39d353; }
  
  @keyframes pulse-flicker {
    0%, 100% { opacity: 0.95; }
    15%, 85% { opacity: 1; fill: inherit; }
    25% { opacity: 0.4; fill: #ff004c !important; }
    30%, 70% { opacity: 0.1; }
    35% { opacity: 0.9; fill: #00ffff !important; }
    60% { opacity: 0.8; fill: #ffd700 !important; }
    95% { opacity: 1; fill: inherit; }
  }
  
  .contribution-grid rect:nth-child(5n+1) { animation: pulse-flicker 2.1s infinite alternate 0.1s; }
  .contribution-grid rect:nth-child(5n+2) { animation: pulse-flicker 1.9s infinite alternate 0.4s; }
  .contribution-grid rect:nth-child(5n+3) { animation: pulse-flicker 2.3s infinite alternate 0.7s; }
  .contribution-grid rect:nth-child(5n+4) { animation: pulse-flicker 2.0s infinite alternate 1s; }
  .contribution-grid rect:nth-child(5n) { animation: pulse-flicker 2.2s infinite alternate 1.3s; }
  
  @keyframes svg-distortion {
    0%, 100% { transform: scale(1) skew(0deg); opacity: 1; }
    2% { transform: scale(1.005) skew(0.1deg); opacity: 0.95; }
    10%, 90% { transform: scale(1) skew(0deg); opacity: 1; }
    50% { transform: scale(1.002) skew(0.05deg); opacity: 0.99; }
  }
  
  #main-grid { animation: svg-distortion 5s infinite linear; }
</style>
"""

def generate_svg():
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{WIDTH}" height="{HEIGHT}" viewBox="{VIEWBOX}">'
    svg_content += "<defs>" + STYLE + "</defs>"
    svg_content += f'<g id="main-grid" transform="translate({GRID_TRANSLATE_X}, {GRID_TRANSLATE_Y})">'
    svg_content += '<g class="contribution-grid">'
    
    # Jana 52 lajur (minggu)
    for week in range(52):
        x = week * (RECT_SIZE + RECT_GAP)
        # Jana 7 kotak (hari) untuk setiap minggu
        for day in range(7):
            y = day * (RECT_SIZE + RECT_GAP)
            # Tentukan level contribution rawak (boleh diganti dengan data sebenar jika mahu)
            level = random.randint(0, 4)
            rect_class = f"level-{level}"
            svg_content += f'<rect x="{x}" y="{y}" class="{rect_class}" data-level="{level}"/>'
            
    svg_content += "</g>"
    
    # Tambah elemen teks
    for text in TEXT_ELEMENTS:
        svg_content += text
        
    svg_content += "</g></svg>"
    return svg_content

if __name__ == "__main__":
    generated_svg = generate_svg()
    with open("contribution-glitch.svg", "w") as f:
        f.write(generated_svg)
    print("Fail contribution-glitch.svg yang lengkap telah dijana!")
