# Lash glam

Face-accessory lens. It imitates the format of `2016 + lashes` (#13) and
`Lash Light Touch` (#22) on the Lens+ top chart. See `research/analysis.md`.

## What is in this folder

```
Assets/Scripts/LashGlam.ts     Script: anchors a lash strip to each eye
Assets/Textures/lashes.png     Transparent PNG, generated with gpt-image-1
prompts.json                   Prompt used to generate the PNG
```

## How it works

- Two `Component.Head` anchors follow the eyes: `LeftEyeballCenter` and `RightEyeballCenter`.
- The right-eye strip reuses the same texture with `flipX`, so the pair is symmetrical.
- Size, vertical offset and face index are `@input`s.

## Set up in Lens Studio (Windows 11 or macOS 12+)

1. Open Lens Studio and create a new project from the **Empty** template.
2. Drag `Assets/Scripts/LashGlam.ts` and `Assets/Textures/lashes.png` into the project's **Assets**
   panel.
3. Create an empty **Scene Object** named `Lens Controller` at the root of the scene.
4. Add the `LashGlam` script component to it.
5. In the Inspector, set **Lash Texture** to the imported PNG.
6. Press **Preview**, check the webcam feed, and tune **Lash Size** (starting value 0.25) and
   **Lash Offset Y** (starting value 0.05) so the lashes sit on the lash line.

## Status

- The API calls were checked against the Lens Studio 5.24.1 TypeScript declarations. The script
  type-checks cleanly.
- It has **not** been run in Lens Studio. The size and offset values are starting guesses.
