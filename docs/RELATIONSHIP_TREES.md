# Afoi Deli — Relationship Trees

**Generated 2026-07-02** by the `/repo-analysis` skill — regenerated at every session end (`CLAUDE.md` §8, ADR-0006). **Do not hand-edit.**

Four trees: the supply ecosystem, the people around the operation, the data-contract family, and the memory spine. Quantitative link-graph numbers (hub degrees, edge counts) live in `docs/REPO_ANALYSIS.md` §2/§7 — one source of truth per number. The human family itself is drawn in `docs/FAMILY_TREE.md`.

## 1. The supply ecosystem — house → conduits → brands → collections

Sources: `04_SUPPLIERS_AND_BRANDS/Supplier Master Index.md`, the conduit notes, the Kronos subtree.

```mermaid
graph TD
    ad["Afoi Deli Floor + Bath"]
    ad ==> pi["Plus Interiors — Kostas Tzanidis, son George — the founding conduit"]
    ad ==> fi["Filon IKE — Alexandros Simos — professional, punctual"]
    ad ==> dealer["Dealer network — direct brand channel"]
    ad --> stubs["8 seed houses — Atlas Concorde · Florim · Emilgroup · Sant'Agostino · ABK · 41zero42 · Antonio Lupi · Fima Carlo Frattini"]

    pi --> kron["Kronos — tiles · depth target dossier"]
    pi --> cielo["Cielo — sanitaryware · the founding-act brand"]
    pi --> fant["Fantini — faucets · Greek channel needs confirmation"]
    fi --> mut["Mutina — designer ceramics + subbrands"]
    dealer --> scav["Scavolini — kitchens · the expansion keystone"]

    kron --> pv["Collection - Kronos Pierre Vive — first born-on-ingestion note"]
    kron --> kcr["Kronos Collections Reference — the ingest roster"]
    pv -.-> sku["Future SKU tier — OS products table, zero rows today"]
```

*Legend: thick `==>` = live commercial channel · solid `-->` = documented relationship · dashed `-.->` = future/specified. The power-geometry doctrine on every conduit edge: the conduit is replaceable, the brand is not, and the client always turns to Afoi Deli (`04_SUPPLIERS_AND_BRANDS/Conduit - Plus Interiors.md`).*

## 2. The people around the operation

Sources: `01_COMPANY_CORE/People and Roles Map.md`, `01_COMPANY_CORE/Afoi Deli — Operating Doctrine.md`, tracer ground truth (`02_OPERATIONS_OS/Order Lifecycle — Ground-Truth Capture.md`).

```mermaid
graph LR
    subgraph house["The house"]
        kostas2["Kostas — founder · strategy · supplier relationships"]
        chrys2["Chrysoula — the closer"]
        orf["Orfeas — successor · steward · this vault's owner"]
        ekt["Ektoras — role held open"]
    end
    subgraph desk["The operation"]
        odesk["Orders desk — Dimitris and Vicky, orders at afoideli.gr"]
        roles["Role rows — sales · operations · warehouse · logistics · finance · management"]
    end
    subgraph outside["External relationships"]
        tzan["Plus Interiors — Tzanidis father and son"]
        simos["Filon IKE — Alexandros Simos"]
        elxis2["ELXIS — freight forwarder + Italian correspondent"]
        mega["MEGASOFT — external accounting system of record"]
        archs["Architects and designers — the rebate channel"]
    end
    orf --> odesk
    kostas2 --> tzan
    orf --> roles
    odesk --> tzan
    odesk --> simos
    roles --> elxis2
    roles --> mega
    chrys2 -.-> archs
    orf -.-> archs
```

*Legend: solid `-->` = documented working relationship · dashed `-.->` = inferred relationship channel. Per-step ownership of the six critical order gates is deliberately unresolved in `01_COMPANY_CORE/People and Roles Map.md` — an open question the tracer is closing.*

## 3. The data-contract family — one master, ten entities, eleven CSVs

Source: `03_DATABASE_DESIGN/Database Master Schema.md` (the md↔csv precedence rule: CSV header is the stored contract, the note annotates).

```mermaid
graph TD
    master["Database Master Schema — ERD + parity table"]
    master --> commerce["Commerce — orders · order_lines · clients · projects"]
    master --> supplyd["Supply — suppliers · products · supplier_loadings"]
    master --> moneyd["Money — supplier_invoices AP · client_invoices AR"]
    master --> opsd["Ops — tasks_alerts · issues_exceptions"]
    commerce -.-> gap1["Pending from ground truth — MEGASOFT mirror · rebates table"]
    master -.-> gap2["ERD names PEOPLE and PAYMENTS — no contract yet, known P2 gap"]
```

*Legend: solid `-->` = entity pairs in sync (md note + CSV header) · dashed `-.->` = acknowledged gaps. All 11 CSVs are header-only — the data layer is a specification awaiting its first real rows.*

## 4. The memory spine — how the repo remembers

```mermaid
graph TD
    heart2["The Heart"] ==> claude2["CLAUDE.md — boot order + rituals"]
    claude2 ==> vsm2["Vault State Memory — single source of where-we-are"]
    vsm2 --> sessions["Session logs ×18 — one per working session"]
    vsm2 --> adrs["ADRs ×6 — dated decisions"]
    vsm2 --> brains["Brainstorm trail — strategic reframings"]
    vsm2 --> backlog["Capture Backlog — the ranked next-work queue"]
    audits2["_meta audits — charter · STATE ledger · dated reports"] -.-> vsm2
    vsm2 --> docsuite["docs suite — this analysis, regenerated each session"]
    docsuite -.-> guard2["git-sync guard — a stale push does not leave the machine"]
```

*Legend: thick `==>` = the literal boot chain · solid `-->` = maintained-at-session-end artifacts · dashed `-.->` = enforcement/reconciliation feedback. The loop closes at the guard: every push carries the state that describes it.*
