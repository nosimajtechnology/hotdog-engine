# Hotdog

An easy creative tool for making images and short videos with Hotdog, the small upright dog built into a hot dog.

You do not need to know prompting.

Tell the Engine what Hotdog is doing. It handles the character, old-game graphics, camera direction, storyboards, video prompts, and common repairs.

**[Download Hotdog](https://github.com/nosimajtechnology/hotdog-engine/releases/latest/download/hotdog.zip)** · **[All releases](https://github.com/nosimajtechnology/hotdog-engine/releases)**

## What you need

- **ChatGPT with Skills available** to install and use Hotdog.
- **Image generation** for pictures, first frames, and storyboards.
- **A separate video tool** to turn the prompts into video, such as fal.ai MiniMax H3 Max, Seedance, or Kling. Video tools and their credits are separate from the Engine.

The character reference is included. You do not need to install another community engine or write any code.

## Install and start

1. Download [hotdog.zip](https://github.com/nosimajtechnology/hotdog-engine/releases/latest/download/hotdog.zip). **Keep it zipped for import.** Choose this file from the release assets, rather than GitHub's source-code archives.
2. Open your ChatGPT **Skills** area and use its ZIP upload/import option to select the file. Some interfaces place Skills under **Plugins**. If your interface does not offer skill import, check the [official Skills guide](https://learn.chatgpt.com/docs/build-skills) for supported setup options.
3. Start a new chat and select **Hotdog** by typing `@`, or ask:

```text
Load the "Hotdog" skill.
```

Then describe your idea:

```text
Make an image of Hotdog waiting at an empty bus stop at night.
```

If the picture looks right, reply `Approved.` If something is off, say what to fix:

```text
He has an extra arm. Fix only that and keep everything else the same.
```

## What you can make

| Mode | What it makes |
| --- | --- |
| **IMAGE** | One finished picture |
| **MINI** | A quick animated moment |
| **SCENE** | A short cinematic with a setup and payoff |
| **BUMPER** | A short loop or character showcase |
| **FAKE AD** | A fictional commercial |

Name a mode or describe your idea and let the Engine choose. You can also ask for a character study, turnaround, or a longer episode.

Images are generated in the chat when image generation is available. For video, the Engine prepares the frames or references your chosen workflow needs, then gives you a prompt to use in your video tool.

## The look

**Original PS2 graphics are the default.** Expect simple geometry, painted low-resolution textures, sparse environments, and camera work inspired by early-2000s games. The Engine researches actual original-platform screenshots to guide each new game-style scene.

Scenes start in **4:3**, with **no music** unless you ask for it. Tell the Engine if you want a different format, duration, or audio direction. It checks what your chosen video tool supports.

You can request a specific PS2 game influence or a researched PS1 or Dreamcast translation. Hotdog's approved character design stays the starting point.

## Three ways to make a video

You can describe how you want to work in plain language:

| What you want | Workflow | What happens |
| --- | --- | --- |
| "Let me approve the opening image first." | **Classic Control / I2V** | Approve a first frame, then a storyboard when useful. The first frame becomes the video's opening image. |
| "Give me text-only video concepts." | **Direct Explore / T2V** | Get a complete video prompt with no reference uploads. Useful for trying ideas quickly. |
| "Use the character sheet as the reference." | **Character Lock / R2V** | Use the included Hotdog sheet as the only default reference for H3 Max, without fixing the opening composition. |

For your first video, start with **Classic Control**. Choose **Character Lock** when keeping Hotdog recognizable matters more than choosing the exact first frame. Text-only results can drift from his approved face and proportions.

Already have an approved frame? Attach it and ask to continue. You can also say `No storyboard` to skip that step.

## Need an idea?

Copy one of these and change anything you like:

```text
Make a short PS2 scene where Hotdog waits at a bus stop and an impossibly small bus arrives. No music.
```

```text
Make a fictional late-night ad for Hotdog's shoe repair service. He does not wear shoes.
```

```text
Make a six-second character showcase where Hotdog turns around once. Use the character sheet as the only reference.
```

Or ask: `Give me three ideas for Hotdog.` Browse more [starter ideas](hotdog/references/example-ideas.md).

## Character reference

This sheet is included with the Engine and used to keep Hotdog recognizable across scenes. Preserve his face, compact proportions, bun shape, front mustard stripe, two short arms, and two short legs. Explore different activities, expressions, props, and worlds.

![Hotdog PS2 character reference showing six views](hotdog/assets/hotdog-character-sheet-v1.png)

## Community use

Community-created scenes are unofficial and do not automatically become canon. Character ownership and formal community attribution are unspecified; the Engine does not imply a partnership or ownership claim.

Suggested engine credit:

> Made with the Hotdog Engine by Nosimaj Media.

Explore more creative tools at [nosimaj.com/tools](https://nosimaj.com/tools).

## For contributors

The complete installable skill lives in [`hotdog/`](hotdog/). See the [validation results and known limits](docs/ACCEPTANCE.md), [release instructions](docs/RELEASING.md), and [original PRD](docs/Hotdog_PRD_v1.0.md).

<details>
<summary>Development and release commands</summary>

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

Builds create `dist/hotdog.zip` and `dist/hotdog.zip.sha256`. Release automation validates and attaches both files when a version is released. A change to `hotdog/VERSION` on `main` triggers a release; documentation-only changes do not.

For a filesystem-based skill host, extract the `hotdog/` folder into its skills directory and invoke `$hotdog` where supported. See the host's installation instructions for the correct location.

</details>
