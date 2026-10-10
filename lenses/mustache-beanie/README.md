# Mustache + beanie

Face-accessory lens. It imitates the format of `mustache + beanie` (#46) and
`mustache + tattoos` (#4) on the Lens+ top chart. See `research/analysis.md`.

## What is in this folder

```
Assets/Scripts/MustacheBeanie.ts   Script: anchors two overlays to the face
Assets/Textures/mustache.png       Transparent PNG, generated with gpt-image-1
Assets/Textures/beanie.png         Transparent PNG, generated with gpt-image-1
prompts.json                       Prompts used to generate the PNGs
```

## How it works

- A `Component.Head` on an anchor object follows the face. `setAttachmentPointType` picks the point:
  `MouthCenter` for the mustache and `Forehead` for the beanie.
- Each `Component.Image` is a child of its anchor, so it moves with the face.
- Textures and sizes are `@input`s, so you can tune them without editing code.

## Set up in Lens Studio (Windows 11 or macOS 12+)

1. Open Lens Studio and create a new project from the **Empty** template.
2. Drag `Assets/Scripts/MustacheBeanie.ts` and the two PNGs in `Assets/Textures/` into the
   project's **Assets** panel. Lens Studio imports the PNGs as textures.
3. Create an empty **Scene Object** named `Lens Controller` at the root of the scene.
4. Add the `MustacheBeanie` script component to it.
5. In the Inspector, set **Mustache Texture** and **Beanie Texture** to the imported PNGs.
6. Press **Preview** and check the webcam feed. Adjust **Mustache Size** and **Beanie Size**
   (starting values 0.35 and 1.2) until they fit.

## Status

- The API calls were checked against the Lens Studio 5.24.1 TypeScript declarations
  (`global.scene.createSceneObject`, `Component.Head`, `setAttachmentPointType`,
  `AttachmentPointType.MouthCenter`, `Forehead`, `Component.Image`, `mainPass.baseTex`).
  The script type-checks cleanly.
- It has **not** been run in Lens Studio. The editor did not reach its main window in this
  sandbox (see the top-level README). The size values are starting guesses.
