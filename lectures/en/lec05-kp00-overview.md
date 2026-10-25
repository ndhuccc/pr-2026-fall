# Chapter 4 Route Map: After One Line Is Not Enough

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4 overview (KP01–KP05)

[Slides: read and download](../../slides/lec05-kp00-overview-en.jbd.json) | [中文版](../lec05-kp00-overview.md)

## Learning objectives

- Connect KP01 to KP05 with one question and state the question, the answer and what is left open for each.
- Say in which knowledge point each term of the chapter appears.
- State the conclusion and limits of the chapter and what the next chapter learns.

## Chapter 4 Route Map

**One-sentence summary**: When labels alternate (as in XOR) one line fails; adding lines and layers separates them, KP05 says how a network grows from points, and the open question is how to learn the weights.

### 1. This chapter asks one thing

How can a network separate labels that one line cannot? The starting point is XOR: A on one diagonal, B on the other.

![XOR and the same line](../../assets/figures/lec05-kp01-xor-check.png)

### 2. Route map: each knowledge point takes over the question left by the previous one

![Route map of the chapter](../../assets/figures/lec05-kp00-map.png)

Figure `lec05-kp00-map`: top to bottom are KP01 to KP05.

### 3. Question, answer and what is left open for the five knowledge points

| Knowledge point | Question | Answer | Left open |
|---|---|---|---|
| KP01 one line fails | Does any line separate XOR? | The two A scores sum above 0 and the two B scores at most 0, yet it is the same expression, a contradiction. | What must change is the combination of boundaries, e.g. a strip between two lines. |
| KP02 encode then classify | How are the two decisions built as a network? | Two lines give one bit each, the four points get three codes, one output line separates A from B. | With more lines, is the output layer still enough? |
| KP03 codes and limit | With more lines, can one cut separate every labelling? | Some yes, some no (A and B alternate on the bottom face). | Labellings one cut misses need another layer. |
| KP04 detect each code | How do we add a layer on top of the codes? | Detector score $=0.5-$ (wrong bits), output layer merges with an OR. | Only proves it is enough; how does the network grow from points? |
| KP05 grow from points | With only labelled points, how does the network grow? | A master unit splits once, ancillary units handle mixed groups and add bits to purify. | All correct only means these points; fix the architecture and learn weights. |

![The strip of KP01](../../assets/figures/lec05-kp01-strip.png)

![The strip of KP02](../../assets/figures/lec05-kp02-strip-net.png)

![The cube and cut of KP03](../../assets/figures/lec05-kp03-cube-cut.png)

![The A region of KP04](../../assets/figures/lec05-kp04-plane-final.png)

![The new plane of codes of KP05](../../assets/figures/lec05-kp05-code-plane.png)

### 4. Recap: the whole network and four reminders

![The four stages of the network](../../assets/figures/lec05-kp04-stages.png)

**Common misconception**: that a construction showing a network is enough means the weights are learned or the network is minimal. A construction only proves it is enough.

**Four reminders**: one cut on fixed codes has a limit; contradictory labels cannot be all correct; all correct only means these points; a construction proves it is enough, not that the weights are learned or the network is minimal. Next chapter: fix the architecture first, then learn the weights with a cost function (backpropagation).

## Terms and sources

| English | Knowledge point |
|---|---|
| Bit, step rule, hidden layer, hidden code | KP02 |
| Code, realized code, unrealized code, linearly separable | KP03 |
| Target code, detector, OR merge, three-layer network | KP04 |
| Master unit, ancillary unit, mixed group, purification | KP05 |

Source: the slides and lectures of KP01–KP05 of this chapter (compiled 2026-10-25). This page only recaps and adds no new content.
