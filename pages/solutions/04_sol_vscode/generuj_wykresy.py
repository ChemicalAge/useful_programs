"""Generate projectile-motion plots for raport.md using only Python's standard library."""

from html import escape
from math import cos, hypot, radians, sin
from pathlib import Path

OUT = Path(__file__).parent / "files" / "rzut_ukosny"
OUT.mkdir(parents=True, exist_ok=True)

G = 9.81
V0 = 24.0
ALPHA_DEG = 37.0
MASS = 0.145
RHO = 1.225
CD = 0.47
AREA = 0.0042
DT = 0.002
DRAG_C = RHO * CD * AREA / (2 * MASS)
ANGLE = radians(ALPHA_DEG)
INITIAL = [0.0, 0.0, V0 * cos(ANGLE), V0 * sin(ANGLE)]


def derivative(state):
    _, _, vx, vy = state
    speed = hypot(vx, vy)
    return [vx, vy, -DRAG_C * speed * vx, -G - DRAG_C * speed * vy]


def add_scaled(state, slope, scale):
    return [value + scale * change for value, change in zip(state, slope)]


def simulate():
    time = 0.0
    state = INITIAL[:]
    samples = [(time, state[:])]
    while time < 20.0:
        k1 = derivative(state)
        k2 = derivative(add_scaled(state, k1, DT / 2))
        k3 = derivative(add_scaled(state, k2, DT / 2))
        k4 = derivative(add_scaled(state, k3, DT))
        next_state = [
            value + DT * (a + 2 * b + 2 * c + d) / 6
            for value, a, b, c, d in zip(state, k1, k2, k3, k4)
        ]
        next_time = time + DT
        if next_state[1] < 0:
            fraction = state[1] / (state[1] - next_state[1])
            landing = [
                value + fraction * (following - value)
                for value, following in zip(state, next_state)
            ]
            samples.append((time + fraction * DT, landing))
            return samples
        samples.append((next_time, next_state))
        time, state = next_time, next_state
    raise RuntimeError("The projectile did not return to ground within 20 s.")


def ideal_state(time):
    return [
        V0 * cos(ANGLE) * time,
        V0 * sin(ANGLE) * time - 0.5 * G * time**2,
        V0 * cos(ANGLE),
        V0 * sin(ANGLE) - G * time,
    ]


def render_chart(filename, title, x_label, y_label, series, x_limits, y_limits):
    has_wide_legend = len(series) > 3
    width, height = (1100 if has_wide_legend else 900), 500
    left, right, top, bottom = 90, (260 if has_wide_legend else 30), 65, 85
    plot_width, plot_height = width - left - right, height - top - bottom
    x_min, x_max = x_limits
    y_min, y_max = y_limits

    def point(x, y):
        px = left + (x - x_min) / (x_max - x_min) * plot_width
        py = top + (y_max - y) / (y_max - y_min) * plot_height
        return px, py

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">',
        "<rect width='100%' height='100%' fill='white'/>",
        "<style>text{font-family:Arial,sans-serif;fill:#233044}"
        ".grid{stroke:#dbe2ea;stroke-width:1}"
        ".axis{stroke:#526174;stroke-width:1.5}</style>",
        f"<text x='{left}' y='35' font-size='22' font-weight='bold'>"
        f"{escape(title)}</text>",
    ]
    for index in range(6):
        x_value = x_min + (x_max - x_min) * index / 5
        px, _ = point(x_value, y_min)
        parts.append(
            f"<line class='grid' x1='{px:.1f}' y1='{top}' "
            f"x2='{px:.1f}' y2='{top + plot_height}'/>"
        )
        parts.append(
            f"<text x='{px:.1f}' y='{top + plot_height + 24}' "
            f"font-size='13' text-anchor='middle'>{x_value:.1f}</text>"
        )
        y_value = y_min + (y_max - y_min) * index / 5
        _, py = point(x_min, y_value)
        parts.append(
            f"<line class='grid' x1='{left}' y1='{py:.1f}' "
            f"x2='{left + plot_width}' y2='{py:.1f}'/>"
        )
        parts.append(
            f"<text x='{left - 12}' y='{py + 4:.1f}' "
            f"font-size='13' text-anchor='end'>{y_value:.1f}</text>"
        )

    parts.extend(
        [
            f"<line class='axis' x1='{left}' y1='{top + plot_height}' "
            f"x2='{left + plot_width}' y2='{top + plot_height}'/>",
            f"<line class='axis' x1='{left}' y1='{top}' "
            f"x2='{left}' y2='{top + plot_height}'/>",
            f"<text x='{left + plot_width / 2}' y='{height - 20}' "
            f"font-size='16' text-anchor='middle'>{escape(x_label)}</text>",
            f"<text x='22' y='{top + plot_height / 2}' font-size='16' "
            f"text-anchor='middle' transform='rotate(-90 22 "
            f"{top + plot_height / 2})'>{escape(y_label)}</text>",
        ]
    )
    for index, (label, values, color) in enumerate(series):
        if any(
            x < x_min - 1e-9 or x > x_max + 1e-9
            or y < y_min - 1e-9 or y > y_max + 1e-9
            for x, y in values
        ):
            raise ValueError(f"Data for {label!r} fall outside the chart axes.")
        coordinates = " ".join(
            f"{point(x, y)[0]:.1f},{point(x, y)[1]:.1f}" for x, y in values
        )
        parts.append(
            f"<polyline points='{coordinates}' fill='none' "
            f"stroke='{color}' stroke-width='3'/>"
        )
        legend_x = left + plot_width + 20 if has_wide_legend else left + 15
        legend_y = top + 18 + index * 23
        parts.extend(
            [
                f"<line x1='{legend_x}' y1='{legend_y}' "
                f"x2='{legend_x + 25}' y2='{legend_y}' stroke='{color}' "
                "stroke-width='3'/>",
                f"<text x='{legend_x + 32}' y='{legend_y + 5}' "
                f"font-size='13'>{escape(label)}</text>",
            ]
        )
    parts.append("</svg>")
    (OUT / filename).write_text("\n".join(parts), encoding="utf-8")


