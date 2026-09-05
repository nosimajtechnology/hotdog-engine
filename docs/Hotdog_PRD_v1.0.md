# Hotdog

## Product requirements document

| Field | Decision |
| --- | --- |
| Product | Hotdog, a Nosimaj community creative engine |
| Skill name and package folder | `hotdog` |
| Display name | Hotdog |
| PRD version | 1.0 |
| Proposed initial skill version | 1.0.0 |
| Date | September 5, 2026 |
| Status | Implementation specification; skill has not been built or installed by this document |
| Character authority | User-approved six-view PS2 turnaround, reproduced below |
| Architecture baseline | Inspected Chihuahua Community Engine v0.7.1 and GIGA Community Engine v1.3.1 |
| Flagship visual style | Original PS2 game rendering |
| Excluded style families | Anime, Late-Z, battle-cel, OVA, and their style-specific assets and motion rules |

### Product objective

Build a self-contained skill that turns an ordinary idea into recognizable Hotdog media. The creator supplies the premise; the skill handles character identity, original-game grounding, composition, continuity, storyboards, model-specific prompts, and targeted repairs.

The user should not need to upload the character sheet repeatedly, describe Hotdog from scratch, know game-rendering terminology, or understand the package structure.

Use the current community-engine architecture with Hotdog-specific canon. Preserve its separation of identity, visual rendering, production format, creation route, motion, and provider packaging. Remove anime functionality throughout the package, rather than merely hiding it from the menu.

## 1. Architecture baseline and deliberate adaptations

The baseline is the installed source inspected for this PRD, not an independently audited public GitHub release. Different engines have different mode counts and shot defaults; Hotdog must use the explicit decisions below instead of copying conflicting defaults.

| Layer | Source to reuse | Hotdog decision |
| --- | --- | --- |
| Beginner entry and automatic routing | Chihuahua `SKILL.md` and `CINEMATIC_MODES.md` | Small primary menu; infer a mode from a clear idea |
| Character studies | GIGA `modes.md` | Add CHARACTER for turnarounds, portraits, and expression studies |
| Bundled character authority | Both engines | One approved Hotdog PS2 sheet, automatically available |
| Game grounding | GIGA `rendering-grounding.md`; Lost Game Engine grounding protocol | Ground every new game build, including an inferred/default PS2 build |
| Style registry | Both engines' style routers | Retain the modular layer; register PS2 only at launch |
| Adjacent game profiles | Chihuahua `LOST_GAME_STYLE.md` | PS1 and early-sixth-generation/Dreamcast interpretation on explicit request |
| Creation routes | Both engines' H3 Max adapters | Classic Control, Direct Explore, and Character Lock |
| Motion and provider separation | Both engines | Model-neutral brief first, then the selected provider adapter |
| Scene and crossover continuity | GIGA `continuity.md` | Per-character identity blocks and a persistent state ledger |
| Longer stories | GIGA episode workflow | Four progressive boards by default, available on request |
| Repairs | Both engines | Repair the smallest failed layer, with a bounded automatic retry |
| Anime adapters | Existing anime-specific modules | Exclude modules, assets, menus, examples, aliases, and inherited defaults |

Chihuahua currently makes some screenshot research conditional on an explicit game request. Hotdog adopts GIGA's stronger rule: the active game build triggers grounding regardless of how that build was selected.

Do not inherit GIGA-specific gym/culture modes, Chihuahua's durag, another character's anatomy, token identity, branded props, or character attribution.

## 2. Launch scope

### Required

- CHARACTER, IMAGE, MINI, SCENE, BUMPER, and FAKE AD workflows.
- EPISODE as an advanced natural-language route, without expanding the primary menu.
- Classic Genesis Frame -> approved storyboard -> animation-prompt workflow.
- H3 Max I2V, T2V, and R2V packaging, with route-specific reference behavior.
- Seedance, Kling, and generic provider adaptation using verified host capabilities.
- The approved PS2 sheet, character lock, game-grounding procedure, continuity ledger, and repair rules.
- Prompt-only operation when requested or when generation is unavailable.
- A PS2 style signifier on relevant production-stage titles.
- A small bank of Hotdog-specific example premises and a behavioral acceptance suite.

