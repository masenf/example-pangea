from pathlib import Path

import reflex as rx


IMAGE_DIR = Path(__file__).parent.parent / "assets" / "pangea"
N_IMAGES = len(list(IMAGE_DIR.glob("*.png"))) - 1


class State(rx.State):
    """The app state."""
    image_index: int = 0

    @rx.var
    def image_path(self) -> Path:
        return str(Path("pangea") / f"frame_{self.image_index:03d}.png")


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Forming the Continents", font_size="2em"),
            rx.slider(min_=0, max_=N_IMAGES, value=State.image_index, on_change=State.set_image_index, width="80vw"),
            rx.image(src=State.image_path, width="80vw"),
            rx.link("Source [Youtube]", href="https://youtu.be/OGdPqpzYD4o?feature=shared", as_="a"),
            spacing="1.5em",
            padding_top="5%",
        ),
        rx.script(
            src="//gc.zgo.at/count.js",
            custom_attrs={
                "data-goatcounter": "https://reflextoys.goatcounter.com/count"
            },
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(
    index,
    title="Forming the Continents",
    description="A series of images showing the formation of the continents from Pangea to Today.",
    image="/pangea/frame_000.png",
)
app.compile()