def main():
    drag = simulate()
    flight_time = drag[-1][0]
    ideal_flight_time = 2 * V0 * sin(ANGLE) / G
    ideal_range = V0 * cos(ANGLE) * ideal_flight_time
    ideal_height = (V0 * sin(ANGLE)) ** 2 / (2 * G)
    drag_apex_time, drag_apex = max(drag, key=lambda sample: sample[1][1])
    drag_range = drag[-1][1][0]
    if abs(drag[-1][1][1]) > 1e-10:
        raise RuntimeError("The interpolated landing point is not on y = 0.")

    ideal_times = [
        ideal_flight_time * i / (len(drag) - 1) for i in range(len(drag))
    ]
    ideal = [(t, ideal_state(t)) for t in ideal_times]
    render_chart(
        "tor_rzutu.svg",
        "Tor rzutu: porównanie modeli",
        "x [m]",
        "y [m]",
        [
            ("Bez oporu", [(s[0], s[1][1]) for s in ideal], "#2463a6"),
            ("Opór kwadratowy", [(s[1][0], s[1][1]) for s in drag], "#d47722"),
        ],
        (0, max(ideal_range, drag_range) * 1.05),
        (0, ideal_height * 1.12),
    )
    render_chart(
        "polozenie_czas.svg",
        "Wysokość w czasie",
        "t [s]",
        "wysokość y [m]",
        [
            ("y bez oporu", [(t, s[1]) for t, s in ideal], "#168578"),
            ("y z oporem", [(t, s[1]) for t, s in drag], "#8455a4"),
        ],
        (0, ideal_flight_time),
        (0, ideal_height * 1.12),
    )
    velocity_series = [
        ("vx bez oporu", [(t, s[2]) for t, s in ideal], "#2463a6"),
        ("vy bez oporu", [(t, s[3]) for t, s in ideal], "#168578"),
        ("vx z oporem", [(t, s[2]) for t, s in drag], "#d47722"),
        ("vy z oporem", [(t, s[3]) for t, s in drag], "#8455a4"),
    ]
    max_speed_component = max(
        abs(value) for _, values, _ in velocity_series for _, value in values
    )
    render_chart(
        "predkosc_czas.svg",
        "Składowe prędkości w czasie",
        "t [s]",
        "prędkość [m/s]",
        velocity_series,
        (0, ideal_flight_time),
        (-1.05 * max_speed_component, 1.05 * max_speed_component),
    )
    drag_energy = [
        (t, 0.5 * MASS * (s[2] ** 2 + s[3] ** 2) + MASS * G * s[1])
        for t, s in drag
    ]
    if any(
        following[1] > previous[1] + 1e-10
        for previous, following in zip(drag_energy, drag_energy[1:])
    ):
        raise RuntimeError("Mechanical energy increased in the drag model.")
    ideal_energy = [
        (t, 0.5 * MASS * (s[2] ** 2 + s[3] ** 2) + MASS * G * s[1])
        for t, s in ideal
    ]
    render_chart(
        "energia_czas.svg",
        "Energia mechaniczna w czasie",
        "t [s]",
        "energia [J]",
        [
            ("Bez oporu", ideal_energy, "#2463a6"),
            ("Opór kwadratowy", drag_energy, "#d47722"),
        ],
        (0, ideal_flight_time),
        (0, max(value for _, value in ideal_energy) * 1.08),
    )

    print(f"v0 = {V0:.2f} m/s; alpha = {ALPHA_DEG:.2f} deg")
    print(f"Bez oporu: T = {ideal_flight_time:.4f} s, "
          f"H = {ideal_height:.4f} m, R = {ideal_range:.4f} m")
    print(f"Z oporem: T = {flight_time:.4f} s, "
          f"H = {drag_apex[1]:.4f} m, R = {drag_range:.4f} m, "
          f"x_apex = {drag_apex[0]:.4f} m, "
          f"t_apex = {drag_apex_time:.4f} s")
    print(f"Wykresy zapisano w: {OUT}")


if __name__ == "__main__":
    main()