### Supported on request

- PS1 or early-sixth-generation/Dreamcast rendering translations using researched game evidence. These are adjacent game profiles, not pre-approved alternate canonical sheets.
- Crossovers, outfit additions, fictional products, expressiveness, and explicitly requested state changes.
- Different aspect ratios, shot counts, durations, audio choices, and reference assignments.

### Outside this release

- Anime styles, anime character sheets, broadcast-cel grounding, and anime motion presets.
- Default photographic, modern CGI, or PS3 transformations inherited from GIGA.
- Automatic creation of a website, public repository, token integration, or hosted generation service.
- Model training, fine-tuning, a 3D rig, or a claim that the reference sheet is an actual extracted game asset.
- Automatic video spending or publishing in response to a request for a prompt.

Future non-game requests remain explicit creative extensions. The skill must not claim that an excluded style is a registered or tested Hotdog capability, silently switch styles, or install an adapter without a separate request.

## 3. Canonical asset and identity

### Approved reference

![Approved Hotdog PS2 six-view turnaround](hotdog-character-sheet-v1.png)

The user's “Excellent” approval establishes this sheet as Hotdog's current visual authority. Bundle its bytes unchanged as `assets/hotdog-character-sheet-v1.png` during implementation. This PRD's companion image is an exact copy for the implementation handoff.

| Asset property | Value |
| --- | --- |
| Source generation | `exec-8a0a5f89-678e-4716-a22f-ae8a2806237a.png` |
| Dimensions | 1536 x 1024 |
| Color mode | RGB |
| Background | Plain white; no alpha transparency |
| Layout | Front, front three-quarter, profile, rear three-quarter, back, opposite profile |
| SHA-256 | `f85cf3e0b1ad946344a741ad3efc822ef286c78f9f9a4935392b37036567444e` |

The earlier checkerboard-background generation is a rejected intermediate and must not ship. Do not regenerate, smooth, upscale, or replace the approved sheet merely to package the skill. A future transparent version requires an actual alpha channel and an identity-preserving edit; a checker pattern is not transparency.

### Immutable default construction

| Feature | Canonical requirement |
| --- | --- |
| Overall form | Small upright bipedal canine integrated into a vertical hot dog; retain the sheet's compact scale and proportions |
| Face | Tan forehead, broad cream cheeks and muzzle, dark faceted nose, muted gray-violet eyes, gentle closed-mouth expression |
| Head placement | Face emerges from the upper front between the bun halves; head remains bounded by the bun silhouette |
| Bun | Two elongated golden-brown halves with pale inner edges; retain their depth, spacing, length, and polygon construction |
| Sausage | Dull brick-red vertical center, with a rounded exposed tip above the forehead |
| Mustard | One yellow sinuous stripe on the front below the face; maintain its placement and scale |
| Rear | Plain red sausage strip between golden bun backs; no rear face or rear mustard |
| Ears | Small tan triangular tips tucked behind the upper bun; visibility follows viewpoint and occlusion |
| Arms | Exactly two short tan arms with pale paw tips, emerging from the same positions as the sheet |
| Legs | Exactly two short tan legs with pale chunky paw feet and simple toe marks |
| Lower rear | Preserve the tiny pale nub shown in the sheet without enlarging it into a curled tail |
| Surface | Painted low-resolution color information, mildly angular meshes, simple game shading |

Do not replace Hotdog with an ordinary dachshund, generic Doge, quadruped wearing a costume, human in a hot-dog suit, long-limbed mascot, or modern toy render. Breed identification is not needed to preserve the approved face.

The bun and sausage are persistent identity geometry. Walking, reaching, turning, and sitting must not detach, exchange, duplicate, or dissolve them. The head and limbs articulate around this structure. Do not invent a zipper, straps, removable hood, or concealed human body.

### Permitted variation

Pose, expression, environment, activity, props, lighting, and camera can vary. Outfit additions are allowed when they preserve the silhouette and attachment logic. Major identity changes, bun removal, condiment changes, new anatomy, and costume replacement require an explicit creative request and must be recorded as a project-specific delta.

The neutral sheet is a reference pose, not a command to keep every scene motionless or expressionless. New expression studies must preserve eye scale, spacing, muzzle volume, and head-to-body proportions.

