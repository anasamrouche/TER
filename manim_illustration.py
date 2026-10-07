from manim import *

config.background_color = ManimColor([8 / 256, 16 / 256, 33 / 256, 1.0])


def article_kernel(x: float, y: float, alpha: float) -> float:
    norm_squared: float = x**2 + y**2
    norm: float = np.sqrt(norm_squared) if norm_squared >= 1e-8 else 1e-8
    return 1 / norm**alpha - 0.3


class IntegrabilityL2(ThreeDScene):
    def construct(self):
        axes_left = (
            ThreeDAxes(
                x_range=[-2, 2],
                y_range=[-2, 2],
                x_length=config.frame_height / 1.5,
                y_length=config.frame_height / 1.5,
                tips=False,
            )
            .set_color(GOLD_B)
            .rotate(PI / 2, LEFT)
            .rotate(PI / 5, UP)
        )
        axes_right = axes_left.copy().shift(3.7 * RIGHT)
        axes_left.shift(3.7 * LEFT)

        kernel_left = (
            axes_left.plot_surface(
                function=lambda x, y: article_kernel(x, y, 1.1),
                u_range=axes_left.x_range[:2],
                v_range=axes_left.y_range[:2],
                resolution=256,
            )
            .set_color(RED)
            .set_opacity(0.3)
        )

        left_label = (
            Tex(r"$\alpha=1.1$\\Not $L^2$ integrable on $\mathbb{R}^2$")
            .set_color(RED)
            .scale(0.9)
            .move_to(4 * DOWN + 4 * LEFT)
        )

        kernel_right = (
            axes_right.plot_surface(
                function=lambda x, y: article_kernel(x, y, 0.5) - 0.2,
                u_range=axes_left.x_range[:2],
                v_range=axes_left.y_range[:2],
                resolution=256,
            )
            .set_color(BLUE)
            .set_opacity(0.3)
        )

        right_label = (
            Tex(r"$\alpha=0.5$\\$L^2$ integrable on $\mathbb{R}^2$")
            .set_color(BLUE)
            .scale(0.9)
            .move_to(4 * DOWN + 4 * RIGHT)
        )

        self.add_fixed_orientation_mobjects(left_label, right_label)
        self.set_camera_orientation(-PI / 6)

        self.add(
            axes_left, axes_right, kernel_left, left_label, kernel_right, right_label
        )
