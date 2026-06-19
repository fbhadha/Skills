<voice_profile>
<!--
  TEMPLATE — fill this in during onboarding (see references/onboarding.md).
  This file holds the quantitative fingerprint of YOUR writing. Until it is
  filled, the my-voice skill has no profile to match and will fall back to the
  generic humanizer engine only. Replace every <bracketed> slot with a real
  value drawn from your own corpus, then delete this comment block.
-->

corpus: <number of pieces analyzed, e.g. 200; mix of platforms/contexts>
generated: <YYYY-MM-DD>
analysis_notes: <tools or method used, or "estimated by hand from N samples">

<constraints>
<!-- Run your corpus through a readability tool (textstat, etc.) or estimate from samples. -->
reading_level: <Flesch-Kincaid grade ceiling for your writing>
sentence_length_avg: <average words per sentence>
sentence_length_median: <median words per sentence>
short_sentences_pct: <% under 10 words>
mid_sentences_pct: <% between 10-25 words>
long_sentences_pct: <% over 25 words>
paragraph_length: <average sentences per paragraph>
declarative_pct: <%>
interrogative_pct: <%>
imperative_pct: <%>
exclamatory_pct: <%>
</constraints>

<lexical_sophistication>
<!-- How plain or specialized is the vocabulary? -->
pct_monosyllabic: <% of one-syllable words — high means plain and punchy>
pct_rare_words: <% obscure vocabulary — low means everyday language>
avg_word_length: <characters>
register_summary: <one or two sentences: where does complexity come from — argument and rhythm, or vocabulary? Any domain-specific terms?>
</lexical_sophistication>

<confidence_calibration>
<!-- Do you assert or hedge? -->
confidence_ratio: <boosters-to-hedges, e.g. 2:1 means positions taken twice as often as hedged>
dominant_modal: <which modal verb dominates: would / can / will / should — reveals how you reason>
modal_summary: <one sentence on what the modal pattern says about how you think>
</confidence_calibration>

<discourse_markers>
<!-- How are arguments stitched together? -->
dominant_connectors: <the conjunctions/markers you lean on, e.g. "but" and "so" for contrastive + causal>
informal_markers: <casual markers if any: lol, lmao, whatever, etc. — or "none / formal register">
signature_reformulators: <e.g. "point being", "long story short", "basically" — or "none">
marker_summary: <one sentence>
</discourse_markers>

<pronoun_ecology>
<!-- Who does the writing center? -->
first_person_level: <high / moderate / low — do you write from "I"?>
i_to_you_ratio: <do you address the reader directly, or stay self-focused?>
they_vs_he_pattern: <do you think in systems/groups ("they/their") or individuals ("he/she")?>
pronoun_summary: <one sentence>
</pronoun_ecology>

<emphasis_fingerprint>
<!-- Your visible signature moves. Count per ~2000 words, or mark present/absent. -->
caps_emphasis: <frequency — is ALL CAPS your emphasis tool? present/absent/rate>
scare_quotes: <frequency — do you quote borrowed framing skeptically?>
parentheticals: <frequency — real-time asides>
ellipses: <frequency — thinking-aloud pauses>
em_dashes: <frequency — typically near-zero for a natural voice; record yours>
exclamations: <frequency, and any platform where they go to zero>
questions: <frequency — mostly rhetorical or real?>
profanity: <frequency and when it appears — emotional peaks or decoration?>
emoji: <rare / never / frequent>
</emphasis_fingerprint>

<platform_comparison>
<!--
  Fill one block per platform/context you write for (e.g. long-form, casual,
  professional). Voice shifts by audience; capture at least 2-3 contexts.
  Delete the example labels and use your own.
-->
<context_name_1>:
  reading_level: <grade>
  avg_sentence_length: <words>
  word_count_typical: <range and mean>
  questions: <frequency>
  exclamations: <frequency>
  confidence_ratio: <boosters-to-hedges>
  register: <one or two sentences on the distinct voice for this context>

<context_name_2>:
  reading_level: <grade>
  avg_sentence_length: <words>
  word_count_typical: <range and mean>
  questions: <frequency>
  exclamations: <frequency>
  confidence_ratio: <boosters-to-hedges>
  register: <one or two sentences>
</platform_comparison>

<vocabulary>
<!-- Words and phrases that are distinctly yours. -->
high_frequency_words: <the content words you reach for most>
characteristic_phrases:
  - <a phrase you use to introduce a hard truth>
  - <a phrase you use to close and walk away>
  - <an identity or stance anchor>
  - <add your own; these are fingerprints>
preserve_habits:
  - <e.g. a non-standard spelling or contraction you use on purpose>
  - <e.g. a filler word that signals "you know the rest">
never_introduce:
  - <words or registers that are NOT you — academic hedging, marketing-speak, etc.>
</vocabulary>

<structural_habits>
<!-- How pieces open, move, and close. -->
openings: <how do you tend to start? a person, a claim, a question, a topic noun?>
closings: <how do you tend to end? on an image, a dismissal, the person, a position?>
transitions: <explicit connectors, or just start the next point?>
signature_mid_moves: <e.g. personal disclosure escalating to a structural point; concession-then-attack; register drop for dismissal>
</structural_habits>

<confirmed_absent_patterns>
<!-- Patterns that are NOT in your writing. Keep them absent in output. -->
- <e.g. exclamation marks in professional contexts>
- <e.g. sycophantic openers>
- <e.g. engagement bait>
- <add the AI-tells and tics that would read as "not you">
</confirmed_absent_patterns>

<long_form_register>
<!--
  If you write long-form (essays, articles, reports) as well as short-form,
  capture the long-form numbers separately here, since they usually differ
  (denser, longer sentences, more structure). Otherwise delete this block.
-->
reading_level: <grade>
sentence_length_avg: <words>
structural_habits_long_form:
  - <e.g. carries section headers and the occasional list>
  - <e.g. builds a sustained argument across paragraphs>
  - <e.g. leans on a single extended analogy and carries it through>
  - <e.g. signature arc: open on a scene, escalate to the structural, close on a plain image>
caution:
  - <any older habits to NOT emulate — e.g. upbeat AI-tell closings>
</long_form_register>
</voice_profile>