## 4. Authority and reference roles

Apply authority by domain, in this order:

1. Explicit user instruction.
2. Latest approved project frame and state for scene-specific continuity.
3. User-supplied references within their declared roles.
4. Bundled Hotdog sheet for underlying identity and construction.
5. Active rendering contract derived from inspected game references.
6. Selected motion profile and provider packaging rules within their own domains.
7. Defaults.

An approved outfit or scene does not silently replace the underlying face and body. A rendering reference cannot import its dog breed or character markings. A motion reference cannot import its character, palette, crop, text, or audio unless explicitly assigned those roles.

For a new scene, assign the sheet to identity, game evidence to rendering/environment construction, and any project image to its actual scene role. Never instruct a model to “blend all references.”

Treat the turnaround's six views as six rotations of one character. Prompts must prohibit reproducing the sheet layout, white background, or multiple Hotdogs in ordinary scenes. Additional characters receive separate identity blocks; they must not inherit Hotdog's bun, mustard, face, or limbs.

## 5. Rendering and grounding

### Flagship build

Use a coherent original PS2-era real-time game build, approximately 2003-2004, with 4:3 scene framing by default. The sheet establishes Hotdog's approved PS2 construction. Its landscape sheet layout does not set the aspect ratio of future scenes.

Use *Dog's Life* on PS2 as the initial canine mesh and diffuse-texture lineage. The inspected contemporary screenshots support modest polygon forms, painted facial detail, simple shading, and practical game environments. They are rendering evidence, not Hotdog identity. [Period screenshot source](https://games.kikizo.com/reviews/ps2/dogslife.asp).

For environments, choose a title appropriate to the seed. An explicit GTA San Andreas scene, for example, requires original PS2 GTA San Andreas evidence for that world; do not force every environment into Dog's Life or average unrelated games into generic low-poly imagery.

### Grounding procedure

Before the first image of a new game build:

1. Resolve the target from user instructions, approved project state, the premise, or the PS2 default.
2. Retrieve and visually inspect approximately three to five useful original-platform screenshots when available.
3. Cover relevant character construction, textures/materials, environment density, lighting, and camera behavior.
4. Select one dominant game lineage, with at most two close comparables when they clarify a specific limitation.
5. Assign narrow roles and derive a short internal rendering contract.
6. Generate, inspect identity and fidelity, and repair any decisive defect before advancing.

Exclude remasters, altered ports, texture packs, modern emulator enhancements, fan renders, promotional CGI, and AI-generated evidence. Extracted models can supplement screenshots when their game/platform provenance is credible. Environment images are unnecessary for a blank character study unless they clarify rendering.

Reuse the approved rendering contract during continuation and repair. Research again only for a changed target, a new visual build, or a failure that needs fresh evidence. If search or trustworthy evidence is unavailable, state that historical-profile fallback is being used and continue; never claim inspection that did not occur.

Store source links and observed traits. Do not redistribute third-party screenshots in the public skill package by default.

### Visible rendering requirements

- Build simple meshes with readable muzzle, bun-cap, limb, and paw planes.
- Use small diffuse maps and painted detail with filtering appropriate to the inspected build.
- Use vertex/baked lighting, broad highlights, and simple period-appropriate shadows.
- Keep environments modular with plausible asset density, skyboxes, foliage, and draw distance.
- Keep camera motion motivated and varied within original in-engine presentation.
- Avoid modern fur strands, bread microdetail, dense subdivision, PBR response, cinematic depth of field, and modern lighting that contradict the chosen evidence.
- Do not paste PS1 affine warping, vertex snapping, or severe dithering into PS2 by default.
- Do not create modern assets and disguise them with grain, blur, scanlines, or pixelation.

### Style selection

At launch, automatically select `flagship-ps2-v1`. Do not stop for a one-option style menu. Use stage titles such as `GENESIS FRAME · FLAGSHIP PS2` and `STORYBOARD · FLAGSHIP PS2`.

Keep a compact style/profile router so explicit PS1 or Dreamcast requests can receive appropriate game-grounding rules. If additional approved styles are introduced later, present those options after mode selection. No anime entry, alias, sheet path, preset, or fallback belongs in the launch registry.

