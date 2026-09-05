# Production modes

Infer smallest useful mode; keep CHARACTER/EPISODE off the primary menu. Offer
at most three concepts when useful; optimize a clear premise into one direction.
Explicit duration, shot count, route and audio override defaults when feasible.

| Mode | Default | Execution |
| --- | --- | --- |
| CHARACTER | One study; sheet only if requested | Assign roles, reuse approved sheet when sufficient, otherwise ground/generate/check/repair |
| IMAGE | One picture | Idea, grounding, image, check, repair or variation |
| MINI | 4-8s; one action, 1-3 shots | Resolve route; one-take beat needs compact motion plan, no mandatory board |
| SCENE | 8-15s; 4-6 connected shots | Resolve route, readable hook/event/payoff, relevant approvals, package |
| BUMPER | 6s; one continuous take | Approved still or first-frame approval, micro-motion lock, provider prompt; no mandatory board |
| FAKE AD | 8-15s; readable fictional product/service | Concept, script/narration plan if used, selected visual route, package |
| EPISODE | Four progressive boards; optional fifth | Episode map, frame foundation, board approvals/ledger, per-clip packaging |

Durations are creative defaults, not provider limits. Verify before execution.
For unsupported duration, explain nearest option or edit plan first; never
silently turn a four-second request into 15 seconds.

## Classic Control

Use an available image model; no fixed version. Ground -> Genesis Frame ->
approval -> storyboard when warranted -> approval -> model-neutral brief ->
provider prompt. Reuse supplied approved frames/approvals. “No storyboard” removes
that step; one-take MINI/BUMPER never requires one. Prompt-only Classic work
delivers the requested stage prompt without claiming unexecuted images/approvals.

## Direct Explore / Character Lock

Direct Explore goes straight to text-only video prompt with no reference uploads
of any modality. Character Lock uses the sheet without an opening-frame gate.
Routes change input authority, not mode: an R2V bumper remains one take. A
text-only still brainstorm is not a video route. Read [model-adapters.md](model-adapters.md).

## Commercials / episodes

Treat a fictional product as real in-world. Use readable scale, simple paw
contact and sincere absurdity. Narration may be in-model, separate or absent;
prefer separate voiceover for exact words and omit its script from the video
prompt. No default narrator, end card, logo or watermark.

Board 1 Hook + Setup; Board 2 Escalation; Board 3 Major Turn; Board 4 Payoff.
Show a compact episode map. Generate/approve progressively unless all boards
are requested. Read [storyboard-continuity.md](storyboard-continuity.md).
