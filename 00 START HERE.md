# Wrench Tale Vault: Start Here

A worldbuilding vault for **Wrench Tale** (and its companion world **Sheed n' Shell**), built around two problems: keeping canon straight, and keeping spoilers straight.

## How the vault is organised
| Folder | What lives there |
|---|---|
| `00 Inbox` | Quick captures. Sort them weekly. |
| `01 Canon` | The truth of the world: characters, places, factions, technology, history, glossary. |
| `02 Story` | Spins (chapters), page notes, plot threads, the **Reveal Tracker**, decisions. |
| `03 Sheed n' Shell` | The companion world, kept separate. |
| `04 Substack` | Series plans, the calendar, a notes bank, spoiler rules, published posts. |
| `05 Art & Reference` | Design notes, model-sheet index, images. |
| `06 Production` | Critique findings, lettering/design standards, the verify list. |
| `99 Templates` | Note templates (set as the Templates folder). |

## The one habit that matters: `status`
Every canon note has these properties:

```yaml
type: character | place | faction | technology | ...
status: public | partly-revealed | unrevealed
first_appears: Spin 2, p.19
spoiler_risk: low | medium | high | very-high
```

- **public**: the comic has shown it. Safe to discuss.
- **partly-revealed**: some of it is on the page. Check the note's "Public" vs "Private" sections.
- **unrevealed**: canon only you know. Do **not** put it in public posts.

Many notes have two headings: **Public (shown in the comic)** and **Private canon (not yet revealed)**. Only the first is safe to publish.

See [[Reveal Tracker]] and [[Substack Spoiler Rules]] before every post.

## Suggested plugins
- **Dataview**: auto-lists (queries below).
- **Templater** (optional): richer templates than the core Templates plugin.
- **Canvas** (built in): relationship maps (family tree, Auction structure).
- **Excalidraw** (optional): diagrams such as the M.A.X.W.E.L.L. loop.

## Handy Dataview queries
Everything not yet fully public:
```dataview
TABLE type, status, spoiler_risk, first_appears
FROM "01 Canon"
WHERE status != "public"
SORT spoiler_risk DESC
```

All technology and its status:
```dataview
TABLE status, first_appears
FROM "01 Canon/Technology"
SORT file.name ASC
```

## Conventions
- Link with `[[` and `]]` double brackets. One idea per note.
- Cite pages as `Spin 2, p.24` (printed page numbers).
- Mark anything uncertain with **[verify]** and add it to [[Verify List]].
- Log decisions in [[Decisions Log]].

## Jump to
[[Reveal Tracker]] · [[G.I.M.M.E. System]] · [[City of Gears]] · [[R.I.S.E. Series]] · [[Publishing Calendar]] · [[Verify List]]