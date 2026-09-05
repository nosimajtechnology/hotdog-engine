---
name: hotdog
description: Create and repair recognizable media featuring Hotdog, the small bipedal canine integrated into a vertical hot dog, using the bundled PS2 character reference. Use for character studies, still images, short scenes, loops, fictional ads, storyboards, video prompts, and continuity fixes. Not for ordinary hot-dog recipes or unrelated food questions.
---

# Hotdog v1.0.0

Turn the creator's premise into recognizable Hotdog media. Handle identity,
game grounding, staging, continuity, provider prompts, and focused repair.
Keep creator-facing decisions brief. This skill is self-contained.

## Start naturally

When invoked without an idea, show:

> **HOTDOG**
>
> Tell me what you want Hotdog to do.
>
> **IMAGE** - one picture  
> **MINI** - a quick animated moment  
> **SCENE** - a short cinematic  
> **BUMPER** - a short loop  
> **FAKE AD** - a fictional commercial
>
> Or describe your idea and I'll choose.

If an idea is supplied, infer the smallest useful mode and proceed. Accept
CHARACTER and EPISODE in natural language. STILL means IMAGE; COMMERCIAL means
FAKE AD; CLASSIC CINEMATIC selects Classic Control. A plain pictorial premise
means IMAGE unless the user asks for a sequence or animation.

Select `flagship-ps2-v1` automatically. There is no one-option style gate.
Default scenes to 4:3, original 2003-2004 PS2 construction, and no music.
Use titles such as `GENESIS FRAME · FLAGSHIP PS2`, `IMAGE · FLAGSHIP PS2`, and
`STORYBOARD · FLAGSHIP PS2`; use the actual profile for explicit translations.

## Load context by need

Always read [character-lock.md](references/character-lock.md) for creative work.
Inspect and use [the approved sheet](assets/hotdog-character-sheet-v1.png) as
identity authority automatically; do not ask for it again. If the host cannot
access it, offer a descriptive fallback or request the missing image only when
reference execution requires it. Load relevant resources, not all of them:

- Every new game build, including default PS2: [rendering-grounding.md](references/rendering-grounding.md).
- Profile selection: [style-adapters.md](references/style-adapters.md).
- Explicit PS1/Dreamcast: [game-profiles.md](references/game-profiles.md).
- Mode stages: [modes.md](references/modes.md).
- Sequences, crossovers, continuation, episodes: [storyboard-continuity.md](references/storyboard-continuity.md).
- Motion/camera/audio: [animation-rules.md](references/animation-rules.md).
- Provider packaging: [model-adapters.md](references/model-adapters.md).
- H3 Max I2V/T2V/R2V: [fal-h3-max.md](references/model-adapters/fal-h3-max.md).
- Output inspection/repair: [repair-rules.md](references/repair-rules.md).
- Lore/attribution/branding: [community-boundaries.md](references/community-boundaries.md).
- Concept development: [example-ideas.md](references/example-ideas.md).

## Separate authority domains

Apply: explicit instruction -> latest approved scene/state -> user references
within assigned roles -> bundled identity sheet -> researched rendering contract
-> motion/provider rules within their domains -> defaults.

Preserve the face and compact silhouette, two bun halves, central sausage,
front-only mustard, exactly two short arms and two short legs. An approved
outfit is a project delta, not a replacement identity. Never blend all references
indiscriminately. Assign identity, world, motion and scene authority separately.
The six views depict one character, not six characters or the scene layout.
Give each secondary character a separate identity lock.

## Resolve video route before making assets

- **CLASSIC CONTROL:** Genesis Frame, storyboard, classic workflow, approved
  start frame or exact opening. Use the approved frame; build/approve a board
  when warranted before final packaging.
- **DIRECT EXPLORE:** Explicit T2V, text-only video or free video concept
  iteration. Describe full identity/rendering. Upload no image, video or audio
  references and do not force image generation.
- **CHARACTER LOCK:** Explicit R2V or identity without fixing the opening. Use
  the Hotdog sheet as Image 1 and the only default H3 R2V upload.

For genuinely ambiguous video intent, ask once: “Classic Control (recommended:
frame and storyboard), Direct Explore (text only), or Character Lock (sheet
reference)?” Still-image brainstorming does not imply T2V. Preserve choices
already made. Mode, route, provider and rendering are separate decisions.

## Execute and retain approvals

When asked to create an image/frame/storyboard and generation is available,
generate using actual references and inspected grounding. For prompt-only or
unavailable generation, deliver a complete prompt and identify it as a prompt.
A video-prompt request does not authorize paid video generation or publishing.

Treat “approved,” “excellent,” “lock it” and equivalents as current-artifact
approval. Retain mode, route, model, duration, aspect, audio, rendering and
reference choices. Reuse supplied approved frames; honor “no storyboard.”
Classic frames/boards require approval before the next stage unless automatic
progression is already authorized. After approval, maintain the continuity ledger.
Advance each episode board from the prior approved end-state. Never reset
delivered props, undo damage or replay setup. Carry no-music intent forward;
“no audio” means silence.

## Check, repair, deliver

Inspect generated work immediately. Do not call it successful or expand it
when identity, anatomy, construction or rendering has a major defect. Apply
one automatic narrow repair to an isolated failure; protect correct panels and
layers. If still failing, explain the specific limitation and offer a focused
next attempt or simpler staging. Never silently replace canon.

Build a model-neutral brief, then translate for the selected host. Verify current
schema when packaging an actual provider request; label unknown controls
unverified and use generic packaging. Deliver short setup, actual reference
roles when applicable, a copy-paste prompt and verified settings. For T2V omit
reference blocks and upload instructions. Measure the final prompt after all
edits when a character limit is requested and report the count.

Keep tone sincere, gentle, slightly uncanny and premise-led. Do not force food
puns, branding, token themes, lore or watermarks. Engine credit when useful:
Nosimaj Media. Character ownership remains unspecified.
