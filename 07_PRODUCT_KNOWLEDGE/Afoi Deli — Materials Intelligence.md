---
title: Afoi Deli — Materials Intelligence
aliases:
  - Materials Intelligence
  - Afoi Deli Materials
  - Material Vault Seed
tags:
  - materials-vault
  - afoi-deli
  - reference
type: MOC
status: draft
confidence: likely
created: 2026-06-16
updated: 2026-06-16
source: https://afoideli.gr/
---

# Afoi Deli — Materials Intelligence

> [!important] Build status — read this first (resume point)
> This is the **canonical index/bridge** for the materials layer. It is being progressively migrated into atomic `Material - <Name>` notes in `07_PRODUCT_KNOWLEDGE/Materials/`, deepest-first. The per-material prose below stays here as the working draft until each section is split out and **verified**.
> - **Method (re-runnable):** [[Materials Research Workflow]] — the repeatable skill. Raw inputs preserved verbatim in `Materials/_sources/` (the deep-research prompt + this file's seed draft).
> - **Field/ingestion contract:** [[Materials Schema]] — typed frontmatter, controlled vocabularies, Supabase mapping.
> - **Done (verified, atomic):** [[Material - Porcelain Stoneware]].
> - **Collections ingested (instance tier, born on ingestion):** [[Collection - Kronos Pierre Vive|Kronos Pierre Vive]] — the first collection note, 2026-06-17, against [[Collection Schema]] (the three-tier model now validated end-to-end).
> - **Next batch (deep):** Large-Format Porcelain Slab → Glass Mosaic → Sanitary Ceramic → SaphirKeramik.
> - **Open decisions for Orfeas** (see [[Session 2026-06-16d]]): (1) approve the Schema + Porcelain pattern; (2) batch size; (3) the ~22 split — Countertop → `sintered-stone`/`engineered-quartz`/`natural-stone`, and a `stainless-steel` note (QuadroDesign) split off from Brass.
> - **Naming:** atomic notes are `[[Material - <Name>]]`; the bare `[[Material name]]` links below are the seed's intended-graph and get repointed to the prefixed note as each is built.

> [!abstract] What this is
> A research-backed map of the **material classes** that sit underneath the eleven product categories sold by [Afoi Deli](https://afoideli.gr/). It is organised for the *materials vault*: each material below is written as a self-contained section with a consistent structure, so it can be split into its own note later.
>
> **Cross-references use `[[Wikilink]]` syntax anticipating that each material becomes its own note.** Until the split, they render as unresolved links — that is expected and shows the intended graph. The shared specification primer is linked in-file as `[[#Reading the specs]]`.
>
> **Research depth** is flagged per material (`Deep` / `Medium` / `Light`). `Light` sections are reliable on fundamentals but thinner on sourced detail — prioritise these for expansion.

> [!warning] Verification posture
> Technical claims (composition, standards, performance) are sourced and stable. **Brand → material mappings are the part to scrutinise** — I have asserted the well-documented ones and flagged the rest with a `To verify` callout. Confirm against current Afoi Deli stock and supplier technical sheets before this becomes canonical.

---

## Category → material map

The site's taxonomy is by *product*; the vault's unit is *material*. This table is the bridge.

| Afoi Deli category | GR | Items | Dominant material(s) |
|---|---|---:|---|
| Tiles | Πλακάκια | 502 | [[Material - Porcelain Stoneware|Porcelain Stoneware]], [[Large-Format Porcelain Slab]], [[Glazed Ceramic]], [[Glass Mosaic]] |
| Sanitaryware | Είδη Υγιεινής | 198 | [[Sanitary Ceramic]], [[SaphirKeramik]], [[Solid Surface Composite]] |
| Faucets / mixers | Μπαταρίες | 103 | [[Brass & Faucet Finishes]], stainless steel |
| Bathroom furniture | Έπιπλα Μπάνιου | 71 | [[Bathroom Furniture Materials]] |
| Mirrors | Καθρέπτες | 72 | [[Mirror Glass]] |
| Shower enclosures | Καμπίνες | 10 | [[Tempered Safety Glass]] |
| Wellness | Wellness | 35 | [[Wellness Materials]] |
| Radiators / towel warmers | Καλοριφέρ | 34 | [[Radiator & Towel-Warmer Materials]] |
| Shading | Σκίαστρα | 28 | [[Shading System Materials]] |
| Kitchens | Κουζίνες | 19 | [[Countertop Materials]], [[Bathroom Furniture Materials\|cabinetry]] |
| Parquet | Παρκέ | 64 | [[Wood Flooring & Parquet]] |

*Counts captured from the live product pages, June 2026.*

---

## Reading the specs

A primer shared by every ceramic/stone material below. When a material section says "see the primer," this is it.

> [!info] The two governing standards
> **ISO 13006** (international) and its European twin **EN 14411** classify ceramic tiles on **two axes**: forming method × water absorption.
> - **Forming method:** `A` = extruded, `B` = dry-pressed (dust-pressed under high hydraulic pressure). `A` is *not* superior to `B`; almost all wall/floor tiles are `B`, the exception being some extruded slabs.
> - **Water absorption (Eᵥ), measured by ISO 10545-3 (vacuum method):**

| Group | Water absorption Eᵥ | Common name |
|---|---|---|
| **Ia** | ≤ 0.5 % | **Porcelain stoneware** (the benchmark) |
| Ib | 0.5–3 % | Dense stoneware |
| IIa | 3–6 % | Stoneware |
| IIb | 6–10 % | Earthenware-grade |
| III | > 10 % | Porous (typical wall tile body) |

> [!note] So "porcelain" has a precise legal meaning
> A tile is **porcelain stoneware only if Eᵥ ≤ 0.5 %**, i.e. group **BIa** (dry-pressed) or AIa (extruded). The label always carries the group. Suffixes **GL** (glazed) and **UGL** (unglazed) follow the group code.

**The performance specs that decide where a tile can go:**

- **PEI abrasion (ISO 10545-7 / ASTM C1027)** — surface-glaze wear resistance, classes **0–5**. *Measures the glaze only, not strength, slip or absorption.*
  - `PEI 0` walls only · `PEI 1` very light (barefoot) · `PEI 2` light residential floors · `PEI 3` all residential + light commercial · `PEI 4` heavy residential + medium commercial (lobbies, restaurants) · `PEI 5` commercial/industrial (airports, hospitals).
  - **Full-body / unglazed porcelain has no PEI** — it uses **deep abrasion (ISO 10545-6)**, reported as volume removed in mm³ (lower = better; ~150 mm³ vs the 175 mm³ ceiling).
- **Slip resistance** — three parallel systems, **no exact conversion** between them:
  - **DIN 51130** ramp, *shod*, oil lubricant → **R9–R13** (R9 lowest, R13 highest). Rough guide: R9 dry interiors · R10 light-wet residential bath · R11 commercial wet · R12–R13 heavy wet/grease.
  - **DIN 51097** ramp, *barefoot*, water → **A / B / C** (A = dry/changing-room, B = shower & pool surround, C = sloped pool access & steps).
  - **ANSI A326.3 — DCOF** (dynamic coefficient of friction) → **≥ 0.42 wet** for level interior floors walked on when wet; ≥0.60 = high slip resistance. Higher DCOF generally = harder to keep clean.
- **Breaking strength / modulus of rupture (ISO 10545-4)** — porcelain typically **> 35 N/mm²**, often >40.
- **Mohs hardness** — scratch resistance of the surface (glazed tiles ~5–7; full-body porcelain high).
- **Other ISO 10545 parts:** -9 thermal shock · -12 frost resistance (critical for exterior in Athens winters, though mild) · -13 chemical resistance · -14 stain resistance.

---

# CERAMIC SURFACES (the core of the house)

## Porcelain Stoneware
> [!example] Snapshot
> **Class:** Vitrified ceramic · **AKA:** Gres porcellanato, porcelain tile, full-body/glazed porcelain · **Afoi Deli category:** Tiles · **Group:** BIa (Eᵥ ≤ 0.5 %) · **Research depth:** Deep
> **Key brands here:** Atlas Concorde, Florim, Marazzi, Mutina, Cedit, Marca Corona, Cotto d'Este, Iris, Emil/Ergon, Sant'Agostino, Cerdomus, Del Conca, La Fabbrica, Lea, Piemme, Italgraniti, Provenza, ABK, Ariana, Flaviker, Cir, Imola, Panaria + most of the tile roster.

**Composition & manufacture.** A ceramic body enriched with **fluxes — primarily feldspar** — plus refined clays, kaolin, quartz/sand and ceramic pigments. Raw materials are **wet-ground**, spray-dried to a granulate, then **pressed under very high pressure** (hydraulic presses, ~400–500+ kg/cm²) and **fired above 1200 °C**. The flux melts into a glass phase during firing that fills nearly all pores (vitrification), driving water absorption below 0.5 % and producing high mechanical strength (>40 N/mm² typical). This near-zero porosity is also what makes it **frost-proof, stain-resistant and chemical-resistant**.

**Sub-types (the distinction clients ask about):**
- **Full-body / technical porcelain (gres tecnico, *tutta massa*)** — colour and structure run **all the way through**. No glaze to wear off, so it outlasts even a glazed PEI 5 tile in punishing traffic; rated by **deep abrasion (ISO 10545-6)**, not PEI. The honest, raw, architectural look.
- **Glazed porcelain (gres smaltato)** — porcelain body with a fired surface glaze carrying the decoration. Vastly wider design range (digital inkjet printing) and the realistic marble/stone/wood/concrete looks; rated by **PEI**.
- **Colored-body porcelain** — a middle path: the body is tinted close to the surface colour so chips are far less visible than on a white-body glazed tile.

**Decoration.** Modern looks are produced by **digital inkjet printing** over the pressed body, often combined with structured/synchronised surfaces (the texture follows the printed graphic) and reactive glazes for depth.

**Formats & finishes.** Vast: 60×60, 60×120, 30×60, 20×20 décor, plank formats for wood-look, up to large slabs (see [[Large-Format Porcelain Slab]]). Thicknesses commonly **8.5–10 mm**, with **20 mm ("2.0")** pavers for outdoor dry-lay/raised floors. Finishes: matte/natural, polished (lappato/levigato), structured, soft/silk, anti-slip (R10–R12), bush-hammered for exteriors.

**Applications.** Floors and walls, residential to heavy commercial, **indoor and outdoor**, façades, pool surrounds, worktops. The default workhorse of the showroom.

**Care.** Effectively maintenance-free; neutral cleaners. Polished surfaces can show limescale/etch-like marks from hard water and need more attention than matte.

> [!question] To verify
> Which brands in stock are sold predominantly as **full-body** vs **glazed** (drives the PEI vs deep-abrasion conversation). Confirm 20 mm outdoor ranges actually carried.

---

## Large-Format Porcelain Slab
> [!example] Snapshot
> **Class:** Vitrified ceramic (thin/large) · **AKA:** Gres laminato, thin porcelain tile (TPT), porcelain slab, "lastra" · **Afoi Deli category:** Tiles / Kitchens (worktops) · **Research depth:** Deep
> **Key brands here:** **Cotto d'Este (Kerlite)**, Florim, Lea, Atlas Concorde, ABK, Italgraniti, Mutina, La Fabbrica (and Laminam-type slabs generally).

**What makes it distinct.** Same porcelain chemistry as [[Material - Porcelain Stoneware|Porcelain Stoneware]] but in **very large sheets at minimal thickness** — a different product form with its own engineering. Pressed at enormous force (Kerlite is pressed at ~15,000 tonnes), fired ~1200 °C, and frequently **reinforced on the back with fibreglass mesh** for handling and flexural safety.

**Thicknesses & formats.**
- **Kerlite (Cotto d'Este):** 3.5 / 5.5 / 6.5 mm.
- **Laminam-type:** 3, 5, 5.6, 12, 20 mm; slabs up to **1620 × 3240 mm** (≈5×10 ft).
- The 3 mm classes are for **walls/cladding/furniture only**; ~5.6 mm+ for floors; 12–20 mm for **worktops**.

**Why it's specified.** Minimal joints → the seamless, continuous look of modern minimalism; light weight; **installs over existing surfaces** (renovation/fast-track); non-porous and hygienic (fewer joints for bacteria — relevant in kitchens, clinics). As a **worktop** it is heat-, scratch-, stain- and UV-stable (see comparison in [[Countertop Materials]]).

**Applications.** Walls, floors, **ventilated façades**, furniture surfaces, countertops, splashbacks, fireplace surrounds, outdoor (UV/frost stable).

> [!question] To verify
> Confirm Kerlite thickness ranges and whether worktop-grade (12–20 mm) slab is offered for the Kitchens category, or only cladding-grade.

---

## Glazed Ceramic
> [!example] Snapshot
> **Class:** Porous/dense glazed ceramic (non-porcelain) · **AKA:** Monocottura, bicottura, majolica, faience, white-/red-body wall tile · **Afoi Deli category:** Tiles · **Research depth:** Medium
> **Key brands here:** Equipe, Wow, Cerasarda, Settecento, La Faenza, Gambini, Peronda, parts of Marca Corona / Imola décor lines.

**Composition & manufacture.** A clay body (white "faience" or red terracotta-type) shaped by dry-pressing and finished with a **fired glaze** that carries colour and pattern. Two classic firing routes:
- **Bicottura (double-fired)** — body fired first, glaze fired second; glossy, decorative **wall** tiles, lower strength.
- **Monocottura (single-fired)** — body and glaze fired together; denser and stronger, usable on some floors.

Higher water absorption than porcelain (typically groups **BIIa / BIII**), so generally **interior, lower-traffic** — but this body is exactly what gives the **handcrafted, glossy, characterful** looks (Zellige-style, majolica, hand-pressed reliefs, colour-pop fields) that porcelain can only imitate. Surface decoration ranges from glossy crackle glazes to relief and hand-decorated tiles.

**Formats & finishes.** Small formats dominate — subway/metro, 10×10, 13×13, hexagons, scales/fish-scale, decorative borders; glossy, crackle, satin, hand-painted.

**Applications.** **Walls, backsplashes, feature areas.** Most carry low/no PEI → not for floors unless the specific tile says so. See [[#Reading the specs]] for PEI.

> [!question] To verify
> Which of Equipe / Wow / Cerasarda lines are floor-rated vs wall-only. Clarify whether any Cerasarda ranges are true majolica vs porcelain.

---

## Glass Mosaic
> [!example] Snapshot
> **Class:** Vitreous glass (and enamel) · **AKA:** Smalti, Venetian/Murano glass mosaic, tesserae · **Afoi Deli category:** Tiles · **Research depth:** Deep
> **Key brand here:** **Bisazza** (signature line).

**What it is.** Mosaic of small glass tiles — **tesserae** — fused from a glass base (silica + soda/lime fluxes) coloured by **metal oxides that fuse completely into the glass**, so colour is through-body and lightfast. Distinct from ceramic mosaic in both material and craft lineage (Byzantine/Venetian).

**Bisazza's material families (from their technical data sheets):**
- **Smalto / sintered glass enamel** — through-body coloured, **sintered** glass enamel; far more durable than standard vitreous glass, rated for **floors and high-traffic, indoor & outdoor**. The matte version is also **non-slip** → pool borders and spa floors.
- **GLOSS / GLOW** — opaque base colours from fused oxides with an **iridescent** surface coating applied while incandescent (GLOW adds a wavy, light-catching texture).
- **LE GEMME (aventurine)** — the centuries-old Murano **aventurine** technique: enamel granules + copper crystals + metal oxides give an internal golden "flamed" sparkle.
- **OPERA** — translucent glass with deliberately **uneven colour distribution**, every tessera unique.
- **ORO / ORO BIS (gold-leaf)** — **24 kt gold leaf** (or a gold/white-gold alloy) **encapsulated between two glass layers** — the luxury Byzantine technique; hand-beaten Venetian gold.

**Formats.** Typically 10×10, 20×20 mm tesserae on sheets/mesh backing; 50×50 mm tiles; plus mosaic **artworks, patterns and made-to-order murals** (Bisazza's atelier work).

**Applications.** Walls, pools/spa, hammam, feature surfaces, decorative bands. Material is hygienic and chemically stable; mesh-backed sheets ease installation.

> [!tip] Why it's a margin/identity line
> Glass mosaic — especially gold-leaf and aventurine — is a story-and-craft product, not a commodity. It anchors the premium/atelier narrative.

---

# SANITARYWARE & BATHROOM MASS

## Sanitary Ceramic
> [!example] Snapshot
> **Class:** Whiteware ceramic (slip-cast) · **AKA:** Vitreous china, fine fireclay, sanitaryware ceramic · **Afoi Deli category:** Sanitaryware · **Research depth:** Deep
> **Key brands here:** Cielo, Flaminia, GSI, Galassia, Scarabeo, Catalano-class peers, Laufen (standard ranges).

The two traditional masses every premium maker chooses between:

**Vitreous China (VC).** Body of **clay + kaolin + feldspar + quartz**, slip-cast into plaster moulds, glazed, and **fired ~1200 °C** until almost all open pores vitrify → **water absorption ≈ 0**, glossy, hyper-hygienic surface. Ideal for **WCs, bidets, urinals, washbasins**. Soft, round, flowing shapes are easy. **Limits:** shrinkage during drying/firing is hard to control, and it **sags on very large parts** — conventional walls are ~**7–12 mm** thick for strength. Flexural strength ~400–800 kgf/cm².

**Fine Fireclay (FFC).** The classic slurry is stabilised with **pre-fired/calcined clay (chamotte)** — often **>40 % of the body**. The chamotte controls shrinkage, allowing **large pieces** (double basins, floor-standing pedestals, big vessels). Coarser body, thicker walls, but the only route to scale in traditional ceramic.

**Applications.** All WCs, basins, bidets, urinals; FFC where size demands. For the radically thin look, see [[SaphirKeramik]]; for moulded organic basins/tubs, see [[Solid Surface Composite]].

> [!question] To verify
> Map which of Cielo / Flaminia / GSI / Galassia / Scarabeo ranges are VC vs FFC. Note **Geberit** here is **flush/cistern/installation systems**, not a ceramic body (see appendix).

---

## SaphirKeramik
> [!example] Snapshot
> **Class:** High-strength engineered sanitary ceramic (patented) · **AKA:** Sapphire ceramic · **Afoi Deli category:** Sanitaryware · **Research depth:** Deep
> **Key brand here:** **Laufen** (proprietary; since 2013).

**What it is and why it matters.** A Laufen-developed ceramic that adds the mineral **corundum** (the hard component of sapphire — hardness second only to diamond, also used for watch crystals) to the body. The result: **flexural strength averaging > 120 MPa** — measured by Germany's BAM institute as **comparable to carbon steel and roughly twice that of vitreous china**.

**The design consequence.** That strength permits **wall thicknesses of just 3–5 mm and edge radii of only 1–2 mm**, where conventional VC needs 7–8 mm. This is what enables the **wafer-thin, knife-edge basin** silhouettes (the Kartell-by-Laufen / Val aesthetic). It is also **insensitive to abrasive cleaners and mechanical abrasion**, lighter, and more material-/energy-efficient (less raw material, lower transport weight). It still uses the **traditional slip-casting process**. Awarded the Swiss Design Prize 2017/18.

**Applications.** Designer basins, slim WCs and shelves where thin edges and tight radii are the point.

> [!tip] Selling line
> "Twice the strength of normal ceramic, edges as thin as 1–2 mm." Pure design-tech differentiation — a reason to specify Laufen over a generic VC basin.

---

## Solid Surface Composite
> [!example] Snapshot
> **Class:** Mineral-filled cast composite (solid surface) · **AKA:** Cristalplant, Corian, Ceramilux, Flumood, Livingtec, etc. · **Afoi Deli category:** Sanitaryware (basins, baths, shower trays) · **Research depth:** Deep
> **Key brands here:** **Antonio Lupi** (Cristalplant, Flumood), **Cielo** (Ceramilux), plus solid-surface tubs/trays across the bath roster.

**What it is.** A homogeneous, **non-porous cast composite** of a binding **resin + mineral filler**, pigmented, that can be moulded into seamless organic shapes, **thermoformed**, joined invisibly, and **repaired/renewed by sanding**. The genre DuPont created with **Corian**.

**The materials you'll meet:**
- **Corian** — the original: **~1/3 acrylic resin (PMMA) + ~2/3 natural minerals** (alumina trihydrate, ATH, from bauxite). Non-porous, repairable, warm to touch, translucent in thin sections.
- **Cristalplant** (Antonio Lupi) — markets itself as the **only bio-based solid surface**, with **resin derived from corn**; bath versions ~**30 % lighter** than rivals; the 2020 formula adds **virucidal/antifungal/self-cleaning** properties; GREENGUARD/LEED-credited. Used 20+ years for shower trays, basins, baths.
- **Ceramilux** (Cielo) — Cielo's solid-surface for slim basins/trays that pair with their ceramic ranges.
- **Flumood** (Antonio Lupi), **Livingtec**, **Korakril**, **Tecnoril**, **Pietraluce**, **Marmoresina**, **HIMACS**, **Akron** — sibling branded composites you'll see on spec sheets; same family, different recipes/owners.

**Properties.** Non-porous (hygienic, stain-resistant), warm and matte, seamless integration of basin-to-counter, **field-repairable** (sand out scratches), matte or satin. Heat tolerance is lower than ceramic/sintered stone — protect from very hot pans/objects.

**Applications.** Freestanding & built-in **bathtubs**, **washbasins**, **shower trays**, integrated counters.

> [!question] To verify
> Lock the brand→material pairs: Antonio Lupi = Cristalplant + Flumood; Cielo = Ceramilux (+ Pietraluce / Cementile?). Note any baths/trays sold in **acrylic** or **enamelled steel** instead (different material — see [[Wellness Materials]] / appendix).

---

# METAL FITTINGS

## Brass & Faucet Finishes
> [!example] Snapshot
> **Class:** Copper-zinc alloy + surface finish · **AKA:** Tapware, mixers, brassware · **Afoi Deli category:** Faucets/mixers · **Research depth:** Deep
> **Key brands here:** **Fantini, Fima Carlo Frattini, Zucchetti, Treemme (3MME), Nicolazzi, Fontealta**; **Quadro (QuadroDesign)** likely **stainless steel** — verify.

**The body: brass.** Premium taps are **solid brass** (copper + zinc), chosen for castability, machinability and corrosion resistance. The quality marker is **DZR (dezincification-resistant) brass** — alloyed (small As/Al additions) so acidic/hard water can't selectively leach the zinc and leave a porous, weak structure. Modern bodies are also **low-lead** to meet potable-water standards (**NSF/ANSI 61 & 372**, EU equivalents; ≤0.25 % lead weighted average).

**The finish (where durability and look are decided):**
- **Chrome electroplating** — the classic. On brass the stack is typically **nickel → chromium** (chromium is the thinnest top layer). Mirror-bright, corrosion- and varnish-resistant; the long-standing default.
- **PVD (Physical Vapour Deposition)** — vacuum process (**sputtering** or arc deposition) that bonds a hard ceramic-metallic film (e.g. **zirconium nitride** for brass/gold tones) at the molecular level. **10–20× more scratch-resistant** than electroplated chrome (Vickers HV-2600+), superior corrosion and **colour stability**, and it unlocks colours not found in nature (matte black, gun metal, copper, gold, brushed/satin variants). Higher cost. This is the technology behind the **PVD Copper / Matte Gun Metal / brushed brass** finishes specified on premium projects.

**Applications.** Basin/bath/shower mixers, spouts, shower systems, progressive/thermostatic cartridges (ceramic-disc internals).

> [!question] To verify
> Confirm **Quadro = QuadroDesign = stainless steel** (a genuinely different material story — corrosion-proof through-body, no plating to fail). Catalogue which finishes are **PVD** vs electroplated per brand for the finish-durability conversation.

---

# WOOD, GLASS, STONE & THE REST

## Wood Flooring & Parquet
> [!example] Snapshot
> **Class:** Solid & engineered timber · **AKA:** Parquet, hardwood flooring · **Afoi Deli category:** Parquet · **Research depth:** Deep
> **Key brands here:** **Bassano Parquet, Original Parquet** (and Provenza wood-look porcelain, which is *not* wood — keep separate).

**The two constructions:**
- **Solid parquet** — solid timber blocks/boards through-and-through. Maximum sandings/lifespan; **moves with humidity** (expands/contracts), generally **not recommended over underfloor heating**; usually **site-finished** (sanded + finished after laying).
- **Engineered parquet** — a **real hardwood wear layer (commonly oak)** bonded to a **multi-ply/plywood core**. The cross-laminated core resists expansion/contraction → **stable, suitable for underfloor heating and apartments**; usually **factory pre-finished** with multiple coats of UV-cured lacquer or oil (tough, consistent, walk-on-immediately).

**Species & grading.** **European oak** dominates; grade (Prime/Select → Rustic) describes the amount of knots/sapwood/colour variation, not quality. Reclaimed and smoked oak for character.

**Finishes (the look-and-feel decision):**
- **Oiled** — penetrates the wood, **matte/natural** feel, "bare wood" look, **spot-repairable**, periodic re-oiling.
- **Lacquered** — a surface film, **more protective for high traffic**, easier to clean, higher sheen (matte→gloss); "invisible/natural" lacquers mimic raw wood.
- **Surface textures:** brushed (raises grain), hand-scraped, smoked, white-/grey-oiled.

**Patterns.** Plank, **herringbone**, chevron, large-format boards. Herringbone/chevron read as design features; pre-finished engineered battens speed installation.

**Applications.** Living areas, bedrooms; engineered + UFH for modern apartments; **not** wet rooms (use wood-look porcelain there).

> [!question] To verify
> Confirm Bassano / Original Parquet ranges are engineered vs solid, dominant species, and stocked finishes (oil vs lacquer). Note acoustic underlay offering for apartments.

---

## Tempered Safety Glass
> [!example] Snapshot
> **Class:** Thermally toughened soda-lime glass · **AKA:** Toughened glass, ESG · **Afoi Deli category:** Shower enclosures (also underpins [[Mirror Glass]]) · **Research depth:** Deep
> **Key brands here:** **Glass 1989**, plus enclosure/wellness ranges using toughened glass.

**How it's made & why it's safe.** Annealed **float glass** is heated **> 600 °C** then **rapidly quenched**; the surfaces lock into **compression** while the core stays in tension. Results: **~4–5× the strength** of annealed glass of equal thickness, high thermal-shock tolerance (withstands ~220–250 °C swings), and on failure it **shatters into small blunt cubes** rather than shards — hence "safety glass." **All cutting, drilling, notching must happen *before* tempering** (you cannot machine it afterward).

**Standards.** **EN 12150** (CE, European safety glass), BS 6206, SGCC. Thicknesses for enclosures: **6 / 8 / 10 mm** (4 mm entry). 6 mm = versatile framed; 8 mm = the frameless sweet spot; 10 mm = architectural, heaviest/most rigid.

**The coating that matters.** Factory **anti-limescale / "easy-clean" nano coatings** (hydrophobic) make water **bead and run off**, resisting limescale, soap and streaks — the single most relevant spec for hard-water Athens bathrooms. **Frameless** designs also avoid metal frames where soap/mould/rust accumulate.

**Supporting metal.** Enclosure profiles/hinges in chrome, matte black, brushed brass, gun metal (anodised/coated aluminium or plated brass).

**Applications.** Shower enclosures, walk-in/wet-room screens, partitions.

> [!question] To verify
> Standard glass thickness offered (8 mm?), whether anti-limescale coating is standard or upgrade, and frame finish range.

---

## Mirror Glass
> [!example] Snapshot
> **Class:** Silvered float glass (+ integrated lighting) · **AKA:** Bathroom mirror, LED mirror · **Afoi Deli category:** Mirrors · **Research depth:** Light
> **Key brands here:** Antonio Lupi, Inda; **Luminor** (LED mirrors — verify); brand mirrors across furniture lines.

**Material.** Polished **float glass** with a rear **silvering** layer (silver + protective copper/paint backing). Bathroom-grade adds **moisture-resistant backing** and, increasingly, **integrated LED lighting**, anti-fog **demister pads** (heated film behind the glass), touch/sensor switches, and magnifying inserts. Frames (if any) in aluminium, brass or the furniture's material.

**Applications.** Above-basin mirrors, mirror cabinets, backlit/illuminated designer mirrors.

> [!question] To verify
> Confirm Luminor = LED mirror brand. Catalogue which mirrors include demister/LED/sensor features (the spec that justifies price).

---

## Countertop Materials
> [!example] Snapshot
> **Class:** Engineered & natural slab surfaces · **AKA:** Worktops, kitchen tops · **Afoi Deli category:** Kitchens · **Research depth:** Deep
> **Key brand here:** **Scavolini** (kitchens). Worktop material is usually specified separately.

The four contenders, by material logic:

- **Sintered stone** — natural minerals compressed and **fired at high heat (sintering)**, usually **resin-free**, **very low porosity**. Best **heat & UV stability**, scratch-resistant, indoor/outdoor, large slabs with vein-matching. (Porcelain slab — see [[Large-Format Porcelain Slab]] — belongs to this performance class.)
- **Engineered quartz** — **~85–95 % crushed quartz + 5–15 % polymer resin** + pigments. **Mohs ≈ 7**, non-porous, no sealing, huge colour/pattern range, consistent. **Caveat:** the **resin is heat- and UV-sensitive** → not ideal outdoors or under very hot pans.
- **Natural stone:**
  - **Granite** — igneous (quartz + feldspar + mica), very hard, **heat-resistant**, unique; **needs periodic sealing** (porous).
  - **Quartzite** — metamorphic, **Mohs 7**, silicate so **acids don't etch**; harder than granite; premium; seal. (Beware "soft quartzite" mislabelled marble-like stone at Mohs 5–6.)
  - **Marble** — beautiful but **porous and acid-sensitive (etches)**; high maintenance; sealing essential.

**Decision heuristic.** Heat/outdoor/UV → **sintered stone/porcelain**. Low-maintenance consistency indoors → **quartz**. Natural character + heat → **granite/quartzite**. Statement luxury, accept patina → **marble**.

**Cabinetry** (Scavolini bodies/fronts) shares the [[Bathroom Furniture Materials]] palette: lacquer, melamine/laminate, veneer, glass, increasingly porcelain-clad fronts.

> [!question] To verify
> Which worktop materials Afoi Deli actually supplies with Scavolini (porcelain slab via the tile side is a natural cross-sell). Confirm whether natural stone is offered at all or only engineered/sintered.

---

## Bathroom Furniture Materials
> [!example] Snapshot
> **Class:** Panel & coating composites · **AKA:** Vanity units, washstands, storage · **Afoi Deli category:** Bathroom furniture · **Research depth:** Light
> **Key brands here:** Antonio Lupi, Inda, Novel, Harmony, Cesi (verify each).

**Materials & why.** Bathroom furniture lives in humidity, so substrate and edge-sealing matter:
- **Lacquered MDF/board** — sprayed matte/gloss lacquer over moisture-resistant MDF; the premium designer look, broadest colour range; edges fully sealed.
- **Melamine / laminate (incl. HPL)** — resin-impregnated decorative surface over board; durable, water- and scratch-resistant, cost-effective; realistic wood/stone décors.
- **Real-wood veneer** — thin hardwood face over board; natural grain, warmth.
- **Solid wood / metal frames / glass** — accents and structure.
- Pairs with [[Solid Surface Composite]] or ceramic **integrated tops**.

**Applications.** Wall-hung & floor vanities, tall units, open shelving, washstands.

> [!question] To verify
> Identify Novel / Harmony / Cesi as furniture vs accessories, and which lines are lacquer vs melamine vs veneer. (Inda is largely **accessories + mirrors**.)

---

## Radiator & Towel-Warmer Materials
> [!example] Snapshot
> **Class:** Steel / aluminium / brass heat emitters · **AKA:** Designer radiators, heated towel rails, scaldasalviette · **Afoi Deli category:** Radiators · **Research depth:** Light
> **Key brands here:** **Tubes Radiatori, Scirocco H** (Italian designer radiators).

**Materials & trade-offs:**
- **Steel (mild/carbon)** — most designer radiators; holds heat well, infinite forms, powder-coated/electro-coated in any colour/finish; the medium for sculptural pieces (Tubes, Scirocco).
- **Aluminium** — light, **fast to heat/cool**, highly responsive and efficient — well-matched to modern low-temperature/heat-pump systems.
- **Brass/stainless** — premium finish options, corrosion resistance.

**Configurations.** Hydronic (plumbed into central heating), electric (heating element), or **dual-fuel**; vertical sculptural panels, towel ladders, mirror-radiators.
**Finishes.** Powder coat (any RAL), polished/brushed metal, textured — coordinated with tapware finishes.

> [!question] To verify
> Confirm electric vs hydronic vs dual-fuel availability and finish range; check whether any mirror-radiator hybrids are stocked.

---

## Wellness Materials
> [!example] Snapshot
> **Class:** Mixed (timber, acrylic, glass, steel) · **AKA:** Sauna, hammam/steam, spa, hot tub · **Afoi Deli category:** Wellness · **Research depth:** Light
> **Key brands here:** **Effegibi** (sauna + hammam/steam), **Jacuzzi** (spa/hot tubs), **Kos** (Zucchetti.Kos — wellness/baths), **Glass 1989** (steam/shower/wellness), **Fontealta** (outdoor showers/wellness).

**Materials by sub-type:**
- **Finnish sauna** — low-resin softwoods that stay cool and resist heat: **Nordic spruce, hemlock, aspen, alder, Western red cedar**; tempered-glass fronts; heater (electric/wood) with stones (often **olivine/diabase**).
- **Hammam / steam room** — water-/heat-proof linings: **porcelain/glass mosaic** (see [[Glass Mosaic]]), solid surface or microcement seating; steam generator; **toughened glass** enclosure.
- **Spa / hot tub** — moulded **acrylic** shells (sometimes on fibreglass) with insulated cabinets; jets, pumps, heaters; some all-stainless premium tubs.

**Applications.** Home and hospitality wellness rooms; the high-ticket, design-led end of the bathroom.

> [!question] To verify
> Map brand → sub-type (Effegibi sauna+hammam; Jacuzzi spa; Glass 1989 steam/shower). Confirm whether saunas are stocked or made-to-order.

---

## Shading System Materials
> [!example] Snapshot
> **Class:** Aluminium structure + technical fabric/louvres · **AKA:** Pergolas, awnings, sunshades, σκίαστρα · **Afoi Deli category:** Shading · **Research depth:** Light

**Materials & why.** Outdoor exposure → corrosion resistance and UV stability are everything:
- **Extruded/powder-coated aluminium** — frames, **bioclimatic louvre (adjustable-blade) pergolas**, awning arms; light, rustproof, any RAL finish.
- **Technical fabrics** — acrylic (solution-dyed, e.g. Sunbrella-class), PVC-coated polyester, PVC mesh (screens) — UV-, water- and mould-resistant, retractable.
- **Glass / polycarbonate** roofs on some systems; **steel** for large spans; motors + sensors (wind/rain/sun) for automation.

**Applications.** Terraces, façades, hospitality outdoor space — pairs with the outdoor 20 mm porcelain paver story.

> [!question] To verify
> Identify the actual shading **brand(s)** carried (not visible on the brand grid) and whether it's bioclimatic pergola, awnings, or both — then deepen this note.

---

# APPENDIX — Brand → Material index

Every brand on the [Afoi Deli brands page](https://afoideli.gr/brands/), grouped by the material it primarily supplies. **Confidence flags:** ✅ well-documented · ⚠️ verify.

> [!abstract]- Tiles — Porcelain stoneware & ceramic (click to expand)
> 41ZERO42 ✅ · ABK ✅ · Ariana ✅ · Atlas / Atlas Concorde ✅ · Cedit ✅ · Cerasarda ✅ (majolica/ceramic ⚠️) · Cercom ✅ · Cerdomus ✅ · Cesi ⚠️ (tiles + furniture?) · Cir ✅ · Cotto d'Este ✅ (+ Kerlite slab) · Del Conca ✅ · Dom ✅ · Edimax ✅ · Emil ✅ · Equipe ✅ (glazed ceramic) · Ergon ✅ · Ermesaurelia ✅ · Faetano ✅ · Ferres ⚠️ · Flaviker ✅ · Florim ✅ (+ slab) · Gambini ✅ · Imola ✅ · Iris ✅ · Italgraniti ✅ (+ slab) · Kronos ✅ · La Fabbrica ✅ (+ slab) · La Faenza ✅ · Lea ✅ (+ Slimtech slab) · Leonardo ✅ · Marazzi ✅ · Marca Corona ✅ · Mutina ✅ · Panaria ✅ · Pastorelli ✅ · Peronda ✅ · Piemme ✅ · Provenza ✅ (porcelain + wood-look) · Sant'Agostino ✅ · Serenissima ✅ · Settecento ✅ (decorative ceramic) · Wow ✅ (glazed ceramic) · Zebis ⚠️

> [!abstract]- Glass mosaic
> **Bisazza** ✅ (Venetian glass mosaic, smalti, gold-leaf, aventurine).

> [!abstract]- Sanitaryware — ceramic & solid surface
> Cielo ✅ (VC/FFC + **Ceramilux** solid surface) · Flaminia ✅ (ceramic) · Galassia ✅ (ceramic) · GSI ✅ (ceramic) · Scarabeo ✅ (ceramic) · Laufen ✅ (ceramic + **SaphirKeramik**) · **Antonio Lupi** ✅ (**Cristalplant / Flumood** solid surface, + furniture/mirrors) · Cerasarda ⚠️ (also sanitary pieces?) · **Geberit** ✅ — **flush/cistern & installation systems** (not a ceramic body).

> [!abstract]- Faucets / mixers
> Fantini ✅ (brass) · Fima Carlo Frattini ✅ (brass) · Zucchetti ✅ (brass) · Treemme/3MME ✅ (brass) · Nicolazzi ✅ (brass, classic) · Fontealta ⚠️ (wellness/outdoor showers) · **Quadro / QuadroDesign** ⚠️ (likely **stainless steel** tapware).

> [!abstract]- Bathroom furniture, mirrors & accessories
> Antonio Lupi ✅ (furniture + mirrors) · Inda ✅ (accessories + mirrors) · Novel ⚠️ (furniture) · Harmony ⚠️ (furniture/accessories) · Luminor ⚠️ (LED mirrors) · Cesi ⚠️.

> [!abstract]- Shower enclosures & glass
> Glass 1989 ✅ (tempered-glass enclosures + wellness/steam).

> [!abstract]- Wellness
> Effegibi ✅ (sauna + hammam/steam) · Jacuzzi ✅ (spa/hot tubs, acrylic) · Kos ✅ (Zucchetti.Kos — wellness/baths) · Glass 1989 ✅ (steam/shower) · Fontealta ⚠️.

> [!abstract]- Radiators / towel warmers
> Tubes ✅ (Tubes Radiatori — steel/aluminium designer) · Scirocco ✅ (Scirocco H — steel designer).

> [!abstract]- Parquet / wood
> Bassano Parquet ✅ · Original Parquet ✅ · (Provenza ✅ — wood-look **porcelain**, not timber).

> [!abstract]- Kitchens
> Scavolini ✅ (kitchen systems; worktop material specified separately — see [[Countertop Materials]]).

---

## Sources

Authoritative references used (paraphrased throughout; verify against live supplier sheets):

- **Standards bodies / EPDs:** ISO 13006:2018 (ceramic tiles — classification); EN 14411:2016; ISO 10545 series (test methods); ANSI A326.3 (DCOF); DIN 51130 & DIN 51097 (slip); EN 12150 / BS 6206 (safety glass); NSF/ANSI 61 & 372 (low-lead).
- **Porcelain manufacture/technology:** RAK Ceramics tile-technology; Crossville/Stone World on thin porcelain tile (TPT); Cotto d'Este (Kerlite); Laminam technical pages.
- **Mosaic:** Bisazza technical data sheets; Orsoni/Murano smalti references.
- **Sanitary ceramic:** Laufen (SaphirKeramik); pop-up-my-bathroom & Architect Magazine on VC/FFC/SaphirKeramik; Kaleseramik VC/FFC.
- **Solid surface:** DuPont Corian Declare/EPA composition; Cristalplant material pages; Archiproducts material taxonomy.
- **Brass & finishes:** Oras/Hansa durability notes; VaporTech & Starcraft on chrome vs PVD; DZR-brass patents.
- **Wood flooring:** Round Wood, Reclaimed Flooring Co., PerfektoWood (engineered vs solid; finishes; grading).
- **Tempered glass:** Merlyn / Elegant Showers (thickness & easy-clean coatings); glass-fabricator process notes.
- **Countertops:** Angi, Natural Stone City, Funtek (quartz vs sintered vs natural stone).

> [!todo] Next actions
> 1. Walk this file against current stock; resolve every `To verify` and the ⚠️ flags in the appendix.
> 2. On approval, **split into individual notes** (each `## Material` → its own note) and add typed frontmatter (`class`, `category`, `group`, `water_absorption`, `key_brands`, `research_depth`) so a **Base** can query the vault.
> 3. Decide whether brand notes ([[Mutina]], [[Laufen]] …) become their own layer linking back to materials.
