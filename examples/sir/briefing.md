# Briefing: what the reproduction number means for policy

*A one-page summary written in Markdown, the way an analyst might brief a decision-maker. The numbers come from
the [SIR report](report.htex); every claim links to the equation behind it.*

## Key points

1. **One number decides whether an outbreak grows.** If each case infects more than one other person on average
   ($R_0 > 1$), cases grow; below one they shrink ([threshold theorem](report.htex#thm:threshold)).
2. **Interventions work by lowering the effective reproduction number**, $R_t = R_0 \times S \times (1 - c)$,
   where $c$ is the fraction of contacts prevented.
3. **Vaccination has a clear target.** Immunising a fraction $p_c = 1 - 1/R_0$ of the population stops
   sustained spread ([equation](report.htex#eq:pc)).

## Targets at a glance

| If $R_0$ is | Vaccinate at least | Unchecked, the peak reaches | and in total infects |
|---:|---:|---:|---:|
| 1.5 | 33% | 6% | 58% |
| 2.5 | 60% | 23% | 89% |
| 4.0 | 75% | 40% | 98% |

> Even a modest $R_0$ eventually reaches most of an unprotected population. Flattening the peak buys time for
> the health system; only immunity or sustained contact reduction changes the final size.

## Caveats

- The model assumes everyone mixes equally. Real contact networks, age structure and waning immunity change the
  numbers, though not the logic[^ext].
- $R_0$ itself is estimated from early growth and carries wide uncertainty; plan for a range, not a point.

## Further reading

- Full derivation and interactive figures: [the SIR report](report.htex)
- How damping plays the same role in a mechanical system: [oscillator example](../oscillator/report.htex)

[^ext]: Hethcote's review (SIAM Review, 2000) surveys these extensions; see the report's references.