## 6. Creator experience and production modes

On invocation without an idea, show:

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

If an idea is already supplied, infer the smallest useful mode and proceed. CHARACTER and EPISODE remain available through natural language. Treat STILL as IMAGE, COMMERCIAL as FAKE AD, and CLASSIC CINEMATIC as a request for Classic Control.

| Mode | Default output and scale | Workflow |
| --- | --- | --- |
| CHARACTER | One identity study; a sheet only when requested | Reference assignment -> study -> identity/render check -> targeted repair |
| IMAGE | One finished image | Idea -> grounding -> image -> check -> repair or variation |
| MINI | One clear action, 4-8 seconds, 1-3 shots | First frame/selected direct route -> compact motion plan -> provider prompt; skip a board for a one-take beat |
| SCENE | One event, usually 8-15 seconds and 4-6 connected shots | Idea -> route -> route-specific approvals and prompt |
| BUMPER | Six seconds when unspecified; one continuous take | Approved still -> micro-motion lock -> provider prompt; no mandatory board |
| FAKE AD | Usually 8-15 seconds with a readable fictional product | Concept -> script/narration if needed -> selected visual route -> animation package |
| EPISODE | Four progressive boards; optional fifth when justified | Compact episode map -> first-frame foundation -> approve each board and update ledger -> package clips |

Durations are creative defaults, not universal provider limits. If a requested duration is unsupported, explain the nearest supported option or a practical edit plan before generation. An explicit user duration or shot count overrides these defaults when feasible.

Offer at most three concepts when development is useful. A clear premise should receive one optimized direction. Do not force a user with a specific image request into a video questionnaire.

## 7. Video creation routes

Resolve route after mode and active build, before generating unnecessary assets.

| Route | Choose when | Main authority | Required behavior |
| --- | --- | --- | --- |
| CLASSIC CONTROL | User wants a Genesis Frame, storyboard, exact opening, or classic workflow | Approved scene frame plus storyboard planning | Create/approve frame, then board when warranted, then provider prompt |
| DIRECT EXPLORE | User explicitly wants T2V, text only, or free concept iteration | Complete textual identity and rendering specification | No uploaded references of any modality and no forced image generation |
| CHARACTER LOCK | User wants R2V or identity consistency without fixing the opening shot | Approved Hotdog sheet | Build a reference-driven video prompt without requiring a Genesis Frame |

When video intent is genuinely ambiguous, ask one compact question offering these three approaches, with Classic Control recommended. Do not ask again after the route is clear. A request to brainstorm images is not automatically a request for T2V.

Treat route, format, and provider as separate decisions. An explicit “no storyboard” overrides the usual Classic Control board step. A supplied approved frame becomes the starting authority without regeneration. A BUMPER remains a one-take workflow even if its provider supports multiple shots.

### H3 Max I2V

Use `minimax/h3-max/image-to-video`. For I2V, populate `image_url` with the approved Genesis Frame. Its aspect determines the generated video's aspect; `end_image_url` is optional when an ending frame has been deliberately approved. Do not omit the starting frame and still describe the request as I2V. [fal I2V schema](https://fal.ai/models/minimax/h3-max/image-to-video/api).

The approved storyboard controls shot sequence, geography, and action in the prompt. It is not uploaded as the literal opening frame by default. The character sheet is used to construct the Genesis Frame, not supplied through an invented extra I2V reference slot.

### H3 Max R2V

Use `minimax/h3-max/reference-to-video`. For ordinary flagship PS2 work, make the approved Hotdog sheet `Image 1` and the only default uploaded reference. It carries the character's identity and established PS2 asset construction; it does not specify the scene environment or opening frame.

This follows the existing engines' canonical-sheet PS2 route. It does not require copying their anime-specific single-sheet exception or any anime text.

Use an opening reference block equivalent to:

```text
#Image1 shows six views of the same Hotdog character. Use it as the authority
for his face, proportions, two bun halves, sausage, front mustard stripe,
short bipedal limbs, rear construction, palette, and PS2 asset treatment.
Keep one consistent Hotdog throughout. Do not show the reference sheet,
its white background, turnaround layout, or multiple copies of Hotdog.
```

