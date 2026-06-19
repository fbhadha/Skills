---
name: company-explainer
description: Produce a sourced, plain-language explainer of how a company makes money and what its strategy is, as an HTML page and a PDF in my field-guide design system, readable by customers, shareholders, and employees at the same time. Trigger when I want to understand or explain a company's strategy, business model, or financials, with phrases like "explain how [company] makes money," "break down [company]'s strategy," "help me understand what [company] is doing," "make a field guide on [company]," or when I paste a company's filings or investor materials and want them made readable. Trigger even when I do not name the skill, as long as I am trying to get a clear, sourced picture of a company.
license: MIT
---

# company-explainer
TASK: Produce a sourced plain-language HTML and PDF explainer of how a named company makes money and what its strategy is, in the field-guide design system, readable by customers, shareholders, and employees.

## INPUT
request: the company to explain and any angle the user names
company: the company name
known_sources: primary source URLs the user already has, or empty

## DIMENSIONS
audience: neutral-all-readers | single-audience
depth: thorough | overview

## OUTPUT
An HTML file built from assets/field-guide-template.html, plus a PDF rendered from it. Sections in order: a header with kicker, title, and a two-sentence takeaway box; a numbered promise band stating the company's headline commitments; a money-machine step table tracing revenue, operating profit, building spend, free cash flow, and where the cash goes; a two-bets block splitting the strategy; a who-is-affected strip after each major decision with one cell per affected group; a section on the forces driving the strategy; a cascade section showing how the top number reaches daily work; a plain-words glossary; a tiered sources block with primary above secondary; a footer. Every figure carries a numbered citation linking to a primary document.

## STEPS
1. Present the DIMENSIONS choices to the user. IF references/provenance.md is readable THEN show the call made last time and one supporting quote for each dimension. Ask the user to keep that path or change it.
2. Set audience and depth from the user's answer.
3. IF deep research mode is off THEN recommend the user turn it on and wait for confirmation before continuing.
4. Research the company until the core mechanism of how it makes money is plain. State that mechanism in one sentence and confirm it with the user before drafting.
5. Set one throughline: the single idea every section supports.
6. List every factual claim the explainer will make and attach a candidate source to each.
7. Open each candidate link and confirm it loads. Replace any dead link with a working source for the same fact.
8. Download each primary document and read it end to end. Correct any figure the document contradicts.
9. Cross-check each founding date, ownership fact, and other objective claim against the broader public record. Use the version the public record supports when a primary document's wording differs.
10. Replace each secondary citation with a primary one wherever a primary source states the fact. Mark every remaining secondary source as secondary.
11. Draft the explainer in assets/field-guide-template.html. Place one visual per structural idea and write the narrative above each visual.
12. Add one concrete proof-point to each business unit and each major claim: a named product, a deal, or a figure from the sources.
13. Define every specialist term in plain words at its first use and add it to the glossary.
14. Add the who-is-affected strip after each major decision, with one cell per group the company affects.
15. Order the sections so the core mechanism comes before the forces behind the strategy.
16. Open the explainer with a takeaway box of two sentences.
17. Render the HTML to PDF.
18. Run CHECK before presenting.

## RULES
- Write at a grade 10 reading level.
- Write in the user's English variant (ask if unknown, default to US English).
- Replace every em or en dash with a comma, a colon, or parentheses.
- Define every specialist term in plain words at first use and in the glossary.
- Trace every factual claim to a primary document read end to end.
- Cross-check each objective historical fact against the public record and use the supported version.
- Cite a secondary source only where no primary source states the fact, and mark it secondary.
- Confirm every link loads before presenting.
- Give each business unit and each major claim one concrete proof-point.
- Open the explainer with a two-sentence takeaway box.
- Write the explainer so a customer, a shareholder, and an employee each read it the same way.
- State the hard parts of the strategy in plain words.
- Build the explainer from assets/field-guide-template.html.
- Recommend deep research mode at the start when it is off.

## EXAMPLES
INPUT:
company: a national telecom carrier, angle: how it plans to grow while its old products shrink
OUTPUT:
<an HTML field-guide explainer rendered to PDF. The takeaway box names the two headline targets. A money-machine step table shows revenue barely growing, operating profit held flat by cost cuts, building spend falling, free cash flow rising, and cash going to dividends and debt. A two-bets block splits selling new services from cutting internal costs, and each new unit carries one concrete proof-point such as a named product or a signed deal. A who-is-affected strip after the cost-cut section shows one cell each for customers, shareholders, and employees. Every figure links to a primary filing. The glossary defines each term. The sources block lists primary above secondary.>

## CHECK
- [ ] every specialist term is defined at first use and in the glossary
- [ ] every figure cites a primary document read end to end
- [ ] each objective historical fact is cross-checked against the public record
- [ ] each business unit and major claim carries one concrete proof-point
- [ ] every secondary source is marked, and none is used where a primary source exists
- [ ] every link loads
- [ ] one throughline holds across the whole piece
- [ ] a customer, a shareholder, and an employee each read it the same way
- [ ] the piece opens with a two-sentence takeaway box
- [ ] the user's English variant with no em or en dashes
- [ ] the output is built from the field-guide template structure
