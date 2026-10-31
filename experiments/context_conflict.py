"""One fixed uploaded contextual prior: ambiguous and contradictory evidence.

All clear controls are fully exposed. Hidden clear scenes are not scored as if
a predictive context were a guaranteed ground-truth object label.
"""
import json
from itertools import product
from experiments.context_ambiguity import run_case


def evaluate():
    rows = []
    for context, sign in product(('horizontal','vertical'),(-1,1)):
        rows.append(run_case(context,sign))
        for clear in ('horizontal','vertical','one_object'):
            rows.append(run_case(context,sign,exposed=True,clear_group=clear))
    return dict(total=len(rows),correct=sum(r['correct'] for r in rows),
                failures=[r for r in rows if not r['correct']],rows=rows)


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