Add another image, video, or audio reference only for a user-requested role, a necessary second character/prop/environment/motion authority, or a demonstrated narrow repair. Keep Hotdog first and describe only actual occupied slots. Raw grounding screenshots stay internal unless they are needed as a declared rendering reference.

The API identifies references by modality and list order. Match the host's displayed syntax while preserving order; `#Image1` is a prompt convention, not a universal API field. Select scene aspect explicitly so the landscape turnaround does not accidentally determine it. [fal R2V schema](https://fal.ai/models/minimax/h3-max/reference-to-video/api).

### H3 Max T2V

Use `minimax/h3-max/text-to-video` with no uploaded images, videos, or audio. Describe Hotdog's full protected identity and active game-rendering contract in words. Do not refer to an unseen sheet or include unused `Image 1` language. The current endpoint exposes explicit aspect-ratio selection including 4:3. [fal T2V schema](https://fal.ai/models/minimax/h3-max/text-to-video/api).

T2V explores interpretations; it does not establish a new canonical face automatically. If identity or anatomy drifts, recommend R2V. If precise composition or geography is the issue, recommend an approved-frame I2V route.

### Adapter implementation rules

Keep endpoint syntax, duration limits, resolution choices, reference budgets, and prompt expansion in the H3 adapter. Record a verification date and official source URLs. Validate current schema values when packaging for an actual host; do not turn a historical API snapshot into a permanent product claim.

Do not promise render speed, exact cut times, exact speech, or proven Hotdog consistency from capabilities observed with other characters. H3-specific Hotdog video validation is still required during implementation.

### Other providers

- **Seedance:** translate the approved storyboard or one-shot source into the selected host's reference workflow. Honor storyboard-only requests. Use additional identity references only when needed and supported.
- **Kling:** use character/Element binding and multi-shot controls only when verified for the selected host. Otherwise use an approved frame with a clear shot plan.
- **Generic:** use the strongest supported input authority. If ordered storyboard interpretation is uncertain, provide individual-shot prompts from the same lock.

The image-generation provider remains replaceable. The inherited classic flow uses an available image model for Genesis Frames and storyboards; identity rules must not depend on a fixed image-model version.

## 8. Motion, camera, and audio

Optimize a seed for an immediate readable hook, clear cause and effect, escalation, and a payoff. Preserve its premise and explicit constraints.

Hotdog's short arms, large bun torso, and short legs create specific staging limits:

- Place reachable handles and props within paw range; use two paws for larger objects.
- Clarify ownership and contact during a handoff before moving the camera.
- Use torso tilt, simple steps, head turns, and clear key poses rather than elastic stretching.
- Preserve bun depth and the front/rear distinction during rotations.
- Avoid packing running, spinning, grabbing, speaking, and prop transfer into one beat.
- Use a close-up, occlusion, or motivated cut when it clarifies an otherwise fragile action.

For H3 multi-shot scenes, prefer roughly four to five principal beats when appropriate to a 15-second idea. A requested six-shot board remains valid; count is not a reason to override the user's structure. Timing blocks must cover the whole duration without overlap. Timecodes express intent, not frame-exact guarantees.

For a rotation bumper, distinguish rotating the character from orbiting the camera. Use one continuous direction and specify one full rotation only when requested. Avoid checkpoints that cause stopping or snapping.

Default to no music. Ambience and sound effects may remain. Generate dialogue only when requested or part of an approved narration plan. `NO AUDIO` means silence. For exact commercial narration, support separate voiceover and omit that spoken script from the video prompt to avoid duplicate voices. Text/end cards are optional, not automatic.

## 9. Approvals and project state

Treat “approved,” “excellent,” “lock it,” and clear equivalents as approval of the current artifact. Retain the model, route, format, duration, and other choices already given. Do not re-ask them during continuation.

After a frame is approved, maintain this internal state:

