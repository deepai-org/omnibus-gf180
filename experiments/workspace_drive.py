"""Audit clipping of specialist influences in the actual cross-stream task.

Instrumentation is read-only: record the arguments delivered to ContentWorkspace
and independently reconstruct its pre-clipping drive. No oracle enters Agent.
"""
import json
from unittest.mock import patch
import numpy as np
from model.content_workspace import ContentWorkspace
from experiments.cross_stream import run_case


def audit(lesion=None):
    rows = []
    original = ContentWorkspace.step

    def record(w, evidence, groups, qualities, available, feedback=(0, 0), recurrence=True):
        evidence, available, feedback = map(np.asarray, (evidence, available, feedback))
        self_drive = w.self_gain*w.activity if recurrence else np.zeros(2)
        raw = 2*(evidence*available + w.return_gain*feedback + self_drive
                 -1.2*w.activity[::-1]-.9*w.adaptation-.45)
        rows.append(dict(activity=w.activity.copy(), raw=raw.copy(),
                         feedback=feedback.copy(), available=available.copy()))
        original(w, evidence, groups, qualities, available, feedback, recurrence)

    with patch.object(ContentWorkspace, 'step', record):
        result = run_case('horizontal', 'horizontal', 1, lesion)
    # Only the object phase: candidate zero has physical evidence available.
    selected = [r for r in rows if r['available'][0] > 0]
    active = [r for r in selected if r['activity'][0] > .7]
    return dict(lesion=lesion, correct=result['correct'], elapsed=result['elapsed'],
                object_steps=len(selected), active_steps=len(active),
                upper_clipped_active_steps=sum(bool(r['raw'][0] >= 1) for r in active),
                raw_drive_active_range=[float(min(r['raw'][0] for r in active)),
                                        float(max(r['raw'][0] for r in active))] if active else None,
                feedback_active_range=[float(min(r['feedback'][0] for r in active)),
                                       float(max(r['feedback'][0] for r in active))] if active else None)


if __name__ == '__main__':
    print(json.dumps([audit(lesion) for lesion in
                      (None, 'sensory_return', 'observer_return', 'memory_return')], indent=2))
