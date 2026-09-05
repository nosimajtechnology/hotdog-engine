# fal H3 Max

Verified 2026-09-05. Recheck for the actual host; observations are dated.
Official sources: [I2V](https://fal.ai/models/minimax/h3-max/image-to-video/api),
[T2V](https://fal.ai/models/minimax/h3-max/text-to-video/api),
[R2V](https://fal.ai/models/minimax/h3-max/reference-to-video/api),
[T2V machine schema](https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=minimax/h3-max/text-to-video).

## Inputs by route

| Route | Endpoint | Authority |
| --- | --- | --- |
| I2V / Classic Control | minimax/h3-max/image-to-video | Approved Genesis Frame in image_url; frame sets aspect; optional approved end_image_url |
| T2V / Direct Explore | minimax/h3-max/text-to-video | Full textual identity/rendering, no image/video/audio uploads; explicit aspect_ratio, normally 4:3 |
| R2V / Character Lock | minimax/h3-max/reference-to-video | reference_image_urls starts with Hotdog sheet, only default reference; explicit aspect_ratio, normally 4:3 |

I2V without `image_url` becomes text-to-video. Never omit the start frame for a
promised I2V. Storyboard controls sequence/geography in prose; do not upload it
as literal first frame by default. The sheet helps construct the frame; no
invented extra I2V identity slot.

R2V adds references only for explicit request, necessary second character/prop/
environment/motion, or demonstrated focused repair. Hotdog remains first.
Grounding screenshots remain internal unless a declared rendering input is
needed. Describe only occupied slots. The sheet does not lock the opening or
scene environment; choose explicit scene aspect instead of adaptive.
`#Image1` is a prompt convention, not an API field. Match the host's displayed
modality/order tokens; fal docs name Image 1, Image 2, Video 1, Audio 1.

## Dated settings

`prompt` and `prompt_expansion_mode` required. Documented expansion choices:
`balanced`, `quality`; do not invent `off`. Start with balanced unless otherwise
requested; inspect returned `expanded_prompt` for unrequested changes when
available. Resolutions: `480P`, `768P`. Set duration explicitly (default 5s).
T2V machine schema: integer 5-15 seconds, prompt maximum 50,000 characters.
Verify I2V/R2V bounds and host limits before execution; do not infer them from
T2V or director-session metadata. Four-second T2V: explain 5s then trim to four
or choose another host; do not submit an unsupported duration.

T2V aspect: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. R2V additionally offers adaptive.
Use deliberate scene aspect; a more limited host UI needs a compatible edit plan.

R2V lists: `reference_image_urls`, `reference_video_urls`, `reference_audio_urls`.
At most 12 files combined. Video/audio clips: 2-15s each, each modality totals
at most 15s. Audio cannot stand alone; include image or video. Budget capacity
is not a reason to add references. No separate music-disable control is assumed;
express intent in prose. Keep provider safety defaults. Do not infer camera or
frame-rate fields from unrelated API “Other types.”

## Prompt shapes

R2V opening:

```text
#Image1 shows six views of the same Hotdog character. Use it as the authority
for his face, compact proportions, two bun halves, sausage, front mustard
stripe, two short arms and two short legs, rear construction, palette and
PS2 asset treatment. Keep one consistent Hotdog throughout. Do not show the
sheet, white background, turnaround layout or multiple copies.
```

Then world/rendering contract, event/camera, timed beats, end-state and audio.
No phantom Image 2 and no opening-frame claim.

I2V: “Begin exactly from the approved input frame. Preserve Hotdog identity,
world, lighting, props and starting geography.” Then approved plan and end-state.
This applies to a scene frame, not the sheet.

T2V: include the full [standalone identity](../character-lock.md), world/rendering
contract, ordered action/camera and audio. No unseen-reference language or upload
instructions. For identity drift suggest R2V; precise geography suggests I2V.

Use readable hook/cause/payoff and manageable paw contact; contiguous timing,
usually 4-5 beats over 15s unless otherwise requested. No promises of speed,
exact cuts/speech or validated Hotdog results without actual reviewed videos.