```text
PROJECT: mode | route | duration | aspect
HOTDOG: identity asset/version | face | bun/sausage/mustard | limbs | pose | outfit
SECONDARIES: separate identity | position | outfit | condition
WORLD: location | time | weather | lighting | permanent changes
PROPS: owner | position | orientation | condition
GEOGRAPHY: camera side | screen direction | entrances | landmarks
ACTION: completed | current | unresolved | next event
BUILD: profile/version | source of selection | rendering contract
GROUNDING: inspected sources | assigned roles | limitations
REFERENCES: ordered inputs and individual roles
MOTION: profile | camera purpose | contact points
STATE CHANGE: pre-state | change-only delta | post-state
AUTHORITY: approved frame | approved board | approved final state
MODEL: provider/host | endpoint | fields | exact prompt limit
AUDIO: music | ambience/effects | dialogue/narration route
REPAIRS: failure | protected layers | attempted correction | outcome
```

For episodes, use Board 1 Hook + Setup, Board 2 Escalation, Board 3 Major Turn, and Board 4 Payoff. Every board begins from the prior approved end-state. Do not replay the setup, reset consumed props, undo damage, or change location without a transition. A fifth board is optional when it earns its place. Do not generate all boards in advance unless requested.

## 10. Quality checks and repairs

Inspect generated work immediately when returned. Tools may display an image before the skill can inspect it; the skill must still withhold claims of success and further expansion when a major defect is present.

| Priority | Check |
| --- | --- |
| Identity | Correct Hotdog face, scale, head placement, silhouette, colors |
| Anatomy | Two arms/two legs; stable paw form, limb length, ears, and attachments |
| Construction | Two bun halves, central sausage, front-only mustard, correct rear |
| Continuity | Same wardrobe, props, ownership, scene geography, and action progression |
| Rendering | Approved PS2 construction without modern material or density drift |
| Direction | Readable action, motivated camera, varied coverage, visible payoff |
| Artifact | Requested number of views/shots; no unwanted collage, text, background pattern, or duplicates |

A major identity/anatomy/construction error, a clear wrong-generation render, or multiple smaller fidelity failures prevents advancement. Apply one automatic narrow repair for an isolated defect. If it still fails, briefly describe the remaining issue and offer a focused next attempt or a simpler staging/route. Do not launch unlimited retries.

Use:

```text
LOCK:
[successful identity, rendering, staging, and project state]

CHANGE ONLY:
[specific failed feature, action, camera, or panel]

DO NOT CHANGE:
[protected layers]
```

Prefer fixing a failed panel to regenerating the whole storyboard. Whole-frame reconstruction is appropriate when both identity and rendering are fundamentally wrong. Never call a newly generated reference canonical without user approval.

## 11. Voice, identity claims, and community fit

Default creative tone: sincere, gentle, slightly uncanny, and absurd when the premise calls for it. This is a working direction inferred from the supplied scenes, not declared official lore. Support mundane jobs, surreal exploration, strange services, action, and quiet character moments without forcing food puns.

The phone and logo in the rear source are incidental scene props. They do not establish a required phone, sponsor, platform affiliation, token, or trading theme. Do not inject tickers, charts, return claims, branding, or finance jokes into ordinary prompts.

Credit the engine to Nosimaj Media if attribution is needed. Character ownership and any formal community attribution are unspecified here; do not copy another engine's character-credit sentence or invent a partnership. No automatic watermark.

## 12. Package specification

Use lowercase `hotdog` as the skill's frontmatter name. A proposed discovery description is:

```yaml
name: hotdog
description: Create and repair recognizable media featuring Hotdog, the small
  bipedal canine inside a vertical hot dog, using the bundled PS2 character
  reference. Use for character sheets, still images, short scenes, loops,
  fictional ads, storyboards, video prompts, and continuity fixes. Not for
  ordinary hot-dog recipes or unrelated food questions.
```

Keep `SKILL.md` concise and route to focused resources. The package must work without Chihuahua, GIGA, or Lost Game Engine being installed. Reuse their decisions by adapting the necessary instructions, not by leaving external filesystem dependencies.

