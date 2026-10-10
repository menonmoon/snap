# Snapchat lenses: research and imitations

Work in progress. This repo holds:

- `research/`: the Lens+ All Time Top 50 chart, as data, and an analysis of what
  makes those lenses rank.
- `lenses/`: lenses that imitate chart formats. Each folder has a Lens Studio
  script, its textures, and setup steps.
- `tools/generate_assets.py`: generates transparent PNG assets with the OpenAI
  image API.

## Start here

- `research/analysis.md`: the formats on the chart, which ones we imitate, and what is next.
- `lenses/mustache-beanie/README.md`: face accessories (mustache and beanie).
- `lenses/lash-glam/README.md`: lashes on both eyes.

## Lens Studio status

Lens Studio 5.24.1 for Windows was downloaded and installed in this sandbox. It runs
under Wine 9.0 with software OpenGL. What we verified and what we did not:

| Step | Result |
|---|---|
| Download the Windows installer from ar.snap.com | Done (806 MB). The download requires accepting the Privacy Policy, License Agreement and Terms of Service on the page. |
| Install silently under Wine | Done. Needed the 32-bit Wine packages (`wine32:i386`). |
| Launch `Lens Studio.exe` on a virtual display | The process starts and loads its services, then stalls. The main window never appears in about 7 minutes, and CPU stays near idle. The cause is not confirmed. Sign-in is one possibility; it is not verified. |
| Use the editor to build or preview a lens | Not possible while the window stays hidden. |
| Check the scripting API | Done. The installed `StudioLib.d.ts` and `Declarations/*.d.ts` were used to type-check the scripts. |

Lens Studio officially supports only Windows 11 and macOS 12+. For editing and previewing, use
a Windows or Mac machine. Open the project folders in `lenses/` there.

## Image generation

`tools/generate_assets.py` reads the OpenAI key from `OPENAI_API_KEY`. The key is never stored
in the repo.

```bash
export OPENAI_API_KEY=...   # your key, from your own shell or secret store
python3 tools/generate_assets.py lenses/mustache-beanie/prompts.json
python3 tools/generate_assets.py lenses/lash-glam/prompts.json
```

The script writes PNGs to `<lens>/Assets/Textures/`. Existing files are skipped.

**Security:** an OpenAI key was pasted into the chat for this work. Treat it as exposed and
rotate it in the OpenAI dashboard once this work is finished.
