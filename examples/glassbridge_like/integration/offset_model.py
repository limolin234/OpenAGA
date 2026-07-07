#!/usr/bin/env python3
"""Tiny offset-to-loss example."""

from __future__ import annotations

import math


def lateral_loss_db(d_um: float, w_um: float) -> float:
    return 4.343 * (d_um / w_um) ** 2


for d in [0.1, 0.2, 0.5, 1.0]:
    print(f"d={d:.1f} um, w=1.75 um -> {lateral_loss_db(d, 1.75):.3f} dB")