| File | Responsibility |
| --- | --- |
| `SKILL.md` | Entry, mode/route inference, authority, approvals, minimal shared rules, resource links |
| `agents/openai.yaml` | Matching display name, description, and default prompt |
| `assets/hotdog-character-sheet-v1.png` | Exact approved visual authority |
| `references/character-lock.md` | Identity, construction, permitted changes, standalone T2V identity description |
| `references/rendering-grounding.md` | Research protocol, source roles, PS2 contract, fidelity check |
| `references/style-adapters.md` | PS2 launch registry and on-request adjacent game-profile routing |
| `references/game-profiles.md` | Compact PS1/early-sixth-generation differences loaded only when needed |
| `references/modes.md` | CHARACTER, IMAGE, MINI, SCENE, BUMPER, FAKE AD, and EPISODE behavior |
| `references/storyboard-continuity.md` | Shot construction, ledger, episode progression, crossovers |
| `references/animation-rules.md` | Model-neutral motion, audio, camera, and Hotdog contact/rotation logic |
| `references/model-adapters.md` | H3 routing plus concise Seedance/Kling/generic packaging rules |
| `references/model-adapters/fal-h3-max.md` | Endpoints, input roles, field verification, and route-specific prompt shapes |
| `references/repair-rules.md` | Failure priorities, narrow repairs, retry boundary |
| `references/community-boundaries.md` | Tone, optional attribution, incidental branding, unspecified lore |
| `references/example-ideas.md` | Small varied example bank that illustrates real routing differences |

Keep the PRD, acceptance records, release notes, and any distribution README outside runtime instructions. Add scripts only for a demonstrated recurring need. Avoid empty adapter directories, duplicated rules, and inherited files that no longer have a caller.

A future public repository and installed personal skill must share the same approved package/version. When implementation or distribution is requested, follow the host's current skill installation workflow, validate the actual installable package, and verify that its referenced assets are present. Public release and download links are separate delivery actions from writing this PRD.

## 13. Behavioral acceptance tests

These are implementation acceptance scenarios, not tests already executed. Routing checks can use prompt-only runs; visual and video tests require actual outputs. Record pass/fail, artifacts, and remaining limitations rather than claiming reliability from prompt inspection alone.

| ID | Test request or condition | Pass condition |
| --- | --- | --- |
| H01 | Invoke `@hotdog` with no idea | Shows the compact menu and invites an idea |
| H02 | “Make Hotdog waiting at a bus stop” | Infers IMAGE, selects PS2, grounds the new build, and creates one image without a style gate |
| H03 | “Canonical Hotdog turnaround, no scenery” | Uses CHARACTER; preserves the approved face/rear; reports actual white/alpha behavior correctly |
| H04 | “Hotdog turns his back to the camera” | No mustard or face on rear; correct bun spacing, ears, and short limbs |
| H05 | “Hotdog climbs three stairs” | Stable bipedal motion and bun depth; no added legs or quadrupedal transition |
| H06 | “Hotdog picks up a small parcel” | Plausible paw reach and contact without stretching arms or detaching bun geometry |
| H07 | “A four-second idle, no storyboard” | Uses the smallest one-take workflow; handles provider duration limits explicitly |
| H08 | “Six-second model-viewer bumper, one full turn” | One continuous rotation, consistent front/rear, no resets, no required contact sheet |
| H09 | “Classic 15-second cinematic” | Frame approval precedes board; board approval precedes final packaging |
| H10 | “Use this approved frame for H3 I2V, skip the board” | Uses that frame as `image_url`; no redundant frame or board generation |
| H11 | “H3 R2V, use only the Hotdog sheet” | One reference, sheet first; no phantom slots, copied sheet layout, or invented opening-frame lock |
| H12 | “Three H3 T2V concepts, no references” | Three distinct concepts, self-contained identity, no upload instructions or reference tokens |
| H13 | “Hotdog meets Chihuahua” | Independent character references and anatomy; no durag or bun transfer |
| H14 | “Fix only the extra arm in shot 3” | Preserves correct shots and repairs the named failure |
| H15 | “Continue Board 2 after the parcel was delivered” | Carries delivery forward; does not reset parcel ownership or replay setup |
| H16 | “PS2 GTA San Andreas street scene” | Uses original PS2 evidence for the named game while retaining Hotdog identity |
| H17 | “PS1 Hotdog loading screen” | Explicit adjacent profile, appropriate grounding, no silent replacement of base canon |
| H18 | “Use the bundled Late-Z style” | Correctly states it is not included; does not route to an inherited anime asset |
| H19 | “No music” then “continue” | Audio intent persists; effects/ambience remain available without adding a score |
| H20 | “Prompt only, under 3500 characters” | No generation; final delivered prompt is measured after edits |
| H21 | Search unavailable | Honest historical-profile fallback; no fabricated sources; useful output still delivered |
| H22 | Isolated install with only Hotdog package | All internal references/assets resolve without another engine installed |

Visual release checks must cover front, profile, rear, one prop interaction, and a multi-shot continuation. Before describing any H3 route as Hotdog-validated, review at least one actual Hotdog result for that route. Until then, distinguish supported prompt packaging from demonstrated character performance.

## 14. Implementation sequence and definition of done

1. Preserve the approved sheet and verify its checksum.
2. Adapt the shared architecture into a self-contained `hotdog` package.
3. Write Hotdog's identity, attachment, orientation, and repair rules first.
4. Implement PS2 grounding and the reduced style router; remove anime dependencies throughout.
5. Implement modes, route inference, continuity, and model-neutral motion.
6. Adapt and verify provider packaging; add the Hotdog-specific examples.
7. Validate frontmatter, metadata, links, assets, and absence of inherited character/style instructions.
8. Run the relevant acceptance scenarios and record actual visual/video limitations.
9. When implementation is requested, install through the current personal-skill workflow and verify the installed result.

The implementation is complete when Hotdog is discoverable by the requested name, uses its bundled approved sheet automatically, follows the selected workflow without redundant questions, preserves its construction through the acceptance cases, and contains no active anime adapter content or dependencies on other community-engine installations.

Prompt packaging and visual execution must be reported separately. A ZIP, installed skill, public repository, and release are different delivery states; none is implied merely by a local draft or this PRD.

## 15. Example concept bank

These are starter examples, not approved lore or finished generation prompts.

| Premise | Best route | What it exercises |
| --- | --- | --- |
| Hotdog waits at an empty bus stop while an impossibly small bus arrives | SCENE | Immediate scale joke, stable geography, visual payoff |
| Hotdog carries a parcel up a long staircase and finds another staircase behind the door | SCENE | Short-leg movement, prop ownership, causal reveal |
| Hotdog idles in a character-select viewer and slowly turns once | BUMPER | Full rotation and front/rear construction |
| Hotdog runs a late-night shoe-repair counter despite having no shoes | FAKE AD | Sincere absurd service, product handling, optional voiceover |
| Hotdog silently meditates in a sparse temple as a vending machine lights up behind him | IMAGE or MINI | Mood, source-inspired staging, small readable motion |
| Hotdog and another mascot trade identical empty briefcases | Crossover SCENE | Separate identities and unambiguous handoff |

## 16. Source notes

Architecture was derived from these installed source snapshots on September 4, 2026:

- **Chihuahua Community Engine v0.7.1:** `SKILL.md`, `STYLE_ADAPTERS.md`, `LOST_GAME_STYLE.md`, `CINEMATIC_MODES.md`, `MODEL_ADAPTERS.md`, and `model-adapters/fal-h3-max.md`.
- **GIGA Community Engine v1.3.1:** `SKILL.md`, `modes.md`, `rendering-grounding.md`, and `continuity.md`; its H3 route architecture corroborates the shared entrypoint behavior.
- **Lost Game Cinematic Engine v4.4 / core v4.4.0:** source already used for Hotdog's initial sheet, including screenshot grounding and reference/identity separation.
- **Hotdog identity:** the five user-supplied character images and the subsequently approved six-view PS2 sheet. The approved sheet is the implementation authority; the originals are provenance and optional repair evidence.
- **Provider verification:** official fal [I2V](https://fal.ai/models/minimax/h3-max/image-to-video/api), [T2V](https://fal.ai/models/minimax/h3-max/text-to-video/api), and [R2V](https://fal.ai/models/minimax/h3-max/reference-to-video/api) documentation inspected for this PRD. Host-specific controls and future changes still require verification at use time.

Open items do not block authoring the skill: formal character-credit wording, any official community link, future public repository/release destination, and measured Hotdog video performance. Leave unspecified claims absent and validate performance during implementation.
